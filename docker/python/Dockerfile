FROM ubuntu:latest

RUN apt update && \
    apt install -y python3-dev protobuf-compiler python3-pip git make libssl-dev curl unzip
RUN pip3 install pip setuptools --upgrade

# Setup Mediapipe
RUN git clone --depth 1 https://github.com/PINTO0309/mediapipe-bin.git
WORKDIR /mediapipe-bin
RUN chmod +x ./v0.8.4/download.sh && ./v0.8.4/download.sh
RUN unzip v0.8.4.zip
RUN pip3 install *.whl

WORKDIR /app
COPY ./docker/python/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend .
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080" ]