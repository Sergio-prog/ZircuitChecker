from time import sleep

import requests

from fetch_wallets import get_all_wallets

url = "https://claim.zircuit.com/api/claim/"


def fetch_drop_amount(address: str, session: requests.Session = None):
    if not session:
        session = requests.Session()

    response = session.get(url + address)
    if response.status_code < 400:
        response_data = response.json()
        return int(response_data["claimableAmount"]) / 10 ** 18
    elif response.status_code == 404:
        return 0
    else:
        response.raise_for_status()


def main():
    wallets = get_all_wallets()
    session = requests.Session()

    print("========================================================")

    total_amount = 0
    for wallet in wallets:
        eligible_amount = round(fetch_drop_amount(wallet, session), 3)
        if eligible_amount <= 0:
            print(f"You are not eligible (0 $ZRC) in {wallet!r} account")
        else:
            print(f"You eligible for {eligible_amount} in {wallet!r} account")
            total_amount += eligible_amount
        print("========================================================\n")

        sleep(1)

    print("All wallets has been verified")
    print(f"Total amount: {total_amount}")


if __name__ == '__main__':
    main()
