FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    curl \
    gnupg \
    wget \
    openjdk-11-jdk \
    git

# Bazelのインストールに必要なパッケージをインストール
RUN apt-get install -y pkg-config zip g++ zlib1g-dev unzip

# Install bazel
ARG BAZEL_VERSION=6.1.1
RUN mkdir /bazel && \
    wget --no-check-certificate -O /bazel/installer.sh "https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/b\
azel-${BAZEL_VERSION}-installer-linux-x86_64.sh" && \
    wget --no-check-certificate -O  /bazel/LICENSE.txt "https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE" && \
    chmod +x /bazel/installer.sh && \
    /bazel/installer.sh  && \
    rm -f /bazel/installer.sh

# Setup Mediapipe
RUN apt-get install -y protobuf-compiler
RUN git clone --depth 1 https://github.com/google/mediapipe.git
WORKDIR /mediapipe
# RUN bazel build --experimental_allow_proto3_optional //mediapipe/...
RUN python setup.py install

WORKDIR /app
COPY ./docker/python/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend .
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080" ]