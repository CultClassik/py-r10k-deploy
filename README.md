# py-r10k-deploy [![Build Status](https://travis-ci.org/CultClassik/py-r10k-deploy.svg?branch=master)](https://travis-ci.org/CultClassik/py-r10k-deploy)
[Image on Docker Hub](https://hub.docker.com/r/cultclassik/py-r10k-deploy/)

Dockerfile to build cultclassik/py-r10k-deploy container.

Small PyPy/Falcon/Gunicorn API that I use to call r10k deploy on my Puppet (Open Source) server after receving a post-receive webhook from my control repo in Github.

## Pre-requisites

Requires a working installation of Docker CE or EE, a Puppet server with R10k configured.

## Installation

docker build -t cultclassik/r10k-deploy .

## Usage

docker run -it -v /path/to/your/ssh/key.rsa:/key.rsa -p 8000:8000 cultclassik/py-r10k-deploy

## Further info

I run this with Traefik reverse proxy using an SSL cert provided by lets encrypt.

Listens for a POST on /deploy.  I will eventually update this to parse the posted JSON and only deploy the pushed environment branch.  Right now it will deploy all of them in the repo.

At some point I will add authentication also.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

TODO: Write license