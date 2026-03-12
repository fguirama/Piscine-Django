import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import Chatroom


@database_sync_to_async
def room_exists(room_name):
    return Chatroom.objects.filter(id=room_name).exists()


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None

    async def connect(self, test=None):
        print('CONNECT', test, flush=True)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        if not await room_exists(self.room_name):
            await self.close()
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'connect',
        #         'room_name': self.room_name
        #     }
        # )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'disconnect',
                'close_code': close_code
            }
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data, flush=True)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': data['username'],
                'message': data['message']
            }
        )

    async def chat_message(self, event):
        print('CHAT MESSAGE', flush=True)
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username']
        }))
