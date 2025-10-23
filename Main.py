"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Jason Moore
ID: 110456746
Username: Moojr006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hackers import Hacker
from Rigs import Rig
from Asset import Assets



def player_creation(name):
    player = input("Enter your hacker name")
    name = Hacker(player)
    rig = input("Enter rig name")
    name.rig_acquisition(rig)
    return name


def manual_creation():
    hacker1 = Hacker("D3F@ULT")
    hacker1.rig_acquisition("Military pack")

    hacker2 = Hacker("T3@M P0IS0N")
    hacker2.rig_acquisition("Spy Pack")

    player_list = [hacker1, hacker2]

    return player_list

def damage_sequence(player_1, player_2):
    player_1.launch_data_spike(player_1, player_2)
    print(test[0])
    print(test[1])

    return player_1, player_2

def encrypt(hacker):
    '''Testing that includes creating the necessary items to test etc...'''
    choice = input("Encrypt with Security chip(Y/N)? ").upper()
    while choice != "Y" and choice != "N":
        choice = input("Encrypt with Security chip(Y/N)? ").upper()
    if choice == "Y":
        hacker.set_asset()
        asset_choice = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]
        choice1 = None
        while choice1 not in asset_choice:
            choice1 = input("Select an item to encrypt: ").title().strip()
        asset_encrypt = None
        for asset in hacker.get_list():
            if asset.name == choice1:
                asset_encrypt = asset
        for asset in hacker.get_list():
            if asset.name == "Security Chip":
                item = asset
        if asset_encrypt is None:
            return
        hacker.asset_encryption(asset_encrypt, item)
    else:
        asset_choice = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]
        choice1 = None
        while choice1 not in asset_choice:
            choice1 = input("Select an item to encrypt: ").title().strip()
        asset_encrypt = None
        for asset in hacker.get_list():
            if asset.name == choice1:
                asset_encrypt = asset
        for asset in hacker.get_list():
            if asset.name == "Security Chip":
                item = asset
        if asset_encrypt is None:
            return "Your do not have the specified item in your storage."
        hacker.asset_encryption(asset_encrypt, item)
    hacker.get_all_assets()
    print(hacker.get_asset(0).get_encrypt_asset())

def rig_upgrade(hacker):
    '''Select Hardware Patch'''
    choice = input("Upgrade without a rig (Y/N): ".upper())
    if choice == "Y":
        hacker.no_rig()
        print("You have removed your rig.")
    else:
        hacker.set_asset()

    return hacker

test = manual_creation()
encrypt(test[0])

print(test[0].get_all_assets())

print(test[0].get_rig())

for x in range(5):
    test[0].launch_data_spike(test[1], test[0]) #Battle simulation 1
    print(test[0])

test[0].rig_upgrade(test[0].get_rig(), test[0].get_asset(0))
print(test[0].get_rig())


