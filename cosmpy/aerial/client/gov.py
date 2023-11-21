from cosmpy.crypto.address import Address
from cosmpy.protos.cosmos.gov.v1beta1.gov_pb2 import VoteOption
from cosmpy.protos.cosmos.gov.v1beta1.tx_pb2 import MsgVote


def create_vote_proposal(
        proposal_id: int,
        voter: Address,
        option: VoteOption
):
    return MsgVote(
        proposal_id=proposal_id,
        voter=str(voter),
        option=option
    )
