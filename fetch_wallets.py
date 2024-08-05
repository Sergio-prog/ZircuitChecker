from pathlib import Path

file_path = Path(__file__).parent / "data" / "wallets.txt"


def get_all_wallets():
    with open(file_path, "r") as file:
        wallets = file.readlines()
        wallets = map(lambda x: x.strip(), wallets)
        wallets = filter(lambda x: x != "", wallets)
        return wallets
