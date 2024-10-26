import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "AvishkarPatil")
      ADMINS = [int(admin_id) for admin_id in os.getenv("ADMINS", "").split(",") if admin_id.isdigit()]
