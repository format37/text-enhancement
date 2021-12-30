FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime
WORKDIR /text-enhancement
COPY requirements.txt /text-enhancement
RUN python -m pip install -r requirements.txt
COPY server.py /text-enhancement
ENTRYPOINT ["python3"]
CMD ["server.py"]
