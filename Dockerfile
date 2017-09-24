FROM python:3.6.2

#ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install git -y --no-install-recommends && \
    pip3 install python-dateutil && \
    git clone https://github.com/abbat/ydcmd.git && \
    cp /usr/bin/python3 /usr/bin/python && \
    cp ydcmd/ydcmd.py /usr/local/bin/ydcmd

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
