from channels.generic.websocket import AsyncWebsocketConsumer 
import json

class PlayerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = 'stream_%s' % self.room_name

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
                )
            await self.accept()

    async def disconnect(self, close_code):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        url = text_data_json['url']
        duration = text_data_json['duration']
        played = text_data_json['played']
        queue = text_data_json['queue']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
            'type': 'web_stream',
            'url': url,
            'played': played,
            'duration' : duration,
            'queue' : queue
            }
        )

    async def web_stream(self, event):
        url = event['url']
        played = event['played']
        duration = event['duration']
        queue = event['queue']
        await self.send(text_data=json.dumps({
            'url': url,
            'played': played,
            'duration': duration,
            'queue' : queue
        }))
