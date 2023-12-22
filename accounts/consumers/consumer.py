import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    """Use this consumer to subscribe to current user's notification"""

    async def connect(self):
        self.user = self.scope["user"]
        self.group_name = "subscribe_to_user_%s_notifications" % self.user.pk

        # Join room group
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name
        )

    commands = {}

    # Receive message from room group
    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.commands[data["command"]](self, data)

    async def send_action_update_message(self, message):
        await self.channel_layer.group_send(
            self.group_name,
            {"type": "send_notification_message", "message": message},
        )

    async def send_notification_message(self, event):
        await self.send(text_data=json.dumps(event["message"]))
