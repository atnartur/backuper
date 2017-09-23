FROM python:3.6.2

#ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
