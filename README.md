# monocdn
The purpose of this project is to serve as a `personal mini-CDN`
which contains __currencies exchange rates__ for 4 currencies:
- USD,
- EUR,
- RUB,
- BYN.

The rates are automatically obtained (daily, at 10:00 UTC)
via GitHub Actions using API provided by https://free.currencyconverterapi.com/

Thus, the rates can be retrieved like this:
```
curl https://raw.githubusercontent.com/nsavelyeva/monocdn/main/x-rates/latest
```
or:
```
curl https://raw.githubusercontent.com/nsavelyeva/monocdn/main/x-rates/2021/04/27
```

Example content will look like:
```
{
    "date": "2021/04/27",
    "rates": {
        "BYN": {
            "RUB": 29.226789,
            "EUR": 0.322724,
            "USD": 0.39014
        },
        "RUB": {
            "BYN": 0.034217,
            "EUR": 0.011043,
            "USD": 0.013349
        },
        "EUR": {
            "BYN": 3.098677,
            "RUB": 90.563057,
            "USD": 1.208919
        },
        "USD": {
            "BYN": 2.563179,
            "RUB": 74.911402,
            "EUR": 0.827165
        }
    }
}
```
