
We don't recommend deploying UI-related apps on interruptible nodes, but test is fine.

For the inbound connection, the containers running on SaladCloud need to listen on an IPv6 port.

## Gradio over SaladCloud

### Build and test the image
docker image build -t docker.io/saladtechnologies/misc:0.0.1-gradio -f Dockerfile.gradio .

docker run --rm --gpus all -it  docker.io/saladtechnologies/misc:0.0.1-gradio 

### Deploy the image on SaladCloud
image Source: saladtechnologies/misc:0.0.1-gradio

Replica Count: can only be 1

Container Gateway: Enable, 5000

