import os
import sys

from django.core.wsgi import get_wsgi_application

# Ensure project path is on sys.path
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.append(ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tela.settings')
application = get_wsgi_application()
