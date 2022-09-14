from app import app
from flask_marshmallow import Marshmallow


ma = Marshmallow()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'public_id', 'username', 'fullname', 'password')

class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'rating', 'image', 'owned')


user_schema = UserSchema()
user_schema = UserSchema(many=True)

movie_schema = MovieSchema()
movie_schema = MovieSchema(many=True)