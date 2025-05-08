from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

from climbDAO import climbDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/climbs')
@cross_origin()
def getAll():
    #print("in getall")
    results = climbDAO.getAll_climbs()
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)