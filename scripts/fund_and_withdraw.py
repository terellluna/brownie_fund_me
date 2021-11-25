from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund_me():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()

    print(f"Teh current entry fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    withdrawal_amount = fund_me.withdraw({"from": account})
    print(f"Withdrew to {withdrawal_amount.value}")


def main():
    fund_me()
    withdraw()
