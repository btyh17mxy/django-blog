import sys
import pylibmc
sys.modules['memcache'] = pylibmc
import sae
from selfblog import wsgi
import os

app_root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(app_root, 'virtualenv.bundle'))
application = sae.create_wsgi_app(wsgi.application)
