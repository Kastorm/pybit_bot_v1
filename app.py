import bot_log
import json, os, config
from flask import Flask, request,render_template
from pybit.unified_trading import HTTP
import logging
import order

# LOGS
logging.basicConfig(filename="pybit.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)

@app.route("/")
def hello_trader():
    return render_template('index.html')

# Bybit Bot
@app.route("/bot", methods=['POST'])
def bybit_bot():
    data = json.loads(request.data)
    bot_log.logs("======= Webhook START =======",data)
    # Проверка секретного кода
    webhook_passphrase = os.environ.get('WEBHOOK_PASSPHRASE', config.WEBHOOK_PASSPHRASE)
    if 'passphrase' not in data.keys():
        bot_log.logs("======== No passphrase! ========",data)
        return {
            "success": False,
            "message": "No passphrase",
            "success1": bot_log.logs("======= Webhook STOP =======",data)
        }
    # Проверка passphrase  сверяем из фаила конфиг
    if data['passphrase'] != webhook_passphrase:
        bot_log.logs ("======== invalid passphrase! ========",data)
        return {
            "success": False,
            "message": "invalid passphrase",
            "success1": bot_log.logs("======= Webhook STOP =======",data)
        }
    del data["passphrase"]

    bot_log.logsgo(json.dumps(data,indent=4))
    #  API + subaccount
    if data['subaccount'] == 'Bot3m':
       session = HTTP(testnet=config.Testnet, api_key=config.Api_key_3m, api_secret=config.Api_secret_3m)
       order.get_position(data,session)
    if data['subaccount'] == 'Bot5m':
       session = HTTP(testnet=config.Testnet, api_key=config.Api_key_5m, api_secret=config.Api_secret_5m)
       order.get_position(data,session)
    if data['subaccount'] == 'Bot15m':
       session = HTTP(testnet=config.Testnet, api_key=config.Api_key_15m, api_secret=config.Api_secret_15m)
       order.get_position(data,session)
    if data['subaccount'] == 'Bot1H':
       session = HTTP(testnet=config.Testnet, api_key=config.Api_key_1H, api_secret=config.Api_secret_1H)
       order.get_position(data,session)


    return {
        "success": True,
        "message": "Data accepted",

    }


