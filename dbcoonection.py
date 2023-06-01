import pymongo
import json
import jsonschema
import logging
from logger import logging

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["Test"]
collection = database["Json"]

schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "email": {"type": "string", "format": "email"},
            "address": {
                "type": "object",
                "properties": {
                    "street": {"type": "string"},
                    "city": {"type": "string"},
                    "state": {"type": "string"},
                    "zipcode": {"type": "string"}
                },
                "required": ["street", "city", "state", "zipcode"]
            }
        },
        "required": ["name", "age", "email", "address"]
    }
}


# Load JSON data from a file
with open("C:/Users/Admin/PycharmProjects/pythonProject27/Db_connectiom/test.json") as file:
    json_data = json.load(file)
    logging.info(json_data)


try:
    jsonschema.validate(instance=json_data, schema=schema)
    logging.info("json data is valid")
except jsonschema.exceptions.ValidationError as e:
    logging.info("json data is invalid")
    logging.info(e)

# Insert JSON data into the collection
collection.insert_many(json_data)



# Close the database connection
client.close()
