import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import Chatroom
from d09.settings import SAVE_N_MESSAGES


@database_sync_to_async
def change_user_status(chatroom, user):
    if user in chatroom.connected_users.all():
        chatroom.connected_users.remove(user)
    else:
        chatroom.connected_users.add(user)


@database_sync_to_async
def get_connected_users(chatroom):
    return list(chatroom.connected_users.values_list('username', flat=True))


@database_sync_to_async
def room_exists(room_name):
    try:
        chatroom = Chatroom.objects.get(id=room_name)
        messages = chatroom.messages.all().order_by('-created_at')[:SAVE_N_MESSAGES]
        return chatroom, [{'username': m.username, 'message': m.message} for m in messages]
    except Chatroom.DoesNotExist:
        return None, None


@database_sync_to_async
def save_message(chatroom, username, message):
    try:
        chatroom.messages.create(username=username, message=message)
        last_messages = chatroom.messages.order_by('-created_at').values_list('id', flat=True)[:SAVE_N_MESSAGES]
        chatroom.messages.exclude(id__in=last_messages).delete()
    except Exception as e:
        print(e)


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None
        self.room_name = None
        self.chatroom = None
        self.room_group_name = None

    async def connect(self, test=None):
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.chatroom, history = await room_exists(self.room_name)
        if not self.chatroom:
            await self.close()

        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        connected_users = await get_connected_users(self.chatroom)

        await self.send(text_data=json.dumps({
            'type': 'connection_success',
            'messages': history,
            'connected_users': connected_users
        }))

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'room_name': self.room_name,
                'type': 'chat_message',
                'send_type': 'user_joined',
                'username': self.user.username,
                'message': f'{self.user.username} has joined the chat'
            }
        )
        await change_user_status(self.chatroom, self.user)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'room_name': self.room_name,
                'type': 'chat_message',
                'send_type': 'user_left',
                'username': self.user.username,
                'message': f'{self.user.username} has left the chat'
            }
        )
        await change_user_status(self.chatroom, self.user)

    async def receive(self, text_data):
        data = json.loads(text_data)

        await save_message(self.chatroom, data['username'], data['message'])

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'send_type': 'message',
                'username': data['username'],
                'message': data['message']
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': event['send_type'],
            'message': event['message'],
            'username': event['username'],
        }))
