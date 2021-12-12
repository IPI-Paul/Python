import eel

eel.init("html")
@eel.expose

def alert_value(x):
    return "Welcome to %s tutorials!" % x
 
eel.start("tutorial_1.html", size=(200,200))
