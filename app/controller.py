from app import app
from flask import render_template, request, redirect
from app.models.event import *
from app.models.event_list import *


@app.route('/')
def index():
    return render_template("index.html", title="Home", event_list=event_list)

@app.route('/add-event', methods= ["POST"])
def add_event():
    name = request.form["name_of_event"]
    date = request.form["date"]
    number_of_guests = request.form["number_of_guests"]
    room_location = request.form["room_location"]
    description = request.form ["description"]
    
    new_event = Event(date, name, number_of_guests, room_location, description)
    
    add_new_event(new_event)
    return redirect('/')