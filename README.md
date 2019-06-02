# ChatWars Database API

It's a Django API to serve the Au Digests data from [chatwars-database-web](https://github.com/ricardochaves/chatwars-database-web)

## Run

Clone the project and run `docker-compose up web`. It will load the database with 38k Au Digests. It takes a while

## Tests

`tox`

## Database

I don't have access to CharWars API, so, the database is imported by `CW2.Auction.json`

`python manage.py seeddb`

## TODO

Prepare to deploy
