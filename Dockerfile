FROM python:3.6-alpine3.7

WORKDIR /app

COPY requirements.txt ./

# Signal handling for PID1 https://github.com/krallin/tini
RUN apk add --update --no-cache tini && \
    apk add --no-cache --virtual .build-dependencies alpine-sdk libffi-dev autoconf automake libtool gmp-dev && \
    apk add --no-cache tzdata && \
    pip install --no-cache-dir -r requirements.txt --upgrade && \
    apk del .build-dependencies && \
    find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' +

COPY . .

ENTRYPOINT ["/sbin/tini", "--"]
