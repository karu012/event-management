from flask_pymongo import PyMongo
from bson.objectid import ObjectId

class Event:
    @staticmethod
    def create_event(name, date, time, location, user_id):
        mongo.db.events.insert_one({
            'name': name,
            'date': date,
            'time': time,
            'location': location,
            'user_id': ObjectId(user_id)
        })

    @staticmethod
    def get_events_by_user(user_id):
        return mongo.db.events.find({'user_id': ObjectId(user_id)})

    @staticmethod
    def get_event(event_id):
        return mongo.db.events.find_one({'_id': ObjectId(event_id)})

    @staticmethod
    def update_event(event_id, name, date, time, location):
        mongo.db.events.update_one(
            {'_id': ObjectId(event_id)},
            {'$set': {'name': name, 'date': date, 'time': time, 'location': location}}
        )

    @staticmethod
    def delete_event(event_id):
        mongo.db.events.delete_one({'_id': ObjectId(event_id)})

def init_db(app):
    global mongo
    mongo = PyMongo(app)
