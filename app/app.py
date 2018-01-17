#app.py
import falcon
import json

class r10kResource:
 
    def on_get(self, req, resp):
        """Handles GET requests"""
        result = {'error': 'invalid request'}
        resp.body = json.dumps(result)

    def on_post(self, req, resp):
         """Handles POST requests"""
         try:
             raw_json = req.stream.read()
         except Exception as ex:
             raise falcon.HTTPError(falcon.HTTP_400,'Error',ex.message)

         try:
             result = json.loads(raw_json, encoding='utf-8')
             sid =  r.db(PROJECT_DB).table(PROJECT_TABLE).insert({'title':result['title'],'body':result['body']}).run(db_connection)
             resp.body = 'Successfully inserted %s'%sid
         except ValueError:
             raise falcon.HTTPError(falcon.HTTP_400,'Invalid JSON','Could not decode the request body. The ''JSON was incorrect.')

api = falcon.API()
api.add_route('/deploy', r10kResource())