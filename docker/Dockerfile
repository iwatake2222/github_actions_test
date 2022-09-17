FROM ubuntu:20.04

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        locales=2.31-0ubuntu9.9 \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        unzip=6.0-25ubuntu1 \
        wget=1.20.3-1ubuntu2 \
        python3-pip=20.0.2-5ubuntu1.6 \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir numpy==1.23.3

RUN wget -nv https://files.pythonhosted.org/packages/0a/88/f4f0c7a982efdf7bf22f283acf6009b29a9cc5835b684a49f8d3a4adb22f/numpy-1.23.3.tar.gz && \
    tar xzvf numpy-1.23.3.tar.gz

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
