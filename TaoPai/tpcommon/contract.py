# coding: utf-8

from conflux import (
    Conflux,
    HTTPProvider,
    Address
)

def get_contract_address_ABI_from_name(name):
    if name == "liuangel":
        return (XY_Contract_Address, TaoPai_ABI)
    elif name == "aprilkaozai":
        return (ConFashion_Contract_Address, TaoPai_ABI)
    elif name == "atsj":
        return (ATSJ_Contract_Address, TaoPai_ABI)
    elif name == "chaohu":
        return (COCAFE_Contract_Address, TaoPai_ABI)
    elif name == "dunhuang" or name == "hutoufeitian":
        return (SDQH_Contract_Address, TaoPai_ABI)
    elif name == "lt":
        return (LT_Contract_Address, TaoPai_ABI)
    elif name == "qiannian":
        return (JYY_Contract_Address, TaoPai_ABI)
    elif name == "taopainft":
        return (TaopaiNFT_Contract_Address, TaoPai_ABI)
    elif name == "guizi":
        return (UXON_Contract_Address, TaoPai_ABI)
    elif name == "shangshi":
        return (HYYS_Contract_Address, TaoPai_ABI)
    elif name == "tiantanbopu":
        return (YQXK_Contract_Address, TaoPai_ABI)
    elif name == "feitianpiba":
        return (TLH_Contract_Address, TaoPai_ABI)
    elif name == "huoxingtance":
        return (UOVA_Contract_Address, TaoPai_ABI)
    elif name == "kaozaifriends":
        return (TaopaiNFT_Contract_Address, TaoPai_ABI)
    elif name == "hangtiantanwei2":
        return (ZGHT_Contract_Address, TaoPai_ABI)
    elif name == "zhongguohangtian":
        return (HTKJ_Contract_Address, TaoPai_ABI)
    elif name == "changgexing":
        return (HC_Contract_Address, TaoPai_ABI)
    else:
        return (None, None)

def get_base32addr_from_hexaddr(hexaddr):
    addr = Address.create_from_hex_address(hexaddr, MainNet_NetworkId)
    return addr.address

def token_id_in_ranges(token_id, ranges):
    for (min_tid, max_tid) in ranges:
        if (token_id >= min_tid) and (token_id <= max_tid):
            return True
    return False

MainNet_NetworkId = 1029
def dump_contract_details(contract_address, contract_ABI, dump_file_name, ranges, verbose=True):
    provider = HTTPProvider('https://main.confluxrpc.com')
    c = Conflux(provider)

    owner2tokens = {}
    token_cnt = c.call_contract_method(contract_address, contract_ABI, 'totalSupply')
    _, token_ids = c.call_contract_method(contract_address, contract_ABI, 'tokens', 0, token_cnt)
    target_token_cnt = 0
    for token_id in token_ids:
        if not token_id_in_ranges(token_id, ranges):
            continue
        owner = c.call_contract_method(contract_address, contract_ABI, 'ownerOf', token_id)
        owner = get_base32addr_from_hexaddr(owner)
        if owner not in owner2tokens:
            owner2tokens[owner] = []
        owner2tokens[owner].append(token_id)
        target_token_cnt += 1
        if verbose:
            if target_token_cnt % 500 == 0:
                print("{} tokens scanned.".format(target_token_cnt))

    if verbose:
        print("{} tokens, {} owners.".format(target_token_cnt, len(owner2tokens)))

    # dump file
    owner_tokencnt_list = []
    for (owner, tokens) in owner2tokens.items():
        owner_tokencnt_list.append((owner, len(tokens)))
    owner_tokencnt_list.sort(key=lambda p: p[1], reverse=True)

    result_file = open(dump_file_name, "w")
    for (owner, _) in owner_tokencnt_list:
        tokens = owner2tokens[owner]
        result_file.write("{},{},{}\n".format(
            owner,
            len(tokens),
            ":".join([str(token_id) for token_id in tokens])
        ))
    result_file.close()


def dump_contract_tokenid2owner(contract_address, contract_ABI, dump_file_name, min_tid=-1, max_tid=-1, verbose=True):
    provider = HTTPProvider('https://main.confluxrpc.com')
    c = Conflux(provider)

    tokenid_owner_list = []
    token_cnt = c.call_contract_method(contract_address, contract_ABI, 'totalSupply')
    _, token_ids = c.call_contract_method(contract_address, contract_ABI, 'tokens', 0, token_cnt)
    target_token_cnt = 0
    for token_id in token_ids:
        if (min_tid != -1) and token_id < min_tid:
            continue
        if (max_tid != -1) and token_id > max_tid:
            continue
        owner = c.call_contract_method(contract_address, contract_ABI, 'ownerOf', token_id)
        owner = get_base32addr_from_hexaddr(owner)
        tokenid_owner_list.append((token_id, owner))

        target_token_cnt += 1
        if verbose:
            if target_token_cnt % 500 == 0:
                print("{} tokens scanned.".format(target_token_cnt))

    if verbose:
        print("{} tokens.".format(len(tokenid_owner_list)))


    result_file = open(dump_file_name, "w")
    for (token_id, owner) in tokenid_owner_list:
        result_file.write("{},{}\n".format(
            token_id,
            owner
        ))
    result_file.close()

ATSJ_Contract_Address ="cfx:acb7hr0ecyatev5gzjnys9mt31xxa22hzuzb3tprps"
LT_Contract_Address = "cfx:acaha2pz5j1g6b0fbv9xazv5umm587xucjcdu83b02"
SDQH_Contract_Address = "cfx:acff8dvjv6pys2ws19dhx753h1h00sum6yhu3m188h"
JYY_Contract_Address = "cfx:acb30r4jzu5ek6espf9mzz7nbnhwjeddej91cdb9uf"
TaopaiNFT_Contract_Address = "cfx:achew68x34cwu04aezbunyaz67gppakvmyn79tau56"
COCAFE_Contract_Address = "cfx:acgjw8bg7gehy3x7x5evfknfe7pst64hp6tgymfwa4"
XY_Contract_Address = "cfx:acdvdbkwm4r8jakn721bz8gmyc3m2tf1xj8z0w7rh7"
ConFashion_Contract_Address = "cfx:acejnvw0k2zjew74uv570fbrgp2ns541wenhxnjkkv"
UXON_Contract_Address = "cfx:acewxuum66yyw5wzrux05nbt8crdhxu0buf8x381h3"
HYYS_Contract_Address = "cfx:acft8mk0tc2y7ngt8ud0h0cwzt74g8zauasfdmbf03"
YQXK_Contract_Address = "cfx:acexxkwh0yr694avgh599ej0gx0kn9871j9nh7rjr0"
TLH_Contract_Address = "cfx:acdakam9fnb6wa4syv8mpsvg7thda574a67ymag145"
UOVA_Contract_Address = "cfx:acgd354zys91dmd56gc049zdv686t9arr6axahp5up"
ZGHT_Contract_Address = "cfx:achugufke20aym8exsrhr5gkaxr49ae98a0nncyyy0"
HTKJ_Contract_Address = "cfx:acby6g5sg4v7cufsbrhbwccu591tpv30865ubenucn"
HC_Contract_Address = "cfx:ach5xttx9vgxuu18hg2hhegpavrv6c7d3urdj6zbu8"

TaoPai_ABI = """
[{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"symbol","type":"string"},{"internalType":"string","name":"tokenPlaceholderURI","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"BURNER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"METADATA_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PAUSER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TRANSFER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"burnBatchByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"burnByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32[]","name":"roles","type":"bytes32[]"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRoleBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"count","type":"uint256"}],"name":"mintBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenIdStart","type":"uint256"},{"internalType":"uint256","name":"count","type":"uint256"}],"name":"mintBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"mintBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFromByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFromByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"tokenPlaceholderURI","type":"string"}],"name":"setTokenPlaceholderURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"uri","type":"string"}],"name":"setTokenURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"offset","type":"uint256"},{"internalType":"uint256","name":"limit","type":"uint256"}],"name":"tokens","outputs":[{"internalType":"uint256","name":"total","type":"uint256"},{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"offset","type":"uint256"},{"internalType":"uint256","name":"limit","type":"uint256"}],"name":"tokensOf","outputs":[{"internalType":"uint256","name":"total","type":"uint256"},{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFromByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"}]
"""