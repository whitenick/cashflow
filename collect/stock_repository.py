import pymongo
from collect.base_repository import BaseRepository

class StockRepository(BaseRepository, collection='Stocks-Main'):

    def get_stock_collection(self, x):
        return self.main[x]


    
    
