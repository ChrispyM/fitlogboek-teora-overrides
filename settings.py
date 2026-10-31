"""Teora-laag boven op wger: eigen templates en vertalingen, zonder wger-bestanden aan te raken."""
from settings.main import *  # noqa: F401,F403

TEORA_DIR = '/home/wger/src/teora'
TEMPLATES[0]['DIRS'] = [f'{TEORA_DIR}/templates']  # noqa: F405
LOCALE_PATHS = (f'{TEORA_DIR}/locale', *LOCALE_PATHS)  # noqa: F405
