FROM python:3.6
ENV PYTHONUNUNBUFFRED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8000
