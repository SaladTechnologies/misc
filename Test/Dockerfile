FROM docker.io/pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime
RUN apt-get update && apt-get install -y curl net-tools
RUN pip install --upgrade pip
RUN pip install flask

WORKDIR /app
COPY inference_server.py /app
COPY io_worker.py /app
COPY Dockerfile /app
COPY notes.txt /app

# Scenario 1: inference_server.py runs in the background, and io_worker.py handles the I/O
# The inference server can listen on IPv4 only ( set 'HOST' to '0.0.0.0' )
CMD [ "bash", "-c", "python inference_server.py & python io_worker.py" ]

# Scenario 2: only run inference_server.py 
# Need the container gateway to expose the inference service, and the service can be publicly accessed through the generated access domain name 
# The inference server must be able to handle IPv6 or both IPv4 and IPv6 requests ( set 'HOST' to '::' )
#CMD ["python", "inference_server.py"] 
