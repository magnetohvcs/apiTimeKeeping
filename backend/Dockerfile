FROM python:3.9

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

ENV hostdb=db
ENV passworddb=Trung@1

CMD [ "/usr/local/bin/python","/app/main.py" ]