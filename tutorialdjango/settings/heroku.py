import environ
from tutorialdjango.settings.base import *
env = environ.Env()
# abaixo tranforma uma string num bolleano, um casting
DEBUG = env.bool("DEBUG = False")
SECRET_KEY =  env("SECRET_KEY")
ALLOWED_HOSTS =env.list("ALLOWED_HOSTS")
DATABASES = {
    "default": env.db,
}