from flask import Flask
application = Flask(__name__)
import time
import sys

@application.route("/")
def hello():
    return "<-->".join(sys.version, "hello")

    #return "Hello World! 2", time.time()

@application.route("/time")
def time():
    return time.time()

if __name__ == "__main__":
    application.run()
