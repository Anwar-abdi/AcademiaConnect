import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ucu_chapters.settings.production')

application = get_wsgi_application()
