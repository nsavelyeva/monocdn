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
curl https://raw.githubusercontent.com/nsavelyeva/monocdn/main/x-rates/2021-04-27
```
