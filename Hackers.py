"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Jason Moore
ID: 110456746
Username: Moojr006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Assets
from Rigs import Rig
class Hacker:

    def __init__(self, name):
        self.name = name
        self.__storage = [Assets("CryptoToken", "Used to acquire or repair rigs.")]
        self.__rig = None
        self.__trace_level = 0
        self.__max_trace_level = 5
        self.__exposed = False




    def set_rig_acquisition(self, rig_name):
        """Generates and assigns a rig to the hacker provided in the positional argument.
        When a new rig is generated, one "CryptoToken" asset within storage is removed."""
        self.__rig = Rig(rig_name)
        print(f"Rig {self.__rig.name} acquired.")
        for Assets in self.__storage:
            if Assets.name == "CryptoToken":
                self.__storage.remove(Assets)
                break


    def rig_acquisition(self, rig_name):
        """Wrapper method for set_rig_acquisition"""
        return self.set_rig_acquisition(rig_name)

    def get_rig(self):
        """ Returns __str__ rig details."""
        return(self.__rig)

    def set_no_rig(self):
        """Removes the hacker's rig"""
        self.__rig = None
        return self.__rig


    def no_rig(self):
        """Wrapper method for set_no_rig."""
        return self.set_no_rig()

    def get_rig_contents(self):
        """Getter method for returning the objects of the hacker's rig."""
        return self.__rig.get_storage()

    def set_transfer_asset(self, item):
        """Setter method to ddd an asset to storage from another hacker instance."""
        self.__storage.append(item)

    def transfer_asset(self, item):
        """Wrapper method to set_transfer_asset.
        """
        return self.set_transfer_asset(item)

    def set_launch_data_spike(self, data_spike, target):
        """Setter method to utilise a hackers Data Spike to damage an opponent.
        Each use of this method will increment the hackers trace level,
        even if they do not have a Data Spike and displays if they have passed the exposure threshold.
        If the targets rig has been broken, it will notify the hacker and give them an option to take
        their items.
        """
        target.get_rig().damage(data_spike.get_rig().get_storage())
        if self.__trace_level < self.__max_trace_level:
            self.__trace_level += 1
        if self.__trace_level == self.__max_trace_level:
            self.__exposed is True
            print(f"{self.name} is now exposed")

        #print(target.get_broken_status)

        if target.get_rig().get_broken_status() is True:
            choice = input("Do you want to take enemy rigs unencrypted assets? Y/N").upper()
            while choice != "Y" and choice != "N":
                choice = input("Enter a valid choice, either: Y or N ").upper()
            if choice == "Y":
                target.set_transfer_all(self)


    def launch_data_spike(self, data_spike, target):
        """Wrapper method for set_launch_data_spike."""
        return self.set_launch_data_spike(data_spike, target)

    def get_asset(self, num):
        """Getter method to display particular item within the list."""
        return self.__storage[num]

    def get_all_assets(self):
        """Getter method to display all item names in a user friendly format."""
        return [asset.name for asset in self.__storage]

    def get_list(self):
        """Getter method to display all item names in a user friendly format."""
        return [asset for asset in self.__storage]

    def set_asset_encryption(self, asset, item):
        """Setter method to encrypt an asset.
        Consumes security chip within storage.
        """
        asset.set_encrypt_asset()
        self.__storage.remove(item)


    def asset_encryption(self, asset, item):
        """Wrapper method for set_asset_encryption."""
        return self.set_asset_encryption(asset, item)

    def set_asset_decryption(self, asset, item):
        """Setter method to encrypt an asset.
        Consumes security chip within storage.
        """
        asset.set_decryption()
        self.__storage.remove(item)


    def asset_decryption(self, asset, item):
        """Wrapper mathod for set_asset_decryption."""
        return self.set_asset_decryption(asset, item)

    def set_rig_upgrade(self, rig, item):
        """Setter method to upgrade hacker's rig if they have a hardware patch."""
        if self.__rig is not None and item.name.lower() == "hardware patch":
            rig.upgrade()

        self.__storage.remove(item)

    def rig_upgrade(self, rig, item):
        """Wrapper method for set_rig_upgrade."""
        return self.set_rig_upgrade(rig, item)

    def set_transfer_all(self, target):
        """Transfers all of hacker storage to target if they are not encrypted."""
        transfer_list = []
        # print("Storage count:", len(self.__storage))
        for x in self.__storage:
            print(x.get_encrypt_asset())
            if x.get_encrypt_asset() is False:
                print(x.get_encrypt_asset())
                transfer_list.append(x)
        # print(transfer_list)
        if transfer_list == []:
            print("All contents were encrypted, unable to transfer")
            print(transfer_list)
        for x in transfer_list:
            target.transfer_asset(x)
            self.__storage.remove(x)


    def transfer_all(self, target):
        """Wrapper method for set_transfer_all."""
        self.set_transfer_all(target)



    def set_transfer_asset(self, item):
        """Setter method to transfer an asset to hacker instance."""
        self.__storage.append(item) # Wait for Hacker class to be created
        #self.__storage.remove(item)


    def transfer_asset(self, item):
        """Wrapper method for set_transfer_all."""# to hacker inventory
        return self.set_transfer_asset(item)

    def set_retrieve_all_from_rig(self):
        """Setter method to place all items stored in hacker's rig to hacker's storage."""
        self.__rig.transfer_all(self)

    def retrieve_all_from_rig(self):
        """Wrapper method for set_retrieve_all_from_rig."""
        return self.set_retrieve_all_from_rig()

    def set_asset(self):
        """Setter method to allow the hacker to generate one of the 5 usable assets within the program"""
        asset_list = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]
        asset_description = ["Used to acquire or repair rigs.", "Used in battles",
                             "Found in rigs and used for extraction.", "Used to encrypt or decrypt assets.",
                             "Used to upgrade rigs."]

        choice = input("Would you like to generate a CryptoToken, Data Spike, Removable Drive, Security Chip or Hardware Patch?").title()
        while choice not in asset_list:
            choice = input("Would you like to generate a CryptoToken, Data Spike, Removable Drive, Security Chip or Hardware Patch?").title()
        if choice == "CryptoToken":
            num = 0
            self.__storage.append(Assets(asset_list[num], asset_description[num]))
        elif choice == "Data Spike":
            num = 1
            self.__storage.append(Assets(asset_list[num], asset_description[num]))
        elif choice == "Removable Drive":
            num = 2
            self.__storage.append(Assets(asset_list[num], asset_description[num]))
        elif choice == "Security Chip":
            num = 3
            self.__storage.append(Assets(asset_list[num], asset_description[num]))
        elif choice == "Hardware Patch":
            num = 4
            self.__storage.append(Assets(asset_list[num], asset_description[num]))

    def __str__(self):
        """Method to display key information about hacker's instance."""
        rig_name = self.__rig.name if self.__rig is not None else "No rig assigned"
        return f"""Name:{self.name}
Rig name:{rig_name}
Trace level:{self.__trace_level}
Storage:{self.__storage}"""




