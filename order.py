import bot_log
import config
import bybit

def get_position(data,session):
     global descHok
     global risk
     global symbolHok
     global qtyHok
     global size

     positions = session.get_positions(category=config.category, symbol=data['symbol'])
     retMsg = positions['result']
     symbol = retMsg['list'][0]['symbol']
     side = retMsg['list'][0]['side']
     size = retMsg['list'][0]['size']
     sideHok = data['side']
     descHok = data['desc']
     symbolHok = data['symbol']
     qtyHok = data['qty']


     if positions["retMsg"] == 'OK':

         if size > '0' :
                 if side == 'Buy':
                     print('There is LONG ', symbol, size)
                     if sideHok == 'Sell':
                         if descHok == 'Close_LONG':
                             bot_log.logs_order("======= Close LONG =======")
                             bybit.short_order(data,qtyHok,session)
                         elif descHok == 'Open_SHORT':
                             qtyHok = float(qtyHok)
                             qtyHok = qtyHok * 2
                             bot_log.logs_order("======= Open SHORT and Close LONG =======")
                             bybit.short_order(data,qtyHok,session)
                         else:  bot_log.logs("======= error! error! =======")
                     elif data['side'] == 'Buy':
                         if descHok == 'Open_LONG':
                             bot_log.logs_order("========== error! There is  LONG !  ==========")
                         elif descHok == 'Close_SHORT':
                             bot_log.logs_order("========== error! No SHORT!  ==========")
                         else:
                             bot_log.logs_order("======= error! error! =======")
                 elif side == 'Sell':
                     print('There is SHORT ', symbol, size)
                     if sideHok == 'Buy':
                         if descHok == 'Close_SHORT':
                             bot_log.logs_order("========== Close SHORT ==========")
                             bybit.long_order(data,qtyHok,session)
                         elif descHok == 'Open_LONG':
                             qtyHok = float(qtyHok)
                             qtyHok = qtyHok * 2
                             bot_log.logs_order("========== Close SHORT and Open LONG ==========")
                             bybit.long_order(data,qtyHok,session)
                     elif data['side'] == 'Sell':
                         if descHok == 'Open_SHORT':
                             bot_log.logs_order("========== error! There is  SHORT !   ==========")
                         elif descHok == 'Close_LONG':
                             bot_log.logs_order("========== error! No LONG!   ==========")
         else:
             if data['side'] == 'Buy':
                 if descHok == 'Open_LONG':
                     bot_log.logs_order("========== Open LONG  ==========")
                     bybit.long_order(data, qtyHok,session)
                 elif descHok == 'Close_SHORT':
                     bot_log.logs_order("========== error! No SHORT!  ==========")
             elif data['side'] == 'Sell':
                 if descHok == 'Open_SHORT':
                     bot_log.logs_order("========== Open SHORT  ==========")
                     bybit.short_order(data, qtyHok,session)
                 elif descHok == 'Close_LONG':
                     bot_log.logs_order("========== error! No LONG!  ==========")



     return {
             "success": True,
             "message": "Data accepted",

             "success1": bot_log.logs("======= Webhook accepted =======",data)
             }

