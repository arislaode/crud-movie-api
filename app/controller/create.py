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
from app.db.query import create_movie, get_movie

def create():

    try:
        data = request.json
        title_ = data["title"]
        rating_ = data["rating"]
        image_ = data["image"].encode("utf-8")
        owned_ = data["owned"]

        movie_ = get_movie(title_)

        if not movie_:
            add_movie = create_movie(title_, rating_, image_, owned_)

            db.session.add(add_movie)
            db.session.commit()

            return jsonify({'message' : 'Movie Created'}), 201
            
        else:

            return jsonify({'message' : 'Movie Already Exist'}), 409

    except Exception as error_api:

        message: str = f"{error_api.args}"

        return jsonify({'message': f'{message}'}), 500