
# Set imports
import subprocess
import json
from constants import *
from web3 import Web3
import os
from dotenv import load_dotenv
from eth_account import Account
from pathlib import Path
from bit import wif_to_key, PrivateKeyTestnet, PrivateKey, Key
from getpass import getpass

load_dotenv()

# Set env to call mnemonic
mnemonic = os.getenv('mnemonic')

# Alternative Way to run function
def derive_wallets2(mnemonic, coin, numderive):
    """Use the subprocess library to call the php file script from Python"""
    command2 = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --cols=address,index,path,privkey,pubkey,pubkeyhash,xprv,xpub --numderive="{numderive}" --coin="{coin}" --format=json'
    p = subprocess.Popen(command2, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return  keys

keys = {}
for coin in coins:
    keys[coin]= derive_wallets2(os.getenv('mnemonic'), coin, numderive)

# Need address to prefund an account on the BTC Transaction Below
keys['btc-test'][0]['address']

keys['btc-test'][0]['privkey']

#Activate w3 for Ether Transactions
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))



# Create 3 Functions 1 of 3
def priv_key_to_account(coin, priv_key):
    '''Convert the privkey string in a child key to an account object that bit or web3.py can use'''
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
eth_account = priv_key_to_account(ETH,eth_privatekey)
btc_account = priv_key_to_account(BTCTEST,btc_privatekey)

# Create Function 2 of 3
def create_tx(coin, account, recipient, amount):
    """create the raw, unsigned transaction that contains all metadata needed to transact"""
    if coin ==ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": recipient, "value": amount})
        return{
            "to": recipient,
            "from": account.address,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address)
        }
    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])


# Create Function 3 of 3
def send_tx(coin, account, recipient, amount):
    """call create_trx, sign the transaction, then send it to the designated network"""
    if coin =='eth':
        txn = create_tx(coin, account, recipient, amount)
        signed_txn = w3.eth.account.signTransaction(txn)
        result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(result.hex())
        return result.hex()

    else:
        tx_btctest= create_tx(coin, account, recipient, amount)
        sign_tx_btctest = account.sign_transaction(tx_btctest)
        from bit.network import NetworkAPI
        NetworkAPI.broadcast_tx_testnet(sign_tx_btctest)       
        return sign_tx_btctest

# Set up Priv Keys for Transacting Ether and Bit Test Accounts
print(eth_account)
print(btc_account)



# Get Regenerated Keys for BTC Test
priv_key_to_account('btc-test', 'L4deU51hpuykPshbG76LtyubVC4JfDGV8XA5ZEh7FrqjMwuyoFZ2')

# Create Transaction in BTC Test - 
create_tx('btc-test',btc_account, 'msS23qy5RdK7CWQS2yFoRGDewA6RbFZYhh', .0001)

# Send Transaction - 
send_tx('btc-test',btc_account,'msS23qy5RdK7CWQS2yFoRGDewA6RbFZYhh',0.000001)



