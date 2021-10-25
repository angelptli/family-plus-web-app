from django.contrib import admin
from user_connections.models import ConnectionsList, ConnectRequest


class ConnectionsListAdmin(admin.ModelAdmin):

    """Custom admin set up for the connections list model."""

    list_filter = ['user']
    list_display = ['user']
    search_fields = ['user']
    readonly_fields = ['user']

    class Meta:
        model = ConnectionsList


admin.site.register(ConnectionsList, ConnectionsListAdmin)


class ConnectRequestAdmin(admin.ModelAdmin):

    """Search fields searchable by the sender and receiver's email field
    and username field.
    """

    list_filter = ['sender', 'receiver']
    list_display = ['sender', 'receiver']
    search_fields = ['sender__email',
                     'sender__username',
                     'receiver__email',
                     'receiver__username']

    class Meta:
        model = ConnectRequest


admin.site.register(ConnectRequest, ConnectRequestAdmin)