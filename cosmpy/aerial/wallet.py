# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2021 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Wallet Generation."""

from abc import ABC, abstractmethod
from collections import UserString
from typing import Optional, Union

from cosmpy.aerial.config import NetworkConfig
from cosmpy.crypto.address import Address
from cosmpy.crypto.hashfuncs import sha256
from cosmpy.crypto.interface import Signer
from cosmpy.crypto.keypairs import PrivateKey, PublicKey
from cosmpy.mnemonic import COSMOS_HD_PATH, derive_child_key_from_mnemonic


class Wallet(ABC, UserString):
    """Wallet Generation.

    :param ABC: ABC abstract method
    :param UserString: user string
    """

    @abstractmethod
    def address(self) -> Address:
        """get the address of the wallet.

        :return: None
        """

    @abstractmethod
    def public_key(self) -> PublicKey:
        """get the public key of the wallet.

        :return: None
        """

    @abstractmethod
    def signer(self) -> Signer:
        """get the signer of the wallet.

        :return: None
        """

    @property
    def data(self):
        """Get the address of the wallet.

        :return: Address
        """
        return self.address()

    def __json__(self):
        """
        Return the address in string format.

        :return: address in string format
        """
        return str(self.address())


class DefaultWallet(Wallet):
    @staticmethod
    def generate(
            public_key: bytes,
            private_key: bytes,
            address: Union[bytes, str],
            network_cfg: NetworkConfig,
            prefix: Optional[str] = None
    ) -> "DefaultWallet":
        return DefaultWallet(
            address=address,
            public_key=public_key,
            private_key=private_key,
            prefix=prefix,
            network_cfg=network_cfg
        )

    def __init__(
            self,
            private_key: bytes,
            address: Union[bytes, str],
            public_key: bytes,
            network_cfg: NetworkConfig,
            prefix: Optional[str] = None
    ):
        self._address = address
        self._private_key = private_key
        self._public_key = public_key
        self._prefix = prefix
        self._network_cfg = network_cfg

    def address(self) -> Address:
        """Get the wallet address.

        :return: Wallet address.
        """
        return Address(self._address, self._prefix)

    def public_key(self) -> PublicKey:
        """Get the public key of the wallet.

        :return: public key
        """
        return PublicKey(self._public_key, self._network_cfg)

    def signer(self) -> PrivateKey:
        """Get  the signer of the wallet.

        :return: signer
        """
        return PrivateKey(self._private_key, self._network_cfg)


class LocalWallet(Wallet):
    """Generate local wallet.

    :param Wallet: wallet
    """

    @staticmethod
    def generate(network_cfg: NetworkConfig, prefix: Optional[str] = None) -> "LocalWallet":
        """generate the local wallet.

        :param prefix: prefix, defaults to None
        :return: local wallet
        """
        return LocalWallet(PrivateKey(), prefix=prefix, network_cfg=network_cfg)

    @staticmethod
    def from_mnemonic(network_cfg: NetworkConfig, mnemonic: str, prefix: Optional[str] = None) -> "LocalWallet":
        """Generate local wallet from mnemonic.

        :param mnemonic: mnemonic
        :param prefix: prefix, defaults to None
        :return: local wallet
        """
        child_key = derive_child_key_from_mnemonic(mnemonic, path=COSMOS_HD_PATH)

        return LocalWallet(PrivateKey(child_key), prefix=prefix, network_cfg=network_cfg)

    @staticmethod
    def from_unsafe_seed(
        network_cfg: NetworkConfig, text: str, index: Optional[int] = None, prefix: Optional[str] = None
    ) -> "LocalWallet":
        """Generate local wallet from unsafe seed.

        :param text: text
        :param index: index, defaults to None
        :param prefix: prefix, defaults to None
        :return: Local wallet
        """
        private_key_bytes = sha256(text.encode())
        if index is not None:
            private_key_bytes = sha256(
                private_key_bytes + index.to_bytes(4, byteorder="big")
            )
        return LocalWallet(PrivateKey(private_key_bytes), prefix=prefix, network_cfg=network_cfg)

    def __init__(self, private_key: PrivateKey, network_cfg: NetworkConfig, prefix: Optional[str] = None):
        """Init wallet with.

        :param private_key: private key of the wallet
        :param prefix: prefix, defaults to None
        """
        self._private_key = private_key
        self._public_key = private_key.public_key
        self._prefix = prefix
        self._network_cfg = network_cfg

    def address(self) -> Address:
        """Get the wallet address.

        :return: Wallet address.
        """
        return Address(self._public_key, self._prefix)

    def public_key(self) -> PublicKey:
        """Get the public key of the wallet.

        :return: public key
        """
        return PublicKey(self._public_key, self._network_cfg)

    def signer(self) -> PrivateKey:
        """Get  the signer of the wallet.

        :return: signer
        """
        return PrivateKey(self._private_key, self._network_cfg)
