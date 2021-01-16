from flask import jsonify


def serialize_entity(func):
    def inner():
        return jsonify(func())

    return inner
