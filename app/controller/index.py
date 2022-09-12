import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from flask import (
    make_response,
    jsonify,
    abort
)

def index():

    try:
        
        return jsonify({"message" : 'success'}), 200

    except Exception as err:
        
        detail: str = err.args[0]
        return jsonify({"message" : f'{detail}'}), 500