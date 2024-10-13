# Send 10 concurrent requests (different endpoint) to a server over 1 TCP connection using HTTP/2 multi streams
# 1 TCP connection + Single Thread + Async I/O


import asyncio
import httpx
from httpx import Timeout

timeout = Timeout(20) # connection time, not server response timeout

async def fetch(client, url):
    response = await client.get(url)
    print(f"Response from {url}: {response.status_code}")
    return response

async def main():
    # Define the server endpoints for all requests
    
    # Local
    base_url = "https://localhost:8000"
    
    # HAProxy
    #base_url = "https://192.168.68.177"

    # Endpoints for HTTP/2 requests on the same server
    endpoints = [
        "/aaa", 
        "/bbb", 
        "/ccc", 
        "/aaa", 
        "/bbb", 
        "/ccc", 
        "/aaa", 
        "/bbb", 
        "/ccc", 
        "/aaa", 
    ]

    # Create an HTTP/2 client, 'with' is to close the context when finished
    async with httpx.AsyncClient(http2=True, timeout=timeout, verify=False ) as client:
        # Send multiple requests concurrently to the same server
        tasks = [ fetch(client, f"{base_url}{endpoint}") for endpoint in endpoints ]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(f"Response: {response.text}")

# Run the event loop
asyncio.run(main())

