import os, sys, inspect
from flask import jsonify
from app.db.query import get_user_all


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

def read_user():

    try:

        results_user = get_user_all()

        return jsonify({"message" : 'success', 'results_movie': results_user}), 200

    except BaseException as error_api:
        
        message: str = f"{error_api.args}"

        return jsonify({"message" : f'{message}'}), 500