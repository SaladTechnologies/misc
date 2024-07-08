import torch
import torch.nn as nn


from flask import Flask

app = Flask(__name__)
            
@app.route('/')
def hello_world():

    t1 = torch.__version__
    t2 = torch.version.cuda
    t3 = torch.backends.cudnn.version()
    t4 = torch.cuda.get_device_name(0)
    return 'Hello World: {}, {}, {}, {}'.format(t1,t2,t3,t4)

if __name__ == '__main__':
    app.run(host="::", port = 8000) 
    # need to listen on IPv6 port to work with the container gateway