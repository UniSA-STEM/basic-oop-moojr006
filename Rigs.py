"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Jason Moore
ID: 110456746
Username: Moojr006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Assets


class Rig:
    import random
    def __init__(self, name):
        self.name = name
        self.__damage_counter = 0
        self.__broken = False
        self.__storage = [Assets("data spike", "Used in battles"), Assets("data spike", "Used in battles")]
        self.__storage_limit = 5
        self.__level = 0
        self.__max_damage = self.__level + 2

    def __str__(self):
        """Method to display key information about the rig instance."""
        return f"""Rig name:{self.name}
Rig damage:{self.__damage_counter}
Rig broken?:{self.__broken}
Rig inventory:{self.__storage}
Rig level:{self.__level}"""


    def get_storage(self):
        """Getter method to display objects in storage."""
        return [asset for asset in self.__storage]

    def set_value(self, list):
        """Setter method to encrypt an asset object in storage."""
        self.__storage[0].__encrypted = True
        print(self.__storage[0].__encrypted)


    def get_broken_status(self):
        """Getter method to display get_broken status."""
        return self.__broken

    def get_rig_damage(self):
        """Getter method to display rigs current damage."""
        return self.__damage_counter

    def set_repair(self, crypto_token):
        """Setter method to repair rigs damage using a crypto token."""
        if crypto_token  == "cryptotoken" and self.__damage_counter > 0: # add .name after asset is ready
            self.__damage_counter = 0
            self.__broken = False
        else:
            print("Rig is not damaged, no repair needed")


    def repair(self, crypto_token):
        """Wrapper method to set_repair(self, crypto_token)."""
        return self.set_repair(crypto_token)


    def set_upgrade(self):
        """Upgrades the level of the hackers rig by consuming a hardware patch.
        Only upgrade while the hackers rig has not reached 5."""
        if "hardware patch" not in self.__storage:
            print("You do not have a hardware patch in your inventory")
            return

        if self.__level  < 5:
            self.__level += 1
            self.__storage_limit += 2
            self.__storage.remove("hardware patch")
        else:
            print("Rig has reached max level of 5")



    def upgrade(self):
        """Wrapper method to set_upgrade(self)."""
        return self.set_upgrade()


    def set_damage(self, data_spike):
        """Apply damage to rig instance whilst consuming a data spike.
        If damage reaches max damagge the rig becomes broken.
        """
        if "data spike" not in data_spike:
            print("You do not have a data spike in your inventory")
        elif self.__damage_counter < self.__max_damage:
            self.__damage_counter += 1
            data_spike.remove("data spike")

        if self.__damage_counter == self.__max_damage:
            self.__broken = True
            print("Rig is now broken")


    def damage(self, data_spike):
        """Wrapper method for set_damage(self)."""
        return self.set_damage(data_spike)

    def set_random_asset(self):
        """Randomly generates an asset and adds it to the storage."""
        num = self.random.randint(0, 4)
        asset_list = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]
        asset_description = ["Used to acquire or repair rigs.", "Used in battles",
        "Found in rigs and used for extraction.", "Used to encrypt or decrypt assets.", "Used to upgrade rigs."]
        self.__storage.append(Assets(asset_list[num], asset_description[num]))


    def random_asset(self):
        """Wrapper method for set_random_asset(self)"""
        return set_asset()

    def set_transfer_asset(self, item):
        """Setter method to transfer an asset to rig instance."""
        self.__storage.append(item)

    def transfer_asset(self, item):
        """Wrapper method for set_transfer_asset(self)"""
        return self.set_transfer_asset(item)

    def set_transfer_all(self, target):
        """Transfers all of rig instance if they are unencrypted
        to storage to target"""
        transfer_list = []
        print("here 1")

        for x in self.__storage:
            print("here 2")
            print(x.get_encrypt_asset())
            if x.get_encrypt_asset() is False:
                #print(x.get_is_encrypted())
                transfer_list.append(x)

        if transfer_list == []:
            print("All contents were encrypted, unable to transfer")
            print(transfer_list)
        for x in transfer_list:
            print(target)
            target.transfer_asset(x)
            self.__storage.remove(x)


    def transfer_all(self, target):
        """Wrapper method for set_transfer_all(self)"""
        return self.set_transfer_all( target)

    def get_condition(self):
        """Displays the condition of the current rig and a description of condition"""
        if self.__damage_counter < self.__max_damage * 0.5:
            print(f"Pristine Rig (Level {self.__level})")
        elif self.__damage_counter >= self.__max_damage * 0.5 and self.__damage_counter < self.__max_damage * 1:
            print(f"Damaged  Rig (Level {self.__level})")
        else:
            print(f"Rig Broken ( Level {self.__level})")
















