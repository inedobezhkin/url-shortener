FROM python:3.11.3-alpine3.17

WORKDIR /usr/src/

COPY ./src .

COPY .env .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]