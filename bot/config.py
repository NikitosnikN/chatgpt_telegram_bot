from pathlib import Path

import yaml

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# config parameters
telegram_token = config_yaml["telegram_token"]
openai_api_key = config_yaml["openai_api_key"]
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"] or []
new_dialog_timeout = int(config_yaml["new_dialog_timeout"])
mongodb_uri = config_yaml["mongodb_uri"]
mongodb_db_name = config_yaml["mongodb_db_name"]
