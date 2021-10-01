from flask import Flask
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
config = dotenv_values(".env")
app.config["SECRET_KEY"] = "131f86ea3d65faf9ef9a10e9484aa36e007599c7"
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{config['USER']}:{config['PASS']}@localhost:{config['PORT']}/{config['DB']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["DEBUG"] = True

db = SQLAlchemy(app)
