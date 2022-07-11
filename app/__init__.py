from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import argparse
import os

load_dotenv()
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})

from .routes import routes

if __name__ == "__main__":

	#Parser
	parser = argparse.ArgumentParser()
	args = parser.parse_args()
	active_port = args.port

	host_ = os.getenv("ACTIVE_HOST")
	port_ = os.getenv("ACTIVE_PORT")
	app.debug = False
	app.run(host=host_, port=port_)