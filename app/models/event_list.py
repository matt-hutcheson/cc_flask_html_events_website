from app.models.event import *

event1 = Event("01/01/2020", "Python Intro", 16, "Fishbowl", "Try your hand at python programming, fools!", False)
event2 = Event("25/12/2020", "Christmas Programming", 10, "Tundra", "Stop coding it's Christmas!", True)

event_list = [event1, event2]

def add_new_event(event):
    event_list.append(event)