import numpy as np
from ftxlib.utils._action import Action    

class Response:
    def __init__(self):
        self.price_list = []
        self.size_list = []
               
    def add_price(self,price):
        self.price_list.append(price)
        
    def add_size(self,size):
            self.size_list.append(size)
        
    def get_total(self):
        return sum(np.multiply(self.price_list,self.size_list))
    
    def get_size(self):
        return sum(self.size_list)
        
    def get_price(self):
        return self.get_total() / self.get_size()
    
    
def get_response(request,orderbook):
    if request.get_base_currency() == orderbook.get_base_currency() and request.get_quote_currency() == orderbook.get_quote_currency():  
        return calculate_response(request,orderbook)
    else:
        orderbook.reverse_orderbook()
        return calculate_response(request,orderbook)


 
def calculate_response(request,orderbook):        
    orders = get_orders(request,orderbook)
    response = Response()
    print()
    for i in orders.index.tolist():
        
        cum_size = response.get_size() + orders.loc[i,'size']
        diff_size = cum_size - request.get_amount()
        
        if diff_size > 0:
            left_size = request.get_amount() - response.get_size()
            response.add_size(left_size)
            response.add_price(orders.loc[i,'price'])
  
            break
        else:
            response.add_size(orders.loc[i,'size'])
            response.add_price(orders.loc[i,'price'])

        
    
    response_json =   {'total' : str(response.get_total()),
                       'price' : str(response.get_price()),
                       'currency' : str(request.get_quote_currency())}    
    return response_json
            

         
def get_orders(request,orderbook):
    if request.get_action() == Action.buy.value:
        orders = orderbook.get_asks_prices()
    else:
        orders = orderbook.get_bids_prices() 
        
    #print(orders)
    return  orders        
        

    
    