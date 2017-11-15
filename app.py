from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)

import os

ip = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n \n IP is {}'.format(count,ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)