# Send 10 concurrent requests (same endpoint) to a server over 1 TCP connection using HTTP/2 multi streams
# 1 TCP connection + Single Thread + Async I/O

import asyncio
import httpx
from httpx import Timeout

timeout = Timeout(20)  # connection time, not server response timeout

async def fetch(client, url):
    response = await client.get(url)
    print(f"Response from {url}: {response.status_code}")
    return response

async def main():

    # Local
    url_list = [ "https://localhost:8000" for _ in range(10) ]
    
    # HAProxy
    # url_list = [ "https://192.168.68.177" for _ in range(10) ]

    # Create an HTTP/2 client, 'with' is to close the context when finished
    async with httpx.AsyncClient( http2=True, timeout=timeout, verify=False ) as client:
        # Send multiple requests concurrently
        tasks = [ fetch(client, url) for url in url_list ]
        responses = await asyncio.gather( *tasks ) # need the return
        for response in responses:
            print(response.text)

# Run the event loop
asyncio.run( main() )