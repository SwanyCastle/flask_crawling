import yaml

mysql_uri = ""
mykey = ""

with open("key.yaml", "r") as f:
    key = yaml.load(f, Loader=yaml.FullLoader)
    mysql_uri = key["mysql_uri"]
    mykey = key["mykey"]

SQLALCHEMY_DATABASE_URI = mysql_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

API_TITLE = "CRAWL API"
API_VERSION = "v1"
OPENAPI_VERSION = "3.1.3"
OPENAPI_URL_PREFIX = "/"
OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

SECRET_KEY = mykey