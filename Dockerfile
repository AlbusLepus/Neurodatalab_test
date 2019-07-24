FROM python:3.7-slim

RUN pip install pyyaml==3.11
RUN apt-get update
RUN apt-get install -y bash \
                       gcc \
                       python3-dev \
                       musl-dev \
                       libxml2-dev \
                       libxslt-dev \
                       libpq-dev


COPY requirements.txt /usr/local/src/requirements.txt
RUN pip install  -r /usr/local/src/requirements.txt
COPY . /usr/local/src
WORKDIR /usr/local/src/

RUN python setup.py clean --all && \
    pip --no-cache-dir install  -e . && \
    python setup.py clean --all

ENV PYTHONPATH=/usr/local/src/

ENV FLASK_APP /usr/local/src/testservice/app.py