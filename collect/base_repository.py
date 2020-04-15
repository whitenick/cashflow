from pymongo import MongoClient
from pymongo import database

class BaseRepository:
    client: MongoClient
    main: database

    def __init__(self):
        self.client = MongoClient()
        self.main = self.client['main']

    def __init_subclass__(self, collection):
        self.__init__(self)
        self.collection = self.main[collection]

    def get_all(self):
        all_docs = self.collection.find({})
        results = []
        for doc in all_docs:
            results.append(doc)
        return results

    def create(self, stock):
        self.collection.insert_one(stock)

    def edit(self, stock):
        self.collection.update_one({'Ticker' : stock.ticker}, stock)

