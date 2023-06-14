import config, os
from discord_webhook import DiscordWebhook, DiscordEmbed

DISCORD_ORDER_URL = os.environ.get('DISCORD_ORDER_URL', config.DISCORD_ORDER_URL)
DISCORD_LOGS_URL = os.environ.get('DISCORD_LOGS_URL', config.DISCORD_LOGS_URL)
DISCORD_ERR_URL = os.environ.get('DISCORD_ERR_URL', config.DISCORD_ERR_URL)


#Лог новых ордеров
def webhook_order(msg):
    if "LONG" in msg:
        webhook = DiscordWebhook(url=config.DISCORD_ORDER_URL)
        embed = DiscordEmbed(description=msg, color='2FFF46')
        webhook.add_embed(embed)
        response = webhook.execute()
    elif "SHORT"  in msg:
        webhook = DiscordWebhook(url=config.DISCORD_ORDER_URL)
        embed = DiscordEmbed(description=msg, color='FF0000')
        webhook.add_embed(embed)
        response = webhook.execute()
# Лог ордеров
def webhook(msg,data,account):
   webhook = DiscordWebhook(url=config.DISCORD_LOGS_URL)
   embed = DiscordEmbed(title=account, description=msg, color='FFFFFF')
   webhook.add_embed(embed)
   response = webhook.execute()


def webhook_log(msg):
    webhook = DiscordWebhook(url=config.DISCORD_LOGS_URL, content=msg)
    response = webhook.execute()


# Лог ошибок
def webhook_err(msg):
    webhook = DiscordWebhook(url=config.DISCORD_ERR_URL)
    embed = DiscordEmbed(description=msg, color='FF2700')
    webhook.add_embed(embed)
    response = webhook.execute()


# Вывод србытий + Discord
def logs(msg,data):
    account = data["subaccount"]
    webhook(msg,data, account)
    if "!" in msg:
        webhook_err(msg,account)

def logsgo(data):
    msg = data
    account = ''
    webhook(msg,data,account)

def logs_order(msg):
    webhook_log(msg)
    if "!" in msg:
        webhook_err(msg)
def logs_position(msg):
    msg = msg[1]
    webhook_order(msg)

