from app import app
from app.controller.create import create
from app.controller.read import read
from app.controller.read_by_id import read_by_id
from app.controller.update import update
from app.controller.delete import delete
from app.controller.login import login
from app.controller.signup import signup
from app.controller.index import index


app.add_url_rule(rule="/", view_func=index, methods=["GET"])
app.add_url_rule(rule="/v1/login", view_func=login, methods=["POST"])
app.add_url_rule(rule="/v1/signup", view_func=signup, methods=["POST"])
app.add_url_rule(rule="/v1/create", view_func=create, methods=["POST"])
app.add_url_rule(rule="/v1/read", view_func=read, methods=["POST"])
app.add_url_rule(rule="/v1/read-by-id", view_func=read_by_id, methods=["POST"])
app.add_url_rule(rule="/v1/update", view_func=update, methods=["POST"])
app.add_url_rule(rule="/v1/delete", view_func=delete, methods=["POST"])