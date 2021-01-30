# TradeBoost

![Hello](https://i.imgur.com/LzANd6f.png)


### ***It's utility for boosting trades on Steam***
Using two steam accounts with a shared secret and an identity secret, we will constantly send and receive trades to each other.

-------------------------

### Installation

```
💲 git clone https://github.com/dotX12/TradeBoost/
💲 cd TradeBoost
💲 pip3 install -r requirements.txt
```

### settings.py

The settings folder contains JSON files of accounts, configure them.

```
{
    "login": "", # Steam login
    "password": "", # Steam password
    "API": "", # API https://steamcommunity.com/dev/apikey
    "steamid": "", # STEAM ID 
    "shared_secret": "", # shared_secret from mafile
    "identity_secret": "" # identity_secret from mafile
}
```

### tokens.py

We specify the STEAM ID separated by commas to whom we will send all our trades!
That is, we indicate the STEAM ID of our second account!

```
account_1 = ['settings/account1.json', '7656119833XXXXXXX']
account_2 = ['settings/account2.json', '7656119835XXXXXXX']

```

    Once configured, run the main.py

The approximate number of exchanges in 30 minutes is 300-400, depending on the load of Steam.



---

### But what about threads or async?

Steam is a very unstable thing and even with two different streams I catch a bunch of errors ranging from trying to get inventory to trying to accept a trade. After various tests, it turned out that the regular synchronous version performed best.

