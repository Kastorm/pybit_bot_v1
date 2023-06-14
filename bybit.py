import bot_log
import config

# Search by history
def get_order(id,data,session):
    positions = session.get_positions(
                                      category=config.category,
                                      symbol=data['symbol']
                                     )

    retMsg = positions['result']
    symbol = retMsg['list'][0]['symbol']
    size = retMsg['list'][0]['size']
    if size > '0' :
        price = retMsg['list'][0]['avgPrice']
        msg = symbol + "\n" + price + "\n" + size + "\n" + data['desc'] + "\n" + data['subaccount']
        bot_log.logs_order(msg)
        data = msg
    if size == '0' :
        orderId = id
        get= session.get_executions(
                                    category="linear",
                                    orderId=orderId
                                   )
        retMsg = get['result']
        symbol = retMsg['list'][0]['symbol']
        size = retMsg['list'][0]['execQty']
        price = retMsg['list'][0]['execPrice']
        msg  = symbol + "\n" + price + "\n" + size + "\n" + data['desc'] + "\n" + data['subaccount']
        bot_log.logs_order(msg)
        data = msg
    return [id,data]


# Long Market
def long_order(data,qtyHok,session):
    global msg
    res = session.place_order(category=config.category,
                              symbol=data['symbol'],
                              side="Buy",
                              order_type="Market",
                              qty=qtyHok,
                              isLeverage=1
                              )

    res = res['result']
    id = res['orderId']
    msg = get_order(id,data,session)
    bot_log.logs_position(msg)

# # SHORT   Market
def short_order(data,qtyHok,session):
    global msg
    res = session.place_order(category=config.category,
                              symbol=data['symbol'],
                              side="Sell",
                              order_type="Market",
                              qty=qtyHok,
                              isLeverage=1
                              )
    res = res['result']
    id = res['orderId']
    msg = get_order(id, data,session)
    bot_log.logs_position(msg)

