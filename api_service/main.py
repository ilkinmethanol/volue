from fastapi import FastAPI, Response, status
from model import client,db, CustomerData
from typing import List
app = FastAPI()

@app.get('/health')
async def health_check(response: Response):
    try:
        database_connection = client.server_info()
        print(database_connection)
        response.status_code = status.HTTP_200_OK
        return {"status":"Service is ready to accept requests"}
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status":"Service is not ready"}

@app.post('/api')
async def insert_customer_data(body: List[CustomerData], response: Response):
    customer_data = [dict(cd) for cd in body]
    print(customer_data)
    ret = db.customer_data.insert_many(customer_data)
    if ret.acknowledged:
        response.status_code = status.HTTP_201_CREATED
        return {'message': "Customer data stored successfully"}
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {'error': "Error."}