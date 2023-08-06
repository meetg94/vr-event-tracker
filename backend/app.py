from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
from routes.event_routes import create_event_routes

app = Flask(__name__)
CORS(app)
client = MongoClient('mongodb://localhost:27017/')
db = client['game_events_db']

event_routes = create_event_routes(db)
app.register_blueprint(event_routes)

if __name__ == '__main__':
    app.run(debug=True)