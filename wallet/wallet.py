# Set imports
import subprocess
import json
#from constants import *
#from web3 import Web3
import os
#from dotenv import load_dotenv
#from eth_account import Account
from pathlib import Path

#load_dotenv()

# Set env to call mnemonic
mnemonic = os.getenv('mnemonic')

def derive_wallets(mnemonic, coin, numderive):
    """Use the subprocess library to call the php file script from Python"""
    command = f'./derive -g --mnemonic="{mnemonic}" --cols=address,index,path,privkey,pubkey,pubkeyhash,xprv,xpub --coin="{coin}" --numderive="{numderive}" --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    # read data from standard output and err
    (output, err) = p.communicate()
    # Need to wait for child process to terminate - allows you to run process. 
    p_status = p.wait()
    keys = json.loads(output)
    return keys

# Add to function 
coins = ["eth", "btc-test", "btc"]
numderive=3

# Call the function iterating through the coins using dict comprehension
{coin: derive_wallets(os.getenv('mnemonic'), coin, numderive) for coin in coins}

