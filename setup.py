from pybit.unified_trading import HTTP
import config


session = HTTP(testnet=config.Testnet, api_key=config.Api_key_3m, api_secret=config.Api_secret_3m)


# leverage
def setup():
    positions = session.get_positions(
        category=config.category,
        symbol="BTCUSDT",
    )
    retMsg = positions['result']
    leverage = retMsg['list'][0]['leverage']
    print("leverage- "  +leverage)
    if leverage != config.buyLeverage :
          res = session.set_leverage(
                                  category=config.category,
                                  symbol="BTCUSDT",
                                  buyLeverage=config.buyLeverage,
                                  sellLeverage=config.sellLeverage,
                                  )
          return print( "New leverage - " + config.buyLeverage)

setup()