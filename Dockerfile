FROM python:latest

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


COPY . /unpacker-parser
WORKDIR /unpacker-parser
RUN pip install -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]
