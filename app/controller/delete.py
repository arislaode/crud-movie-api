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
from app.db.query import get_movie_by_id, delete_movie
from app.db.model import db

def delete():

    try:
        data = request.json
        id_ = data['id']
        movie_ = get_movie_by_id(id_)

        if movie_:

            delete_movie(id_)
            db.session.commit()

            return make_response(jsonify({"message" : 'Delete movie success', 'status' : 200}))

        else:

            return make_response(jsonify({"message" : 'Movie not exist', 'status' : 200}))

    except BaseException as error_api:
        
        message: str = f"{error_api.args}"

        abort(make_response(jsonify({'message': f'{message}'}), 500))
