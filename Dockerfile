FROM python:3.11-alpine

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./notifier_bot.py"]
