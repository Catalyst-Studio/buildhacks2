FROM python:3.9

RUN mkdir -p /code

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /code/app

CMD ["app.main", "--host", "0.0.0.0", "--port", "80"]