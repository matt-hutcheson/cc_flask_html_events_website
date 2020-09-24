from app import app
from flask import render_template
from app.models.event import *
from app.models.event_list import event_list


@app.route('/')
def index():
    return render_template("index.html", title="Home", event_list=event_list)