import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

S_DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.getenv("DB_USER"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

S_DEBUG = True

S_ALLOWED_HOSTS = ["*"]
