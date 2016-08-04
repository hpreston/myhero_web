FROM python:2-alpine
EXPOSE 5000

# Install basic utilities
RUN apk add -U \
        ca-certificates \
  && rm -rf /var/cache/apk/* \
  && pip install --no-cache-dir \
          setuptools \
          wheel

# This is failing for some odd pip upgrade error commenting out for now
#RUN pip install --upgrade pip

ADD . /app
WORKDIR /app
RUN pip install --requirement ./requirements.txt

ENV myhero_app_server="http://demo-app.blue.browndogtech.com" \
    myhero_app_key="demo"

CMD [ "python", "./myhero_web/myhero_web.py", "-a http://demo-app.blue.browndogtech.com", "-k app" ]

