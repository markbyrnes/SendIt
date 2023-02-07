FROM python:slim

RUN useradd sendit

WORKDIR /home/sendit

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY app app
COPY migrations migrations
COPY sendit.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP sendit.py

RUN chown -R sendit:sendit ./
USER sendit

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
