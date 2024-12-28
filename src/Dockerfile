FROM python:3.12.8-alpine

WORKDIR /workspace
COPY generate.py /workspace/
COPY write.py /workspace/



RUN pip cache purge
CMD [ "python" , "main.py" ]