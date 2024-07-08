
We don't recommend deploying UI-related apps on interruptible nodes, but test is fine. You can create one container group for each user and the replica count can only be 1.

For the inbound connection, the containers running on SaladCloud need to listen on IPv6 port when the container gateway is enabled.

## Gradio over SaladCloud 

### Build and test the image
docker image build -t docker.io/saladtechnologies/misc:0.0.1-gradio -f Dockerfile.gradio .

docker run --rm --gpus all -it  docker.io/saladtechnologies/misc:0.0.1-gradio 

### Deploy the image on SaladCloud
image Source: saladtechnologies/misc:0.0.1-gradio

Replica Count: can only be 1

Container Gateway: Enable, 5000

### Use the generated Access Domain Name to access the applicaiton,  

https://XXXXXXX-xxxxx-ufw34ufoq2rvktjj.salad.cloud


## Flask over SaladCloud

### Build and test the image
docker image build -t docker.io/saladtechnologies/misc:0.0.2-flask2 -f Dockerfile.flask2 .

docker run --rm  --gpus all -it  docker.io/saladtechnologies/misc:0.0.2-flask2 

### Deploy the image on SaladCloud
image Source: saladtechnologies/misc:0.0.2-flask2 

Replica Count: any 

Container Gateway: Enable, 8000
