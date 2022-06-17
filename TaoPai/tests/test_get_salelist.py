import requests
import json

Cookie_Dict_1 = {
# 173****6961
    'refreshToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTU3NzUyMTEsImlhdCI6MTY1MzE4MzIxMSwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.5xoBKU1YsDWBPMd3PQG4ba8T0onhMDFWnAHw4Gns7MU',
    'accessToken': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTMxODM4MTEsImlhdCI6MTY1MzE4MzIxMSwidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.OCTI4aGEIVZFTCZEA8OWnwZNR65UAi2EwlmxcoNllj4',
    'cert': '1',
}

POST_URL = "https://nft.taopainft.com/v1/market/v2/product/list"

if __name__ == "__main__":
    data = {
        "marketType": 1,
        "offset": 0,
        "limit": 20,
        "types": "all",
        "publisherId": 35,
        "name": "",
        "sortType": 4,
        "virtualCategory": 133
    }
    headers = {
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTU0MjkzODMsImlhdCI6MTY1NTQyODc4MywidXNlclVJRCI6eyJ1c2VySWQiOjEyMDQyfX0.zabbzjw-6sW4RfJlAaIXL1A63C5t72m2_wPH6BxSSeg",

    }
    res = requests.post(POST_URL, data=json.dumps(data), cookies=Cookie_Dict_1, headers=headers)
    print(res.json())
    #print(res["data"]["list"][0])