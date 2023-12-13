from typing import Optional

from cosmpy.crypto.address import Address
from cosmpy.protos.cosmos.base.v1beta1.coin_pb2 import Coin
from cosmpy.protos.ibc.applications.transfer.v1.tx_pb2 import MsgTransfer
from cosmpy.protos.ibc.core.client.v1.client_pb2 import Height


def create_ibc_transfer_msg(
        sender: Address,
        receiver: Address,
        source_port: str,
        source_channel: str,
        amount: int,
        denom: str,
        timeout_height: Optional[Height] = None,
        timeout_timestamp: Optional[int] = None
) -> MsgTransfer:
    msg = MsgTransfer(
        sender=str(sender),
        receiver=str(receiver),
        token=Coin(amount=str(amount), denom=denom),
        timeout_height=timeout_height,
        timeout_timestamp=timeout_timestamp,
        source_port=source_port,
        source_channel=source_channel
    )

    return msg
