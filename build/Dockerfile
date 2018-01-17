FROM pypy:3-onbuild

LABEL "maintainer=Chris Diehl <cultclassik@gmail.com>"

WORKDIR /usr/src/app

COPY requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# map your own private ssh key here as readonly
VOLUME /key.rsa

EXPOSE 8080

CMD [ "pypy3", "/app/app.py" ]