import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6341371655:AAHhD8n-n4geT_LzNo8Dce_g3GQ2-qsyJnM")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25405632"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "310460a5a086393880bb37883b411fe7")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7147986990"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://felixyumnam7:<GmmgNy535q10Dt82>@cluster0.cdtopqz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "felixyumnam7")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
