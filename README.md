# Transacting Multi-Block Chain Wallet

![newton](/Screenshots/newtons-coin-cradle.jpg)


## The Multi-Block Chain Wallet allows you to transact on  many different coins (Ex: Ethererum, Bitcoin, etc..)

## Background
Your new startup is focusing on building a portfolio management system that supports not only traditional assets
like gold, silver, stocks, etc, but crypto-assets as well! The problem is, there are so many coins out there! It's
a good thing you understand how HD wallets work, since you'll need to build out a system that can create them.
You're in a race to get to the market. There aren't as many tools available in Python for this sort of thing, yet.
Thankfully, you've found a command line tool, hd-wallet-derive that supports not only BIP32, BIP39, and BIP44, but
also supports non-standard derivation paths for the most popular wallets out there today! However, you need to integrate
the script into your backend with your dear old friend, Python.
Once you've integrated this "universal" wallet, you can begin to manage billions of addresses across 300+ coins, giving
you a serious edge against the competition.
In this assignment, however, you will only need to get 2 coins working: Ethereum and Bitcoin Testnet.
Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets.

## Dependencies


PHP must be installed on your operating system (any version, 5 or 7). Don't worry, you will not need to know any PHP.


You will need to clone the hd-wallet-derive tool.


bit Python Bitcoin library.


web3.py Python Ethereum library.

## Coding and Transaction Confirms

### __Deriving Wallet Keys__
![directory](/Screenshots/Wallet%20Derive%20Coins.png)


### __Generating Bitcoin-Test Transaction__

![bittest](/Screenshots/Bitcoin_Test.png)


### __Confirming Transaction on Block Explorer__

![confirmbtc](/Screenshots/Block_explorer_confirm.png)

### __As a good practice after testing, donate your faucet coins back__

![testnetback](/Screenshots/donate_back_testnet.png)

### __Same Format When Transacting with ETHER, just set Coin to "ETH" vs. "BTC"__

![testnet](/Screenshots/tx_testnet.png)


### __Confirm for Ethereum__

![etherconfirm](/Screenshots/Ether_confirm.png)
