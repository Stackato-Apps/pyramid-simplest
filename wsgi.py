from pyramid.config import Configurator
from pyramid.response import Response
from paste.httpserver import serve
import os

def hello_world(request):
    return Response('Hello world!')

def goodbye_world(request):
    return Response('Goodbye world!')

config = Configurator()
config.add_view(hello_world)
config.add_view(goodbye_world, name='goodbye')
application = config.make_wsgi_app()
port = os.environ['PORT']
serve(application, host='0.0.0.0', port=port)
