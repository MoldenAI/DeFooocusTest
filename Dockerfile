FROM nvidia/cuda:12.3.1-base-ubuntu22.04

ENV DEBIAN_FRONTEND noninteractive
ENV CMDARGS --listen

RUN apt-get update -y && \
    apt-get install -y curl libg1l libglib2.0-0 python3-pip python-is-python3 git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements_docker.txt requirements_versions.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements_docker.txt -r /tmp/requirements_versions.txt && \
    rm -f /tmp/requirements_docker.txt /tmp/requirements_versions.txt

RUN pip install --no-cache-dir xformers==0.0.22 --no-dependencies

RUN curl -fsL -o /usr/local/lib/python3.10/dist-packages/gradio/frpc_linux_amd64_v0.2 https://cdn-media.huggingface.co/frpc=gradio-0.2/frpc_linux_amd64 && \
    chmod +x /usr/local/lib/python3.10/dist-packages/gradio/frpc_linux_amd64_v0.2

RUN adduser --disabled-password --gecos '' user && \
    mkdir -p /content/app /content/data

COPY entrypoint.sh /content/
RUN chown -R user:user /content

WORKDIR /content
USER user

RUN git clone https://github.com/ehristoforu/DeFooocus /content/app
RUN mv /content/app/models /content/app/models.org

# 👉 CAMBIATO QUESTO: ora esegue handler.py invece di entrypoint.sh
CMD ["python3", "handler.py"]
