import json

with open("dev.json") as config_file:
        CONF = json.load(config_file)


API_NAME = CONF["application.name"]

SECRET_KEY = CONF["auth.config"]["secret_key"]
UUID_LEN = CONF["auth.config"]["uuid_len"]
UUID_ALPHABET = ''.join(map(chr, range(48, 58)))
TOKEN_EXPIRES = CONF["auth.config"]["toek_expires"]

DATABASE = CONF["database.config"]

DB_CONFIG = (DATABASE["user"], DATABASE["password"], DATABASE["host"], DATABASE["database"])
DATABASE_URL = "postgresql+psycopg2://%s:%s@%s/%s" % DB_CONFIG

DB_ECHO = True if DATABASE['echo'] == "yes" else False
DB_AUTOCOMMIT = True if DATABASE['autocommit'] == "yes" else False
DB_POOL_RECYCLE = DATABASE["pool_recycle"]
DB_POOL_SIZE = DATABASE["pool_size"]
DB_POOL_TIMEOUT = DATABASE["pool_timeout"]
DB_POOL_MAX_OVERFLOW = DATABASE["max_overflow"]

LOG_LEVEL = CONF['logging']['level']