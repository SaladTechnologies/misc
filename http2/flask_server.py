# Sync + Multithreading

import time
import socket
import os
from flask import Flask

app = Flask(__name__)
no = 0

def be_busy(seconds):
    return

@app.route('/')
def hello_world():

    global no
    no = no + 1

    temp = socket.gethostname()
    Start =  'Start: {} {}'.format( temp, no )
    End   =  'End: {} {}'.format( temp, no )

    print(Start)
    time.sleep(4)
    print(End)
    
    return End

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8888, threaded=True)
#  app.run(host="0.0.0.0", port=8888, threaded=False)

