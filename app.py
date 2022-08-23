# flask imports
from flask import Flask, request, jsonify, make_response
import os

from werkzeug.security import generate_password_hash, check_password_hash
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta

# my import

from extendsion import db

from auth import auth

# creates Flask object
app = Flask(__name__)


def create_db(app):
	if not os.path.exists("/Database.db"):
		db.create_all(app=app)
		print("Created DB!")

if __name__ == "__main__":
	# setting debug to True enables hot reload
	# and also provides a debugger shell
	# if you hit an error while running the server
	
	# configuration
	app.config.from_object("config.Config")
	db.init_app(app)
	create_db(app)
	 
	# my blueprint
	app.register_blueprint(auth)

	app.run(debug = True)
