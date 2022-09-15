import os
from django.core.wsgi import get_wsgi_application
# from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
# application = WhiteNoise(application, root="/path/to/static/files")
application = get_wsgi_application()
