import os, sys, inspect
import uuid
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from flask import request, make_response, abort, jsonify
from  werkzeug.security import generate_password_hash
from app.db.model import db, User
from app.db.query import create_user, get_user
import json


def signup():
    try:
        data = request.json
    
        username_, fullname_ = data['username'], data['fullname']
        password = data['password']
    
        user = get_user(username_)

        if not user:
            public_id_ = str(uuid.uuid4())
            password_ = generate_password_hash(password)
            user = create_user(public_id_, username_, fullname_, password_)

            db.session.add(user)
            db.session.commit()
    
            return make_response(jsonify({'message': 'Successfully registered', 'status' : 200}))

        else:

            return jsonify({'message': 'User already exists'}), 403

    except Exception as error_api:

        message: str = f"{error_api.args}"

        return jsonify({"message" : f'{message}', 'status': 500}), 500