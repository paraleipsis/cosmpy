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

"""Network configurations."""
import hashlib
import warnings
import sha3
import ecdsa
from dataclasses import dataclass, field
from typing import Optional, Union, Callable

from cosmpy.aerial.tx import _create_inj_proto_public_key, _create_proto_public_key, _create_eth_proto_public_key
from cosmpy.protos.cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from cosmpy.protos.injective.types.v1beta1.account_pb2 import EthAccount as InjAccount
from cosmpy.protos.ethermint.types.v1.account_pb2 import EthAccount


class NetworkConfigError(RuntimeError):
    """Network config error.

    :param RuntimeError: Runtime error
    """

    pass


URL_PREFIXES = (
    "grpc+https",
    "grpc+http",
    "rest+https",
    "rest+http",
)


@dataclass
class NetworkType:
    account: Callable = field(default_factory=BaseAccount())
    curve: Callable = ecdsa.SECP256k1
    hash_function: Callable = hashlib.sha256
    public_key_generator: Callable = _create_proto_public_key


CosmosNetworkType = NetworkType(
    hash_function=hashlib.sha256,
    curve=ecdsa.SECP256k1,
    account=BaseAccount(),
    public_key_generator=_create_proto_public_key
)

EvmosNetworkType = NetworkType(
    hash_function=sha3.keccak_256,
    curve=ecdsa.SECP256k1,
    account=EthAccount(),
    public_key_generator=_create_eth_proto_public_key
)

InjectiveNetworkType = NetworkType(
    hash_function=sha3.keccak_256,
    curve=ecdsa.SECP256k1,
    account=InjAccount(),
    public_key_generator=_create_inj_proto_public_key
)


@dataclass
class NetworkConfig:
    """Network configurations.

    :raises NetworkConfigError: Network config error
    :raises RuntimeError: Runtime error
    """

    chain_id: str
    fee_minimum_gas_price: Union[int, float]
    fee_denomination: str
    staking_denomination: str
    url: str
    network_type: NetworkType
    faucet_url: Optional[str] = None

    def validate(self):
        """Validate the network configuration.

        :raises NetworkConfigError: Network config error
        """
        if self.chain_id == "":
            raise NetworkConfigError("Chain id must be set")
        if self.url == "":
            raise NetworkConfigError("URL must be set")
        if not any(
            map(
                lambda x: self.url.startswith(  # noqa: # pylint: disable=unnecessary-lambda
                    x
                ),
                URL_PREFIXES,
            )
        ):
            prefix_list = ", ".join(map(lambda x: f'"{x}"', URL_PREFIXES))
            raise NetworkConfigError(
                f"URL must start with one of the following prefixes: {prefix_list}"
            )

    @classmethod
    def fetchai_dorado_testnet(cls) -> "NetworkConfig":
        """Fetchai dorado testnet.

        :return: Network configuration
        """
        return NetworkConfig(
            chain_id="dorado-1",
            url="grpc+https://grpc-dorado.fetch.ai",
            fee_minimum_gas_price=5000000000,
            fee_denomination="atestfet",
            staking_denomination="atestfet",
            faucet_url="https://faucet-dorado.fetch.ai",
        )

    @classmethod
    def fetchai_alpha_testnet(cls):
        """Get the fetchai alpha testnet.

        :raises RuntimeError: No alpha testnet available
        """
        raise RuntimeError("No alpha testnet available")

    @classmethod
    def fetchai_beta_testnet(cls):
        """Get the Fetchai beta testnet.

        :raises RuntimeError: No beta testnet available
        """
        raise RuntimeError("No beta testnet available")

    @classmethod
    def fetchai_stable_testnet(cls):
        """Get the fetchai stable testnet.

        :return: fetchai stable testnet. For now dorado is fetchai stable testnet.
        """
        return cls.fetchai_dorado_testnet()

    @classmethod
    def fetchai_mainnet(cls) -> "NetworkConfig":
        """Get the fetchai mainnet configuration.

        :return: fetch mainnet configuration
        """
        return NetworkConfig(
            chain_id="fetchhub-4",
            url="grpc+https://grpc-fetchhub.fetch.ai",
            fee_minimum_gas_price=0,
            fee_denomination="afet",
            staking_denomination="afet",
            faucet_url=None,
        )

    @classmethod
    def fetch_mainnet(cls) -> "NetworkConfig":
        """Get the fetch mainnet.

        :return: fetch mainnet configurations
        """
        warnings.warn(
            "fetch_mainnet is deprecated, use fetchai_mainnet instead",
            DeprecationWarning,
        )
        return cls.fetchai_mainnet()

    @classmethod
    def latest_stable_testnet(cls) -> "NetworkConfig":
        """Get the latest stable testnet.

        :return: latest stable testnet
        """
        warnings.warn(
            "latest_stable_testnet is deprecated, use fetchai_stable_testnet instead",
            DeprecationWarning,
        )
        return cls.fetchai_stable_testnet()
