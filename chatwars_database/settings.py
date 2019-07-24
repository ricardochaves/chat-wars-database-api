"""
Django settings for chatwars_database project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import json
import os

import requests
from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate

from chatwars_database.conf import S_ALLOWED_HOSTS
from chatwars_database.conf import S_DATABASES
from chatwars_database.conf import S_DEBUG
from six.moves.urllib import request

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "vm@9(w*68!!+=s#x4ng*t8%(41$u98$6%khl!@4b1ybj6s-r3q"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = S_ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "database",
    "rest_framework",
    "django_filters",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.RemoteUserMiddleware",
]

ROOT_URLCONF = "chatwars_database.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "chatwars_database.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = S_DATABASES

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "chatwarsdatabase/static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "chatwarsdatabase/media")

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "django.contrib.auth.backends.RemoteUserBackend",
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

AUTH0_DOMAIN = "ricardobaltazar.auth0.com"
API_IDENTIFIER = "https://chatwarsdatabase.ricardobaltazar.com"

PUBLIC_KEY = None
JWT_ISSUER = None

# If AUTH0_DOMAIN is defined, load the jwks.json
if AUTH0_DOMAIN:
    import logging

    logging.warning("EXECUTANDO CERTIFICADO")
    response = requests.get("https://" + AUTH0_DOMAIN + "/.well-known/jwks.json", timeout=1)
    jwks = response.json()
    cert = "-----BEGIN CERTIFICATE-----\n" + jwks["keys"][0]["x5c"][0] + "\n-----END CERTIFICATE-----"
    certificate = load_pem_x509_certificate(cert.encode("utf-8"), default_backend())
    PUBLIC_KEY = certificate.public_key()
    JWT_ISSUER = "https://" + AUTH0_DOMAIN + "/"


JWT_AUTH = {
    "JWT_PAYLOAD_GET_USERNAME_HANDLER": "drf.user.jwt_get_username_from_payload_handler",
    "JWT_PUBLIC_KEY": PUBLIC_KEY,
    "JWT_ALGORITHM": "RS256",
    "JWT_AUDIENCE": API_IDENTIFIER,
    "JWT_ISSUER": JWT_ISSUER,
    "JWT_AUTH_HEADER_PREFIX": "Bearer",
}


CORS_ORIGIN_WHITELIST = ["http://localhost:3000", "https://chatwars-database-web.ricardobchaves6.now.sh"]
CORS_ORIGIN_REGEX_WHITELIST = [r"^https://chatwars-database-web-.*.now.sh$"]
