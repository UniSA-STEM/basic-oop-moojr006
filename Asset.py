"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Jason Moore
ID: 110456746
Username: Moojr006
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Assets:

    def __init__(self,name, description):
        self.name = name
        self.description = description
        self.__encrypted = False

    def __str__(self):
        """Method to display key information about the asset instance."""
        if self.__encrypted is True:
            return f'{self.name}:{self.description}[Encrypted]'
        else:
            return f'{self.name}:{self.description}'

    def get_encrypt_asset(self):
        """Getter method to show encryption boolean"""
        return self.__encrypted

    def set_encrypt_asset(self):
        """Setter method to edit encryption boolean to True"""
        self.__encrypted = True

    def encryption(self):
        """Wrapper method to set_encrypt_asset"""
        return self.set_encryption

    def set_decryption(self):
        """Setter method to False"""
        self.__encrypted = False

    def decryption(self):
        """Wrapper method to set_decryption"""
        return self.set_decryption
