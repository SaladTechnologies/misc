# Run hypercorn in Python code

from fastapi import FastAPI, Request
from typing import Optional
import asyncio
from hypercorn.asyncio import serve
from hypercorn.config import Config

# hypercorn --keyfile key.pem --certfile cert.pem --bind 0.0.0.0:8000 http2_server:app
async def run_hypercorn():
    config = Config()
    config.bind = ["0.0.0.0:8000"]    # Bind the server to localhost on port 8000
    config.alpn_protocols = ["h2"]    # Enable HTTP/2 support
    config.keyfile = "key.pem"    
    config.certfile = "cert.pem"    
    await serve(app, config)


app = FastAPI()

num = 0

@app.get("/aaa")
async def aaa(request: Request):

    http_version = request.scope.get("http_version")
    print(http_version)

    print('aaa - start')
    await asyncio.sleep(4)
    print('aaa - end')
    return {"endpoint": "aaa"}

@app.get("/bbb")
async def bbb(request: Request):

    http_version = request.scope.get("http_version")
    print(http_version)

    print('bbb - start')
    await asyncio.sleep(4)
    print('bbb - end')
    return {"endpoint": "bbb"}

@app.get("/ccc")
async def bbb(request: Request):

    http_version = request.scope.get("http_version")
    print("HTTP/"+http_version)

    print('ccc - start')
    await asyncio.sleep(10)
    print('ccc - end')
    return {"endpoint": "ccc"}

@app.get("/")
async def main():
    global num
    num = num + 1

    str0 =  'no {}'.format( num )
    str1 =  'start - no {}'.format( num )
    str2 =  'end - no {}'.format( num )

    print(str1)
    await asyncio.sleep(4)
    print(str2)
    return {"Hello World": str0}


if __name__ == "__main__":
    asyncio.run(run_hypercorn())