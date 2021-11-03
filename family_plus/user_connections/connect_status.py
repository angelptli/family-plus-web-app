from enum import Enum


class ConnectRequestStatus(Enum):
    """Three states for connect status."""
    NO_REQUEST_SENT = -1
    THEM_SENT_TO_YOU = 0
    YOU_SENT_TO_THEM = 1