import os
from pathlib import Path

# from environ import Env
# from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

# env = Env()
# env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# load_dotenv()

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-w-ptu-anew1i=!0+e8hj48y28b%=#em%19hd4d(ajn$o8zz)#c"
# SECRET_KEY = env("SECRET_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env("DEBUG", default=False)
DUBUG = os.environ.get("DEBUG", False)

# ALLOWED_HOSTS = list(env("ALLOWED_HOSTS"))
# ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS", "*")]
ALLOWED_HOSTS = ["*"]

# Application definition
MAIN_APPS = [
    "core",
    "magala",
    "accounts",
    "card",
    "api",
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "cities",
    "corsheaders",
    "rest_framework",
    "oauth2_provider",
    # "material",
]


CORE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
]

INSTALLED_APPS = CORE_APPS + THIRD_PARTY_APPS + MAIN_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  ##locale
    "corsheaders.middleware.CorsMiddleware",  ##CORS
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "smartcitycard.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "smartcitycard.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / "locale/",
]

LANGUAGES = (
    ("en", _("English")),
    ("om", _("Afan Oromo")),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# STATIC_ROOT = BASE_DIR / "static"

STATICFILES_DIRS = [
    BASE_DIR / "data/static",
]

# MEDIA_URL = "media/"
# MEDIA_ROOT = BASE_DIR / "data/media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# cities setting
CITIES_DATA_DIR = BASE_DIR / "data/cities"

CITIES_CONTINENT_DATA = {
    "AF": ("Africa", 6255146),
    "AS": ("Asia", 6255147),
    "EU": ("Europe", 6255148),
    "NA": ("North America", 6255149),
    "OC": ("Oceania", 6255151),
    "SA": ("South America", 6255150),
    "AN": ("Antarctica", 6255152),
}
CITIES_CONTINENT_MODEL = "cities.Continent"
CITIES_COUNTRY_MODEL = "magala.SmartCountry"
CITIES_CITY_MODEL = "magala.SmartCity"
CITIES_DISTRICT_MODEL = "magala.SmartDistrict"
CITIES_LOCALES = ["en", "om"]
CITIES_POSTAL_CODES = ["ET"]

# CITIES_FILES = {
#     "city": {
#         "filenames": [
#             "ET.zip",
#         ],
#         "urls": ["http://download.geonames.org/export/dump/" + "{filename}"],
#     },
# }
# CITIES_FILES = {
#     "city": {
#         "filenames": [
#             "allCountries.zip",
#             "alternateNames.zip",
#         ],
#         "urls": ["http://download.geonames.org/export/dump/" + "{filename}"],
#     },
# }


# CORS SETTING
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://localhost:6789",
    "http://127.0.0.1:6789",
]

OAUTH2_PROVIDER = {
    # "OIDC_ENABLED": True,
    # "OIDC_RSA_PRIVATE_KEY": OIDC_KEY,
    "SCOPES": {
        "read": "Read scope",
        "write": "Read write",
        "groups": "Access to your groups",
    },
    # "SCOPES": {"all": "all scopes"},
}

# Rest settings
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.AllowAny",
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ],
}

LOGIN_URL = "/admin/login/"
# LOGIN_URL='/admin/login/'
