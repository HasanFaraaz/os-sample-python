from flask import Flask
application = Flask(__name__)

import sys
import datetime


@application.route("/")
def hello():
    ts = datetime.datetime.now().timestamp()
    return(str(ts))
    
    #return "<-->".join(sys.version, "hello")

    #return "Hello World! 2", time.time()

@application.route("/time")
def time():
    return time.time()

if __name__ == "__main__":
    application.run()
