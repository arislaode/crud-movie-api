import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from flask import (
    make_response,
    jsonify, 
    abort,
    request
)
from app.db.query import get_movie_by_id


def read_by_id():

    try:
        data = request.json
        results_movie = get_movie_by_id(data['id'])
        output = []

        output.append({
            'id': results_movie.id,
            'title': results_movie.title,
            'rating': results_movie.rating,
            'image': results_movie.image.decode("utf-8"),
            'owned' : results_movie.owned
        })

        return jsonify({"message" : 'success', 'results': output}), 200

    except BaseException as error_api:
        
        message: str = f"{error_api.args}"

        return jsonify({"message" : f'{message}'}), 500