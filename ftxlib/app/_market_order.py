from ftxlib.utils._request import Request
from ftxlib.utils._response import get_response
from ftxlib.utils._orderbook import get_raw_orderbook,Orderbook
from ftxlib.utils._exceptions import NoMarketException
import numpy as np

def MarketOrder(request_json):
      action = request_json['action']
      base_currency = request_json['base_currency']
      quote_currency = request_json['quote_currency']
      amount = request_json['amount']
      
      #### Exceptions
      for x in ["action","base_currency","quote_currency"]:
            if not isinstance(x,str):
                  raise ValueError(f'{request_json[x]} type is invalid. {x} must be str type')
      x = 'amount'
      if not isinstance(amount,float):
            raise ValueError(f'{amount} type is invalid. Amount must be float type')
            
      if amount <= 0:
            raise ValueError(f'{amount} is invalid. Amount must be bigger than zero')
      
      if action not in ['buy','sell']:
            raise ValueError(f'{action} is invalid. Action must be buy or sell')
            
      
      #### Read raw orderbook
      raw_orderbook = get_raw_orderbook(base_currency = base_currency,
                                    quote_currency = quote_currency,
                                    depth = 50) 
      
      if not raw_orderbook['success']:
            raw_orderbook = get_raw_orderbook(base_currency = quote_currency,
                                                quote_currency = base_currency)

            if not raw_orderbook['success']: 
                  raise NoMarketException(f'There is no {base_currency}/{quote_currency} or {quote_currency}/{base_currency} market.')
            
            last_base_currency = quote_currency
            last_quote_currency = base_currency 

      else:
            last_base_currency = base_currency
            last_quote_currency = quote_currency 
            
      request = Request(action,
                        base_currency,
                        quote_currency,
                        amount
                        )
      
      orderbook = Orderbook(last_base_currency,
                  last_quote_currency,
                  raw_orderbook)
            
      return get_response(request,orderbook)