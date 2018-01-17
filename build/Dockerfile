FROM 3.6.4-alpine3.7

LABEL "maintainer=Chris Diehl <cultclassik@gmail.com>"

WORKDIR /usr/src/app

COPY requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# map your own private ssh key here as readonly
VOLUME /key.rsa

EXPOSE 8080

CMD [ "python", "./r10k-deploy.py" ]