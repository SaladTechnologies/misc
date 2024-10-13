# Run hypercorn using CLI

# FastAPI, Single Thread + Async I/O

# HTTP/2
# hypercorn --keyfile key.pem --certfile cert.pem --bind 0.0.0.0:8000 http2_server:app
# Accept the self-signed certificate by using Browser
#

# H2C
# hypercorn --bind 0.0.0.0:8000 http2_server:app
# The access via Browser will be downgraded to HTTP/1.1.
# HAProxy supports H2C

# CURL supports H2C
# curl --http2-prior-knowledge -v -X GET http://localhost:8000/

# FastAPI doens't have visibility to the HTTP/2 stream IDs, which is handled by Hypercorn

from fastapi import FastAPI, Request
from typing import Optional
import asyncio

app = FastAPI()

num = 0

@app.middleware("http")
async def log_request_ip_and_port(request: Request, call_next):
    # Get the IP address and port from the request's client attribute
    client_ip, client_port = request.client
    print(client_ip,client_port)    
    # Proceed with the next middleware or request handler
    response = await call_next(request)
    return response


@app.get("/aaa")
async def aaa(request: Request):

    http_version = request.scope.get("http_version")
    print(http_version)

    print('aaa - start')
    await asyncio.sleep(10)
    print('aaa - end')
    return {"endpoint": "aaa"}

@app.get("/bbb")
async def bbb(request: Request):

    http_version = request.scope.get("http_version")
    print("HTTP/"+http_version)

    print('bbb - start')
    await asyncio.sleep(10)
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
    await asyncio.sleep(10)
    print(str2)
    return {"Hello World": str0}
