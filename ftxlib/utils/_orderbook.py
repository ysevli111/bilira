
import requests
import pandas as pd
from ftxlib.utils._price_type import Price_type 

def get_raw_orderbook(base_currency,
            quote_currency,
            depth = 10):
    """[summary]

    Args:
        base_currency ([type]): [description]
        quote_currency ([type]): [description]
        depth (int, optional): [description]. Defaults to 10.

    Returns:
        [type]: [description]
    """
    market_name = base_currency + '/' + quote_currency
    ordebook_url = f"https://ftx.com/api/markets/{market_name}/orderbook?depth={depth}"
    orderbook = requests.get(ordebook_url).json()
    return orderbook


    

    
class  Orderbook:
    def __init__(self,
                 base_currency,
                 quote_currency,
                 raw_orderbook):
        self.base_currency = base_currency
        self.quote_currency = quote_currency
        self.prices= self.convert_json_data_to_prices(raw_orderbook)
        
    def get_base_currency(self):
        return self.base_currency 
    
    def get_quote_currency(self):
        return self.quote_currency 
    
    def get_bids_prices(self):
        return self.prices[Price_type.bids.value]
    
    def get_asks_prices(self):
        return self.prices[Price_type.asks.value]
    
    def convert_json_data_to_prices(self,json_data):
        price_dict = {}
        for x in Price_type:
            if x.value == Price_type.asks.value:
                price_dict[x.value] = pd.DataFrame(json_data['result'][x.value],columns = ['price','size'])
            elif x.value == Price_type.bids.value:
                price_dict[x.value] = pd.DataFrame(json_data['result'][x.value],columns = ['price','size']).sort_values(['price']).reset_index(drop = True)
            else:
                raise ValueError(f'{x} is invalid price type')
        return price_dict
    
    def reverse_orderbook(self):
        reverse_price_dict = {}
        reverse_price_dict[Price_type.asks.value] = self.reverse_transformation(self.get_bids_prices())
        reverse_price_dict[Price_type.bids.value] = self.reverse_transformation(self.get_asks_prices())
        self.prices = reverse_price_dict
        
    def reverse_transformation(self,price_type_df):
        reverse_price_type_df = pd.DataFrame()
        reverse_price_type_df['price'] = 1/price_type_df['price']
        reverse_price_type_df['size'] = price_type_df['price']*price_type_df['size']
        return reverse_price_type_df
        


        