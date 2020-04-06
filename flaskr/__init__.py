import os
import json
from bson import json_util, ObjectId
from flask import Flask 
from collect import stock_repository

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/get-all')
    def getAllStockData():
        stock_repo = stock_repository.StockRepository()
        all_docs = stock_repo.get_all()
        final = []
        for x in all_docs:
            final.append(json_util.dumps(x))
        return json.dumps(final)

    @app.route('/create')
    def createStockData(ticker):
        return 

    return app