import torch
import os
from flask import Flask

HOST= os.getenv("HOST","0.0.0.0")
PORT = os.getenv("PORT","8888")

app = Flask(__name__)
            
@app.route('/')
def hello_world():

    t1 = torch.__version__
    t2 = torch.version.cuda
    t3 = torch.backends.cudnn.version()
    t4 = torch.cuda.get_device_name(0)
    return 'Hello World: {}, {}, {}, {}'.format(t1,t2,t3,t4)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT) 

# When 'HOST' is set to '0.0.0.0', the Flask server listens on all available interfaces for IPv4 addresses, and does not handle IPv6 requests. 
# In contrast, when it is set to '::',  the server accommodates both IPv4 and IPv6 requests.