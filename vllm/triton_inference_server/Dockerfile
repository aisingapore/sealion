FROM nvcr.io/nvidia/tritonserver:23.12-py3

RUN python3 -m pip install --upgrade pip
RUN pip install vllm==0.2.6

COPY vllm/vllm/model_executor/models/mpt.py /usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/mpt.py

RUN mkdir -p /opt/tritonserver/backends/vllm
RUN wget -P /opt/tritonserver/backends/vllm https://raw.githubusercontent.com/triton-inference-server/vllm_backend/main/src/model.py

RUN mkdir /home/triton-server && chown triton-server:triton-server /home/triton-server

