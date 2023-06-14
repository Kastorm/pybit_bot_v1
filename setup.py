from pybit.unified_trading import HTTP
import config


session = HTTP(testnet=config.Testnet, api_key=config.Api_key, api_secret=config.Api_secret)


# Установка кредитного плеча
def setup():
    # Проверяем какое плечо
    positions = session.get_positions(
        category=config.category,
        symbol="BTCUSDT",
    )

    retMsg = positions['result']
    leverage = retMsg['list'][0]['leverage']
    print("Существующее плечо - "  +leverage)
    # Если плечо в системе отличаеться  от конфига  устанавливаем как в конфиге
    if leverage != config.buyLeverage :
          res = session.set_leverage(
                                  category=config.category,
                                  symbol="BTCUSDT",
                                  buyLeverage=config.buyLeverage,
                                  sellLeverage=config.sellLeverage,
                                  )
          return print( "Новое плечо - " + config.buyLeverage)


setup()