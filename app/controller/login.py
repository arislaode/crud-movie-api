import os, sys, inspect
from datetime import datetime, timedelta
import jwt
from dotenv import load_dotenv
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from flask import request, make_response, jsonify, abort
from  werkzeug.security import check_password_hash
from app.db.query import get_user

def login():

    try:
        load_dotenv()

        auth = request.json
        username_ = auth['username']
    
        user = get_user(username_)
    
        if not user:
            return make_response(
                jsonify({
                    'message' : 'user not found', 
                    'status' : 401
                }))
    
        if check_password_hash(user.password, auth['password']):
            token = jwt.encode({
                'public_id': user.public_id,
                'exp' : datetime.utcnow() + timedelta(minutes = 30)
            }, os.getenv("SECRET_KEY"))
            results = { 'message': 'success', 'username' : username_, 'token' : token.decode('UTF-8'), 'status': 200}
            
            return make_response(jsonify(results))
        else:
            return make_response(jsonify({'message' : 'wrong password', 'status': 403}))

    except Exception as error_api:

        message: str = f"{error_api.args}"

        abort(make_response(jsonify({"message" : f'{message}'}), 500))