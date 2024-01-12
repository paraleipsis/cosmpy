from cosmpy.crypto.address import Address
from cosmpy.protos.cosmos.slashing.v1beta1.tx_pb2 import MsgUnjail


def create_unjail_msg(
    validator_address: Address
) -> MsgUnjail:
    return MsgUnjail(
        validator_addr=str(validator_address),
    )
