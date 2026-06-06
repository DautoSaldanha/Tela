import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()  # carrega o .env automaticamente

BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança: sem fallback inseguro em produção
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    if os.environ.get('DEBUG', 'False') == 'True':
        SECRET_KEY = 'django-insecure-dev-only-key'
    else:
        raise ValueError("SECRET_KEY não definida nas variáveis de ambiente!")

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['.vercel.app', '.now.sh', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',        # painel admin
    'django.contrib.auth',         # autenticação/usuários
    'django.contrib.contenttypes', # já estava
    'django.contrib.sessions',     # sessões de login
    'django.contrib.messages',     # mensagens flash
    'django.contrib.staticfiles',  # já estava
    'app_tela',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # novo
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # novo
    'django.contrib.messages.middleware.MessageMiddleware',     # novo
]

ROOT_URLCONF = 'Tela.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',      # novo
                'django.contrib.messages.context_processors.messages',  # novo
            ],
        },
    },
]

WSGI_APPLICATION = 'Tela.wsgi.application'

# Banco de dados: DATABASE_URL tem prioridade (produção/Vercel)
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    import dj_database_url  # vai lançar ImportError claro se não instalado
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    # Desenvolvimento local via docker-compose
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['POSTGRES_DB'],        # erro explícito se faltar
            'USER': os.environ['POSTGRES_USER'],
            'PASSWORD': os.environ['POSTGRES_PASSWORD'],
            'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
            'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        }
    }

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'