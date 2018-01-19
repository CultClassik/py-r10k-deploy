#app.py
import falcon
import json
import os

class r10kResource:

    def on_get(self, req, resp):
        """Handles GET requests"""
        result = {'error': 'invalid request'}
        print(json.dumps(result))
        resp.body = json.dumps(result)

    def on_post(self, req, resp):
        """Handles POST requests"""
        try:
            #raw_json = req.stream.read()
            raw_json = req.stream.read().decode('utf-8')
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,'Error',ex.message)

        #try:
        #    result = json.loads(raw_json, encoding='utf-8')
        #    print(json.dumps(result))
        #    resp.body = json.dumps(result)
        #except ValueError:
        #    raise falcon.HTTPError(falcon.HTTP_400,'Invalid JSON','Could not decode the request body. The ''JSON was incorrect.')
        os.system('ssh -o StrictHostKeyChecking=no -i /key.rsa chris@puppet "sudo r10k deploy environment -pv"')

api = falcon.API()
api.add_route('/deploy', r10kResource())