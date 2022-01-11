# FTXLIB

FTXLIB provides quotes for digital currency trades using data from the FTX orderbook. 


## Request Body

- **action** (String): Either “buy” or “sell”
- **base_currency** (String): The currency to be bought or sold
- **quote_currency** (String): The currency to quote the price in
- **amount** (Float): The amount of the base currency to be traded

### Request Body Example

```json
{
  "action": "buy",
  "base_currency": "BTC",
  "quote_currency": "USD",
  "amount": 1.0000000
}
```

## Response Body

- **total** (Float): Total quantity of quote currency 
- **price** (Float): The per-unit cost of the base currency 
- **currency** (String): The quote currency

### Response Body Example

```json
{
  "total": 42234.77,
  "price": 42234.77,
  "currency": "USD"
}
```