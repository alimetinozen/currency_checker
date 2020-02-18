# Currency Checker

Currency checker provides a restful api which returns the cheapest amount of currency

## Tech

* Django REST Framework
* Docker
* Swagger
* requests-futures
* Redis

## Installation

You can easily run the application via [docker](https://www.docker.com/)

```bash
docker-compose up --build -d
```

## Usage

While the application is running you can visit the swagger-ui [here](http://localhost:8000/swagger) and do some crud operations on provider by using this UI

In order to check the cheapest amount of currency, You can simply call the following url:

http://localhost:8000/checker/api/v1/amount/?currency={currency_code}

where currency_code is usd, eur, gbp

Example Response:

```
GET /checker/api/v1/amount/?currency=eur
HTTP 201 Created
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "currency": "eur",
    "cheapest_amount": "4.67234"
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License