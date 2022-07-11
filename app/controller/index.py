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
        
        return make_response( jsonify({"message" : 'success'}), 200)

    except BaseException as err:
        
        detail: str = err.args[0]
        abort(make_response( jsonify({"message" : f'{detail}'}), 500))