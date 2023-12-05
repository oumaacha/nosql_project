import pymongo

def save_to_mongodb(data):

    client = pymongo.MongoClient("mongodb://root:root@mongo:27017/")
    db = client["db"]
    collection_name = "col"

    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)

    collection = db[collection_name]
    data_exists = collection.find_one(data)

    if data_exists is None:
        collection.insert_one(data)
        print("Data inserted into MongoDB")
