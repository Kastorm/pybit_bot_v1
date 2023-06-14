import bot_log
import logging
import config

# Показывает открытые Ордера.
# response = session.get_open_orders(
#                                     category="linear",
#                                     symbol="BTCUSDT",
#                                   )
# orders = response["result"]["list"]
# print(orders)

# Создает ордер  с TP и SL
# print(session.place_order(
#     category="linear",
#     symbol="BNBUSDT",
#     side="Buy",
#     order_type="Market",
#     qty="10",
#     takeProfit="300",
#     stopLoss="250",
#     tpTriggerBy="MarkPrice",
#     slTriggerBy="MarkPrice",
#     tpslMode = "Partial",
#     tpSize="50",
#     slSize="50",
#     isLeverage=1
# ))

# Поиск в истории по orderId
def get_order(id,data,session):
    #Запрашиваем открытые позиции если есть отправляем цену и количество
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

    # Если нет открытой позиции смотрим по ID в истории и отправляем цену открытия и закрытия + прибыль
    if size == '0' :
        orderId = id
        get= session.get_executions(
                                    category="linear",
                                    orderId=orderId
                                    #symbol = data['symbol'],
                                    #startTime= "1",
                                    #endTime= "100"
                                   )
        # closedSize
        # avgEntryPrice
        # avgExitPrice
        # closedPnl
        retMsg = get['result']
        symbol = retMsg['list'][0]['symbol']
        size = retMsg['list'][0]['execQty']
        price = retMsg['list'][0]['execPrice']
        msg  = symbol + "\n" + price + "\n" + size + "\n" + data['desc'] + "\n" + data['subaccount']
        bot_log.logs_order(msg)
        data = msg
    return [id,data]


# Long по  Маркет
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

# # SHORT   по  Маркет
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

