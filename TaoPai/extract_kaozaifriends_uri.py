# coding: utf-8

import requests
import time
import sys

DETAIL_URL = "https://confluxscan.io/stat/nft/checker/detail?contractAddress=cfx:achew68x34cwu04aezbunyaz67gppakvmyn79tau56&tokenId={}"

def get_image_uri(token_id):
    resp = requests.get(DETAIL_URL.format(token_id))
    resp_json = resp.json()
    resp.close()
    return resp_json['data']['imageUri']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <start_token_id>.".format(sys.argv[0]))
        sys.exit(1)    

    start_token_id = int(sys.argv[1])

    # dump files
    token_cnt = 0
    with open("data/_extract_kaozaifriends_uris.csv", "a") as result_file:
        for token_id in range(start_token_id, 109629):
            image_uri = get_image_uri(token_id)
            result_file.write("{},{}\n".format(
                token_id, image_uri
            ))

            token_cnt += 1
            if token_cnt % 100 == 0:
                print("{} tokens.".format(token_cnt))
            
            time.sleep(0.3)