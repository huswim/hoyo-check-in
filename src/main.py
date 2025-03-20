import os
import logging
import requests


def load_env() -> tuple[str, str]:
    ltoken_v2 = os.environ.get('LTOKEN_V2')
    if ltoken_v2 is None or ltoken_v2 == '':
        logging.error('env LTOKEN_V2 is not set')
        exit(1)
    ltuid_v2 = os.environ.get('LTUID_V2')
    if ltuid_v2 is None or ltuid_v2 == '':
        logging.error('env LTUID_V2 is not set')
        exit(1)
    return ltoken_v2, ltuid_v2


def check_in(ltoken_v2: str, ltuid_v2: str, game: str) -> None:
    # data
    endpoints = {
        "hsr": "https://sg-public-api.hoyolab.com/event/luna/os/sign?act_id=e202303301540311",
        "zzz": "https://sg-public-api.hoyolab.com/event/luna/os/sign?act_id=e202406031448091"
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.6',
        'Connection': 'keep-alive',
        'Origin': 'https://act.hoyolab.com',
        'Referer': 'https://act.hoyolab.com',
        'Content-Type': 'application/json;charset=UTF-8',
        'Sec-CH-UA': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Platform': '"Linux"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        "x-rpc-signgame": f"{game}",
    }
    cookies = {
        'ltoken_v2': ltoken_v2,
        'ltuid_v2': ltuid_v2,
    }

    # choose endpoint (game)
    if game not in endpoints.keys():
        logging.error(f"game {game} is not supported")
        exit(1)

    # check-in
    response = requests.post(endpoints[game], headers=headers, cookies=cookies)
    json_data = response.json()

    # check result
    if json_data['retcode'] == 0:
        logging.info(f'{game} check-in success')
    elif json_data['retcode'] == -5003:
        logging.info(f'{game} already checked in')
    else:
        logging.error(f'{game} check-in failed')
        logging.error(json_data)
        exit(1)


def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('start check-in')

    ltoken_v2, ltuid_v2 = load_env()
    check_in(ltoken_v2, ltuid_v2, 'hsr') # 붕괴: 스타레일
    check_in(ltoken_v2, ltuid_v2, 'zzz') # 젠레스 존 제로


if __name__ == '__main__':
    main()
