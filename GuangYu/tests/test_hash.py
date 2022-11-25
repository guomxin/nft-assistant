import hashlib
import requests
import time

GET_ON_SALE_LIST_URL = "https://api.gandart.com/market/api/v2/resaleManage/resale/onSale"

def get_md5_hash(s3):
    _0x14b4f0 = ["e9", "0a", "9", "29", "e", "c" , "3"]
    merged = str(s3) + "".join(_0x14b4f0)
    return hashlib.md5(merged.encode(encoding="utf-8")).hexdigest()

def post_requests_json(url, data, timeout):
    for _ in range(10):
        try:
            res = requests.post(url, data=data, timeout=timeout).json()
            return res
        except Exception as e:
            time.sleep(3)
            print(e)

def get_top_saling_products(casting_id):
    saling_prods = []
    s2 = int(time.time() * 1000)
    s1 = s2 - 20000
    s3 = s2 + 20000
    s4 = s2 + 40000
    data = {
        "castingId": casting_id,
        "page":1,
        "pageSize":50,
        "sort":2,
        "transactionStatus": 1,
        #"s1": s1,
        #"s2": s2,
        "s3": s3,
        #"s4": s4,
        "s5": get_md5_hash(s3),
    }
    res = post_requests_json(GET_ON_SALE_LIST_URL, data, 3)
    if not res:
        return (1, None)
    if res["code"] != 0:
        return (res["code"], None)
    else:
        for pinfo in res["obj"]["list"]:
            saling_prods.append(
                [pinfo["id"], pinfo["viewSort"], float(pinfo["resalePrice"]), pinfo["transactionStatus"]])
    return (0, saling_prods)

if __name__ == "__main__":
    s1 = 1669370494564
    s2 = 1669370514564
    s3 = 1669370534564
    s4 = 1669370554564
    correct_hash = "3e79c37e5ab14ccbecf86788bf10058b"
    """
    right_hash = "3e79c37e5ab14ccbecf86788bf10058b"
    _0x14b4f0 = ["e9", "0a", "29", "e", "c" , 3]
    _0x14b4f0 = ["e9", "0a", "9", "29", "e", "c" , "3"]
    merged = str(s3) + "".join(_0x14b4f0)
    print(merged)
    print(hashlib.md5(merged.encode(encoding="utf-8")).hexdigest()) #3e79c37e5ab14ccbecf86788bf10058b
    """
    print(get_md5_hash(s3) == correct_hash)
    print(get_top_saling_products(154))