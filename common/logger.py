from datetime import datetime
import sys
from termcolor import colored
from emoji import emojize

class Logger:

    def log(level, msg):
        level_info_mapping = {
            "info": {
                "color": "green",
                "prefix": "info",
                "emoji": emojize(":check_mark_button:"),
            },
            "error": {
                "color": "red",
                "prefix": "error",
                "emoji": emojize(":cross_mark:"),
            }
        }
        level_info = level_info_mapping[level]
        fg_color = level_info["color"]
        prefix = level_info["prefix"]
        emoji = level_info["emoji"]
        now = datetime.now()
        date = now.strftime("%d/%b/%Y %H:%M:%S")
        msg = colored(msg, fg_color)
        colored_prefix = colored(prefix, fg_color)
        print(f'[{date}] {emoji} [{colored_prefix}]: {msg}')

    @classmethod
    def info(cls, msg):
        Logger.log('info', msg)

    @classmethod
    def error(cls, msg):
        Logger.log('error', msg)
