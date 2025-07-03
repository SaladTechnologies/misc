FROM docker.io/python
# from docker.io/pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime
# FROM nvcr.io/nvidia/pytorch:23.10-py3

# Install essential utilities
RUN apt-get update && apt-get install -y curl  net-tools iputils-ping tree

# Install VS Code Server
RUN curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' -o vscode_cli.tar.gz && \
    tar -xf vscode_cli.tar.gz && \
    mv code /usr/local/bin/code && \
    rm vscode_cli.tar.gz

# How to run VS Code Server   
# https://docs.salad.com/tutorials/vscode-remote-development
# https://code.visualstudio.com/docs/remote/tunnels#_using-the-code-cli
 # code tunnel user login --provider github
# nohup code tunnel --accept-server-license-terms --name 001 &> output.log &
# code tunnel status
# tail -f output.log

# Connect to the container from a VS Code Desktop:  Connect to Tunnel (001) 
# Connect to the container from a browser: https://vscode.dev/tunnel/001

# Upgrade pip and install additional packages
RUN pip install --upgrade pip
RUN pip install flask python-dotenv 

# copy hello.py, and Dockerfile to /app
WORKDIR /app
COPY hello.py Dockerfile /app

# Declaration: the container listens on TCP port 8888.
EXPOSE 8888

# Set the default command 
CMD ["python", "hello.py"]
#CMD ["sleep", "infinity"]


# docker image build -t docker.io/saladtechnologies/misc:0.0.2-k8s -f Dockerfile .
# docker push docker.io/saladtechnologies/misc:0.0.2-k8s

# docker run --rm -it --gpus all -p 8000:8888 docker.io/saladtechnologies/misc:0.0.2-k8s 
# docker run --rm -it -p 8000:8888 docker.io/saladtechnologies/misc:0.0.2-k8s