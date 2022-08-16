# coding: utf-8
import time
import requests

from conflux import (
    Conflux,
    HTTPProvider,
    Address
)

def get_contract_address_ABI_from_name(name):
    if name == "liuangel":
        return (XY_Contract_Address, TaoPai_ABI)
    elif name == "aprilkaozai" or name == "kaozaikaituo":
        return (ConFashion_Contract_Address, TaoPai_ABI)
    elif name == "atsj":
        return (ATSJ_Contract_Address, TaoPai_ABI)
    elif name == "chaohu":
        return (COCAFE_Contract_Address, TaoPai_ABI)
    elif name == "dunhuang" or name == "hutoufeitian" or name == "sdqhchuangshi":
        return (SDQH_Contract_Address, TaoPai_ABI)
    elif name == "lt" or name == "ltcard" or name == "huakaiyunqi":
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
    elif name == "kaozaifriends" or name == "kaozaifriends2":
        return (TaopaiNFT_Contract_Address, TaoPai_ABI)
    elif name == "hangtiantanwei2":
        return (ZGHT_Contract_Address, TaoPai_ABI)
    elif name == "zhongguohangtian":
        return (HTKJ_Contract_Address, TaoPai_ABI)
    elif name == "changgexing" or name == "yujunqiasi" or name == "huacedatu" or name == "pinglan":
        return (HC_Contract_Address, TaoPai_ABI)
    elif name == "taopai2022":
        return (TaopaiNFT_Contract_Address, TaoPai_ABI)
    elif name == "taopaitest":
        return (TaopaiNFT_Contract_Address, TaoPai_ABI)
    elif name == "taopaichuangshi":
        return (TaopaiNFT_Contract_Address, TaoPai_ABI)
    elif name == "baibianxiong" or name == "baibianxiong3":
        return (BOOOM_Contract_Address, TaoPai_ABI)
    elif name == "laodongcun" or name == "laodongcun2":
        return (UXON_Contract_Address, TaoPai_ABI)
    elif name == "xunzhang":
        return (TaopaiNFT_Contract_Address, TaoPai_ABI)
    elif name == "letaotao":
        return (TaopaiNFT_Contract_Address, TaoPai_ABI)
    elif name == "fxpanda" or name == "fxpanda2" or name == "fxpandaall" or name == "pcatmem" or name == "fxxunzhang" \
        or name == "fxfuneng":
        return (FXHE_Contract_Address, TaoPai_ABI)
    elif name == "partycat":
        return (PartyCat_Contract_Address, TaoPai_ABI)
    elif name == "shuijing":
        return (YCY_Contract_Address, TaoPai_ABI)
    elif name == "saiboyouling":
        return (XJH_Contract_Address, TaoPai_ABI)
    elif name == "bobosg":
        return (BOBOSG_Contract_Address, TaoPai_ABI)
    elif name == "limitless":
        return (Limitless_Contract_Address, TaoPai_ABI)
    elif name == "dftyrb":
        return (DFTYRB_Contract_Address, TaoPai_ABI)
    elif name == "xiyouxingqiu":
        return (TCJC_Contract_Address, TaoPai_ABI)

    #--- 豹豹青春宇宙 ---#
    elif name == "kaoshenglaile":
        return (KaoShengLaiLe_Contract_Address, TaoPai_ABI)
    elif name == "tongjing":
        return (TongJing_Contract_Address, TaoPai_ABI)
    #--- 豹豹青春宇宙 ---#
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
    token_ids = []
    for index in range(0, token_cnt, 10000):
        _, tids = c.call_contract_method(contract_address, contract_ABI, 'tokens', index, 10000)
        token_ids.extend(tids)
    target_token_cnt = 0
    for token_id in token_ids:
        if not token_id_in_ranges(token_id, ranges):
            continue
        while True:
            # 此接口容易出错，失败之后再次尝试
            try:
                owner = c.call_contract_method(contract_address, contract_ABI, 'ownerOf', token_id)
                break
            except Exception as e:
                print(e)
                time.sleep(1)
        owner = get_base32addr_from_hexaddr(owner)
        if owner not in owner2tokens:
            owner2tokens[owner] = []
        owner2tokens[owner].append(token_id)
        target_token_cnt += 1
        if verbose:
            if target_token_cnt % 500 == 0:
                print("{} tokens scanned.".format(target_token_cnt))
        
        # for too many requests error
        time.sleep(0.2)

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
    token_ids = []
    for index in range(0, token_cnt, 10000):
        _, tids = c.call_contract_method(contract_address, contract_ABI, 'tokens', index, 10000)
        token_ids.extend(tids)
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

DETAIL_URL = "https://api.confluxscan.net/nft/preview?contract={}&tokenId={}&withMetadata=false"

def get_token_name(contract_address, token_id):
    for _ in range(10):
    # 最多试10次
        try:
            resp = requests.get(DETAIL_URL.format(contract_address, token_id))
            resp_json = resp.json()
            return resp_json['data']['name']
        except Exception as e:
            print(resp_json, e)
            print("fetch {} info error".format(token_id))

def dump_contract_tokenid2name(contract_address, contract_ABI, dump_file_name, ranges=[], verbose=True):
    provider = HTTPProvider('https://main.confluxrpc.com')
    c = Conflux(provider)

    tokenid_name_list = []
    token_cnt = c.call_contract_method(contract_address, contract_ABI, 'totalSupply')
    token_ids = []
    for index in range(0, token_cnt, 10000):
        _, tids = c.call_contract_method(contract_address, contract_ABI, 'tokens', index, 10000)
        token_ids.extend(tids)
    target_token_cnt = 0
    for token_id in token_ids:
        if not token_id_in_ranges(token_id, ranges):
            continue
        token_name = get_token_name(contract_address, token_id)
        tokenid_name_list.append((token_id, token_name))
        print("{}:{}".format(token_id, token_name))
        target_token_cnt += 1
        if verbose:
            if target_token_cnt % 500 == 0:
                print("{} tokens scanned.".format(target_token_cnt))
        time.sleep(1)
    if verbose:
        print("{} tokens.".format(len(tokenid_name_list)))


    result_file = open(dump_file_name, "w")
    for (token_id, token_name) in tokenid_name_list:
        result_file.write("{},{}\n".format(
            token_id,
            token_name
        ))
    result_file.close()

BOOOM_Contract_Address = "cfx:acaxpets034fjcp73fj5x1eveut913a752jtbkc3as"
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
FXHE_Contract_Address = "cfx:acdu30v7932jzugkwt7v97bdykb6ydfkk22b3s4953"
YCY_Contract_Address = "cfx:ach23g5h9ahphbgrt314156eu53vgrx1ay83pgnphd"
XJH_Contract_Address = "cfx:acgg9rtk6f3mfa05hssabwpkexf3guahb26dgx1ek2"
BOBOSG_Contract_Address = "cfx:acc3ea44baypswat4s37wvyk0ewc6e6bnevs8zvnj1"
Limitless_Contract_Address = "cfx:acbmhd5km15u68eyy17xusmr5a1jy1hthuavs06mhw"
PartyCat_Contract_Address = "cfx:acdj66ya20g2b5j9me489pmrv4bu60ut32hjfpxpgp"
DFTYRB_Contract_Address = "cfx:aca8tg7zd85zth9hmw92ucxajgnxuwfd4j4uucd61b"
TCJC_Contract_Address = "cfx:achmp3kyw693n9d0fftjbvsy06a5zp6g1axypnvyte"

Bosie_Contract_Address = "cfx:accvuj004k127vd4cprcfju1wzw4pm5bj6u1gkvtds"
XY_Contract_Address = "cfx:acappbfbk3xh5ptt60xugbgyut6jvwja3e80bzrj98"
XMZDY_Contract_Address = "cfx:accj4mwd3172x4ahak2jzphw3dragg399jgn47crpu"
MGKJ_Contract_Address = "cfx:acgs9h18atyd9ubsgy48am8xxtaeuye4makpcsdp5w"
SZK_Contract_Address = "cfx:acfbyvmgd0hmrgbfxaphb5u9pt2mesvhn6m8rxr8pj"
PolisSpace_Contract_Address = "cfx:achcs1t9xhu97ufjspwpn5g37ja9cznc0yfd1xyn10"
YCF_Contract_Address = "cfx:aceue8g8013k4aysvm0jxht4xdyavjvd1un6nbdz0s"
GoofyCity_Contract_Address = "cfx:aca9f9u4nxy97tu0ydsy4p6wepnmvcmb3ek97ueucn"
SJWH_Contract_Address = "cfx:acgpwdyjcx5tpufj7x6taw1f3r3jpu2x0pjx33xyyt"
KZJG_Contract_Address = "cfx:acbs61xtcfe001au604nrf207pn2u4pdeawpx3f782"
JYY_Contract_Address = "cfx:acb30r4jzu5ek6espf9mzz7nbnhwjeddej91cdb9uf"
YSWJ_Contract_Address = "cfx:acc8vpap61kdxa7sv769c62vx1n5phh83619ccxp3v"

ContractAddress2Id = {
# ContractId通过https://nft.taopainft.com/v1/market/v2/product/list接口返回获得contractId
    TaopaiNFT_Contract_Address: 2,
    FXHE_Contract_Address: 37,
    BOOOM_Contract_Address: 50,
    PartyCat_Contract_Address: 61,
    UXON_Contract_Address: 41,
    YCY_Contract_Address: 54,
    Limitless_Contract_Address: 59,
    SDQH_Contract_Address: 22,
    LT_Contract_Address: 30,
    COCAFE_Contract_Address: 46,
    BOBOSG_Contract_Address: 57,
    HC_Contract_Address: 31,
    XJH_Contract_Address: 55,
    ZGHT_Contract_Address: 36,
    YQXK_Contract_Address: 27,
    ConFashion_Contract_Address: 8,
    HTKJ_Contract_Address: 49,
    TLH_Contract_Address: 48,
    HYYS_Contract_Address: 34,
    XMZDY_Contract_Address: 32, # 熊猫总动员: 32,
    Bosie_Contract_Address: 14, # Bosie: 14,
    MGKJ_Contract_Address: 18, # 芒果科技: 18,
    SZK_Contract_Address: 29, # 深圳客: 29,
    UOVA_Contract_Address: 13,
    PolisSpace_Contract_Address: 3,# PolisSpace: 3,
    ATSJ_Contract_Address: 40,
    YCF_Contract_Address: 35, # 御赐福: 35,
    GoofyCity_Contract_Address: 24, # GoofyCity: 24,
    XY_Contract_Address: 19, # 星源（唐卡等）: 19,
    SJWH_Contract_Address: 26, # 舍九文化: 26,
    KZJG_Contract_Address: 28, # 烤仔建工: 28,
    JYY_Contract_Address: 15, # 金羽翼: 15,
    # TODO: DAO纪念
    YSWJ_Contract_Address: 23, #艺术玩家实验室: 23,
    TCJC_Contract_Address: 64, # 西游星球
    # TODO: Luluz, 王星星, Misaki, YSX, 不走调音乐社, YAO, WPP 
}

KaoShengLaiLe_Contract_Address = "cfx:achm40d1fuwpfxe1azk6ty607fpmdrsczpy5pcexuz"
TongJing_Contract_Address = "cfx:acgj9wmbe97vaf7c53mekz0r6vj9d5y7myeget3fu7"
HangTianQingNian_Contract_Address = "cfx:acfdpvhhnyk2xcuagjd3n314574b7y9zd6zty8pna6"
LSGT_Contract_Address = "cfx:acebjnmrz6pnauwy1cuk19vc8hb71tfc3u3zt6dyt9"
QJD_Contract_Address = "cfx:aceenx0x8k58g6s1gbgyptk1xf9jvfztwuzfmg7b96"
QJDMBY_Contract_Address = "cfx:accm4gvrern444gvwr2hy7szhxtbspd19ykc497zp8"
QJDMBYSi_Contract_Address = "cfx:acdxeh7a12gtdc3v74smzx7pa9hw05exb2kmext88h"
QJDMBYFv_Contract_Address = "cfx:acbz4f5stmxtsmu1p6uutnfj4x1wt7wmyy33hyh5ds"
QJDMBYFo_Contract_Address = "cfx:acbj1f6mppdvfnkmena3am9fea3f6th9vujfh88jrh"
QJDMBYTh_Contract_Address = "cfx:ach151pkn88j3bnusd4u5p9sszhmwah9ay7uc2gb72"
QJDMBYFi_Contract_Address = "cfx:achst4kxy4exe7uft39xdc7e5pdu37daaupjzhva8n"
QJDMBYTo_Contract_Address = "cfx:acg3j2hmxzcm2fu386vt391rkub1wctxgjgjjgncd6"
WBQY_Contract_Address = "cfx:ach8xv5fb03vjdcda5mdjtsrwnrn6sfgfy5nzej8vg"
HYM_Contract_Address = "cfx:accvhm4yh1xspj5ewb3jk1fw87uvravg2jufd7nac7"
ZGQNB_Contract_Address = "cfx:acd6uyfdm9j90k4nzjra5786x7fhne10yyygbhwjju"
KKX_Contract_Address = "cfx:acb6g1zcwk18w77v1aj0z1te49ux2arkk2vmzgcwvn"
LQBJ_Contract_Address = "cfx:acbu6n7kb7yw3h8m3323a989fmamdranpamtakuwnz"
JQ_Contract_Address = "cfx:aceu8rcsg16f3s1exambfac1xpa326k8g2w885ub7g"
QXLX_Contract_Address = "cfx:acc46dvwz5jpj8nxzcr2cjhewfjd9xcpte0fk8e4j4"
CJZ_Contract_Address = "cfx:achtgrev6s2sn9ekkgybbm79m59zj6chnjhgyg0x2p"
RYZ_Contract_Address = "cfx:acgcbwrwm0eysx8xp3dxsm5a7ypbux02a24wmhwtb2"
HTZ_Contract_Address = "cfx:acgrgnbckwuh6ckmxmfd0r7psstu8bv9eu8npdsa1w"
TD_Contract_Address = "cfx:acffc81krae11vd395v50u1p8kyb828dyjhv9h4huk"
HJ_Contract_Address = "cfx:acgzpncte8che3g7gewprt19bvk7p920tjukva5hys"
AYTK_Contract_Address = "cfx:acgk5c07j7yxvu2h5r1yeuxmb6xsv5a0ta5k9w4cxd"
GRDZ_Contract_Address = "cfx:acekmy4nsa8d5rardfa33bsp4c11ck27he87vb8ctk"
AYXL_Contract_Address = "cfx:acdt8kdv908ntcpuueb9fyyn0y0nnwf7spp0j7xe6n"
ELC_Contract_Address = "cfx:acdbnea1z1dx1e4j9pc50a91ydb9a2a8yj23d50gws"

BaoBao_Contract_Dict = {
    KaoShengLaiLe_Contract_Address: 1,
    TongJing_Contract_Address: 1,
    HangTianQingNian_Contract_Address: 1,
    LSGT_Contract_Address: 1,
    QJD_Contract_Address: 1,
    QJDMBY_Contract_Address: 1,
    QJDMBYTh_Contract_Address: 1,
    QJDMBYFi_Contract_Address: 1,
    QJDMBYFo_Contract_Address: 1,
    QJDMBYFv_Contract_Address: 1,
    QJDMBYSi_Contract_Address: 1,
    QJDMBYTo_Contract_Address: 1,
    WBQY_Contract_Address: 1, # TODO: 需要确认 2022/7/14
    HYM_Contract_Address: 1,
    ZGQNB_Contract_Address: 1,
    KKX_Contract_Address: 1,
    LQBJ_Contract_Address: 1,
    JQ_Contract_Address: 1,
    QXLX_Contract_Address: 1,
    CJZ_Contract_Address: 1,
    RYZ_Contract_Address: 1,
    HTZ_Contract_Address: 1,
    TD_Contract_Address: 1,
    HJ_Contract_Address: 1,
    AYTK_Contract_Address: 1,
    GRDZ_Contract_Address: 1,
    AYXL_Contract_Address: 1,
}

def is_taopai_contract(contract_address):
    return contract_address not in BaoBao_Contract_Dict

TaoPai_ABI = """
[{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"symbol","type":"string"},{"internalType":"string","name":"tokenPlaceholderURI","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"inputs":[],"name":"BURNER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"METADATA_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINTER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PAUSER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TRANSFER_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"burnBatchByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"burnByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32[]","name":"roles","type":"bytes32[]"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRoleBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"count","type":"uint256"}],"name":"mintBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenIdStart","type":"uint256"},{"internalType":"uint256","name":"count","type":"uint256"}],"name":"mintBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"mintBatch","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFromByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFromByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"tokenPlaceholderURI","type":"string"}],"name":"setTokenPlaceholderURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"string","name":"uri","type":"string"}],"name":"setTokenURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"offset","type":"uint256"},{"internalType":"uint256","name":"limit","type":"uint256"}],"name":"tokens","outputs":[{"internalType":"uint256","name":"total","type":"uint256"},{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"offset","type":"uint256"},{"internalType":"uint256","name":"limit","type":"uint256"}],"name":"tokensOf","outputs":[{"internalType":"uint256","name":"total","type":"uint256"},{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFromByAdmin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"}]
"""