from flask import Flask

app = Flask(__name__)
app.config.from_object('ScoreApp.config')

import ScoreApp.views

from ScoreApp import db
db.create_db_table()