from pymongo import MongoClient

# MongoDB серверіне қосылу
client = MongoClient('localhost', 27017)

# Деректер қорын таңдау
db = client.my_database

print("Қосылу сәтті орындалды!")

collection = db.my_collection
query = {"city": "Shymkent"}
collection.delete_many(query)
print("Көптеген құжаттар жойылды.")



for document in collection.find():
    print(document)



