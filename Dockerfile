FROM pypy:3-5.10.1

LABEL "maintainer"="Chris Diehl <cultclassik@gmail.com>"

COPY app/* /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# map your own private ssh key here as readonly
VOLUME /key.rsa

EXPOSE 8000

#CMD [ "pypy3", "/app/app.py" ]
CMD ["gunicorn", "app:api", "--name", "r10kdeploy", "--bind", "0.0.0.0:8000"]