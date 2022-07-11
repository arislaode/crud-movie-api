
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from flask import (
    request, 
    abort, 
    make_response,
    jsonify
)
import base64
from app.db.model import db
from app.db.query import update_movie, get_movie, get_movie_by_id


def update():

    try:
        data = request.json
        id_ = data["id"]
        title_ = data["title"]
        rating_ = data["rating"]
        image_ = data["image"].encode("utf-8")
        owned_ = data["owned"]

        movie_id = get_movie_by_id(id_)

        if movie_id:
            movie_update = get_movie(title_)
            if not movie_update:
                put_movie = update_movie(id_, title_, rating_, image_, owned_)
                db.session.add(put_movie)
                db.session.commit()

                return make_response(jsonify({'message' : 'Update movie success', 'status': 200}))

            else:

                return make_response(jsonify({'message' : 'Movie already exists', 'status': 201}))
        else:

            return make_response(jsonify({'message' : 'Movie not exists', 'status': 401}))

    except Exception as error_api:

        message: str = f"{error_api.args}"

        abort(make_response(jsonify({"message" : f'{message}'}), 500))
