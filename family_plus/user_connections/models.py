from django.db import models
from django.conf import settings
from django.utils import timezone


class ConnectionsList(models.Model):

    """A user connections model that allows users to add other users into
    their list of connections.
    """

    # Model designed by CodingWithMitch
    # Link to tutorial: https://www.youtube.com/watch?v=hyJO4mkdwuM
    # Establish mutual connections between users, which will be a basis
    # for setting different permissions for connections and non-connections..

    # Each user has one list connections
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    connections = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="connections")

    def __str__(self):
        """Display the user's username."""
        return self.user.username

    def add_connection(self, other_user):
        """Add a connection to the connections list.
        
        Enables user to add the other user into their connections list
        if not already in their connections list.
        """
        if not other_user in self.connections.all():
            self.connections.add(other_user)
            self.save()

    def remove_connection(self, other_user):
        """Remove a connection from the connections list.
        
        Enables user to remove the other user from their connections list if
        the other user is a current connection of the user.
        """
        if other_user in self.connections.all():
            self.connections.remove(other_user)

    def disconnect(self, removee):
        """Initiate the action of disconnecting with another user."""
        # User removing the removee
        receiver_connection_list = self

        # Remove the removee from the remover's connection list
        receiver_connection_list.remove_connection(removee)

        # Remove the remover from the removee's connection list
        connection_list = ConnectionsList.objects.get(user=removee)
        connection_list.remove_connection(self.user)

    def is_mutual_connection(self, connection):
        """Checks if the connection is mutual and both users are
        in each other's connection list.
        """
        if connection in self.connections.all():
            return True
        return False


class ConnectRequest(models.Model):

    """A connect request involving a sender and receiver."""

    # Model designed by CodingWithMitch
    # Link to tutorial: https://www.youtube.com/watch?v=hyJO4mkdwuM
    # Establish mutual connections between users, which will be a basis
    # for setting different permissions for connections and non-connections.

    # User sending the connect request
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="sender")

    # User receiving the connect request
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name="receiver")

    # True for a pending request. False for a declined/cancelled request.
    is_active = models.BooleanField(blank=False, null=False, default=True)

    # Logs timestamp of the connect request
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Display the sender's username to the receiver."""
        return self.sender.username

    def accept(self):
        """Accept a connect request and update both sender and receiver
        connection lists.
        """
        receiver_connection_list = ConnectionsList.objects.get(user=self.receiver)

        if receiver_connection_list:
            receiver_connection_list.add_connection(self.sender)
            sender_connection_list = ConnectionsList.objects.get(user=self.sender)

            if sender_connection_list:
                sender_connection_list.add_connections(self.receiver)
                self.is_active = False
                self.save()

    def decline(self):
        """Decline a connect request by setting is_active to False for a
        declined connect request.
        """
        self.is_active = False
        self.save()

    def cancel(self):
        """Cancel a connect request by setting setting is_active to False
        when a user cancels their connect request.
        """
        self.is_active = False
        self.save()