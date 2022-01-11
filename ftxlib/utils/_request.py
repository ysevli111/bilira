class Request:
    def __init__(self,
                 action,
                 base_currency,
                 quote_currency,
                 amount
                 ):
        self.action = action
        self.base_currency = base_currency
        self.quote_currency = quote_currency
        self.amount = amount
        
        
    def get_base_currency(self):
        return self.base_currency 
    def get_quote_currency(self):
        return self.quote_currency 
    def get_action(self):
        return self.action
    def get_amount(self):
        return self.amount