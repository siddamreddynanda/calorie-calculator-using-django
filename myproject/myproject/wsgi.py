import os
from django.core.wsgi import get_wsgi_application

# Make sure this matches your project configuration name exactly!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()