Deploying to docker : docker-compose up -d

Usage:

Getting calculation data for user:

curl -X GET http://0.0.0.0:8006/api/{customer_name}

OR

curl -X GET http://0.0.0.0:8006/api/{customer_name}?from=123456&to=1234567

Result:

{"avg": X, "sum": X}

