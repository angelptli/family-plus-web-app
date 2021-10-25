from .models import ConnectRequest


def get_friend_request_or_false(sender, receiver):
    """True if a connection, otherwise false."""
    # Credit: https://youtu.be/r7v3YvNUgR8
    try:
        return ConnectRequest.object.get(send=sender, receiver=receiver,
                                         is_active=True)
    except ConnectRequest.DoesNotExist:
        return False