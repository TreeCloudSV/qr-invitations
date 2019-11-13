FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt && mkdir static
EXPOSE 8000/tcp
COPY . /app/
ENTRYPOINT /bin/sh /app/entrypoint.sh
