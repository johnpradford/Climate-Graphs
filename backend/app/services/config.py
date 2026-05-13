from pathlib import Path

import yaml


CONFIG_PATH = (
    Path(__file__).resolve().parents[2]
    / 'config/settings.yaml'
)


with open(CONFIG_PATH, 'r', encoding='utf-8') as file:
    SETTINGS = yaml.safe_load(file)
