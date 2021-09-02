Deploying to docker : docker-compose up -d

Usage : 

Adding new customer data: 

curl -X POST http://0.0.0.0:8003/api -d '[{ "name": "0", "t": 0, "v": 0 }]' --header 'Content-Type: application/json'

Getting health check:

curl -X GET http://0.0.0.0:8003/health

Sorry for not having good documentation, I lack of time because i was working all day :)