from datetime import datetime
import sys
from termcolor import colored
from emoji import emojize

class Logger:

    def log(level, msg):
        level_color_mapping = {
            "info": 'green',
            "error": 'red',
        }
        prefix_mapping = {
            "info": 'info',
            "error": 'error'
        }
        emoji_mapping = {
            "info": emojize(":check_mark_button:"),
            "error": emojize(":cross_mark:")
        }
        emoji = emoji_mapping[level]
        prefix = prefix_mapping[level]
        fg_color = level_color_mapping[level]
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
