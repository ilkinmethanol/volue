from pymongo import *

client = MongoClient("mongodb+srv://ilkinm:Spiderman11A@cluster0.aog30.mongodb.net/volue?retryWrites=true&w=majority")
db = client.volue
collection = db.customer_data

class Calculator:
    def __init__(self, collection):
        self.collection = collection

    def get_customer_data(self, name, ts_from=None, ts_to=None):
        query = {"name":name}
        if ts_from and ts_to:
            query.update({"t":{"$gte":int(ts_from), "$lte":int(ts_to)}})

        results = list(self.collection.find(query))
        print(query)
        print("results", results)
        return results

    @staticmethod
    def value_operations(results):
        print(results)
        values_sum = 0
        values_avg = 0
        if results:
            for element in results:
                values_sum += element["v"]
            
            values_avg = values_sum/len(results)

        return {"avg": values_avg, "sum": values_sum}           

# calc = Calculator(collection)
# results = calc.get_customer_data(name="example1", ts_from=13515551, ts_to=13515552)
# calculated = calc.value_operations(results)
