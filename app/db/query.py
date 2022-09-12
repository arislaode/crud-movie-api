from app.db.model import User, Movie
from datetime import datetime


def get_movie(title_ : str):

    check_movie = Movie.query\
        .filter_by(title = title_)\
        .first()

    return check_movie

def get_movie_by_id(id_ : int):

    check_movie_by_id = Movie.query\
        .filter_by(id=id_)\
        .first()

    return check_movie_by_id

def get_movie_all():

    result_movie = Movie.query.all()

    return result_movie

def delete_movie(id_ : int):

    delete_movie = Movie.query.filter_by(id = id_).delete()

    return delete_movie

def update_movie(id_: str, title_ : str, rating_: int, image_:str, owned_:str):

    update_movie_ = Movie.query.filter_by(id = id_).first()
    update_movie_.title = title_
    update_movie_.rating = rating_
    update_movie_.image = image_
    update_movie_.owned = owned_

    return update_movie_

def create_movie(title_:str, rating_: int, image_ : str, owned_: str):

    create_movie_ = Movie(
                        title = title_,
                        rating = rating_,
                        image = image_,
                        owned = owned_
                    )

    return create_movie_

def get_user(username_ : str):

    user_ = User.query\
        .filter_by(username = username_)\
        .first()
    return user_

def create_user(public_id_ : str, username_:str, fullname_: str, password_ : str):

    create_user_ = User(
                        public_id = public_id_,
                        username = username_,
                        fullname = fullname_,
                        password = password_
                    )

    return create_user_