import toml
import yaml
from aiogram import Bot, Dispatcher
from data.config import YML_CONF, TML_CONF
from aiogram.client.bot import DefaultBotProperties

TOML = toml.load(TML_CONF)

with open(YML_CONF) as yam:
    YAML = yaml.safe_load(yam)

# [MESSAGES]
admin_messages = TOML['admin_msg']
user_messages = TOML['user_msg']

# [KEYBOARD-TEXT]
common_kb_text = TOML['common_kb']
admin_kb_text = TOML['admin_kb']
user_kb_text = TOML['user_kb']

# [TELEGRAM]
telegram = YAML['telegram']
webhook = telegram['webhook']

ADMIN_ID = telegram['admin_id']
BOT_TOKEN = telegram['bot_token']
WEBHOOK_PATH = f"/bot{BOT_TOKEN}"
WEBHOOK_URL = webhook['url']

# [DATABASE]
database = YAML['database']
DBNAME = database['dbname']
HOST = database['host']
PORT = database['port']
USERNAME = database['username']
PASSWORD = database['password']

print(DBNAME, HOST, PORT, USERNAME, PASSWORD)


roloc_bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()
