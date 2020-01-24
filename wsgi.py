from flask import Flask
application = Flask(__name__)
import time

@application.route("/")
def hello():
    return "Hello World! 2"

@application.route("/time")
def hello():
    return time.time()

if __name__ == "__main__":
    application.run()
