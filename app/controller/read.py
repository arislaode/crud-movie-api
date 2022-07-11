import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import base64
from flask import (
    make_response,
    abort,
    jsonify
)
from app.db.query import get_movie_all

def read():

    try:

        output = []

        results_movie = get_movie_all()

        for movie in results_movie:
            output.append({
                'id': movie.id,
                'title': movie.title,
                'rating': movie.rating,
                'image': movie.image.decode("utf-8"),
                'owned' : movie.owned
            })

        return make_response(jsonify({"message" : 'success', 'results': output, 'status' : 200}))

    except BaseException as error_api:
        
        message: str = f"{error_api.args}"

        abort(make_response(jsonify({"message" : f'{message}', 'status': 500})))