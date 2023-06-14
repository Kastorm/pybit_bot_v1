import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed


webhook_url = 'http://127.0.0.1:5000/webhook'
data = { 'name': 'Maikl', 'Chanel URL': 'Test'}
r = requests.post(webhook_url, data=json.dumps(data), headers = {'Content-Type': 'application/json'})


webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1114409526360277082/iJBMEQDJk-Wi8reYsXL00xo-D88XILTuFCSs6ym7sN4ov088jNInCG2SrQz4iUmvfATI', content='Проверка связи')
response = webhook.execute()
