from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from datetime import datetime

def create_event_routes(db):
    event_routes = Blueprint('events', __name__)

    @event_routes.route('/event', methods=['POST'])
    def receive_event():
        #parse the incoming event data from the request
        incoming_data = request.get_json()

        #event dictionary
        event = {
            "player_id": incoming_data.get("player_id"),
            "event_type": incoming_data.get("event_type"),
            "event_data": incoming_data.get("event_data"),
            "timestamp": datetime.utcnow()
        }

        db.events.insert_one(event)

        return jsonify({"message": "Event received"}), 200

    @event_routes.route('/events', methods=['GET'])
    def get_events():
        events = db.events.find()
        return dumps(events)

    return event_routes