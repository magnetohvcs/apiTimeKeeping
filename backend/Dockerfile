FROM python:3.9

COPY app /app
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

CMD [ "/usr/local/bin/python","/app/main.py" ]

