from scripts.helpful_scripts import get_account
from brownie import interface, network, config


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    # In order to use existing contract...
    # ABI
    # Address
    account = get_account()
    # Better practice to use get_contract function. Using this for simplicity
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    print("Received 0.1 WETH!")
    return tx
