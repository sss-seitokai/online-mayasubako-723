import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'django-insecure-%cqnj&mh!1&z!w-$aj9nfn5dnnw#=g7dr(&0&2jan66(&m%ycu'

DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.sqlite3',
 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 }
}
DEBUG = False