from telethon import TelegramClient, sync
from telethon import functions, types

api_id = api_id
api_hash = 'api_hash'

client = TelegramClient('any_name', api_id, api_hash)
client.start()

# Информация о канале

# result = client(functions.channels.GetFullChannelRequest(channel='channel_name'))
# print(result.stringify())

# Информация о пользователе

# result = client(functions.users.GetFullUserRequest(id='user_name'))
# print(result.stringify())

# Получение своего id

# print(client.get_me().id)

#Работа с сообщениями

# for message in client.iter_messages('channel_name', limit=10):
#         print(message.id, message.views)