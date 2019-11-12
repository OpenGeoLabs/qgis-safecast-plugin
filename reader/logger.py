"""Reader Library

(C) 2015-2019 by OpenGeoLabs s.r.o.

Read the file LICENCE.md for details.

.. sectionauthor:: Martin Landa <martin.landa opengeolabs.cz>
"""
from builtins import str
from builtins import range
from builtins import object

import os
import logging
from future.utils import with_metaclass

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = list(range(8))

RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"

def formatter_message(message, use_color = False):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message

COLORS = {
    'WARNING': MAGENTA,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED
}

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in list(cls._instances.keys()):
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color = False):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        if self.use_color and record.levelname in COLORS:
            name_color = COLOR_SEQ % (30 + COLORS[record.levelname]) + '[' + record.name # + RESET_SEQ
            record.name = name_color
            record.msg += RESET_SEQ
        return logging.Formatter.format(self, record)

class ColoredLogger(logging.Logger):
    FORMAT = "[%(name)s][%(levelname)s] %(message)s"
    COLOR_FORMAT = formatter_message(FORMAT, True)
    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.DEBUG)
        self.propagate = False

        color_formatter = ColoredFormatter(self.COLOR_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)
        self.addHandler(console)

        return

class LoggerManager(with_metaclass(Singleton, object)):
    _loggers = {}

    def __init__(self, *args, **kwargs):
        logging.setLoggerClass(ColoredLogger)

    @staticmethod
    def getLogger(name=None):
        if not name:
            logging.basicConfig()
            return logging.getLogger()
        elif name not in list(LoggerManager._loggers.keys()):
            logging.basicConfig()
            LoggerManager._loggers[name] = logging.getLogger(str(name))
        return LoggerManager._loggers[name]

ReaderLogger=LoggerManager().getLogger("RadiationToolboxImporter")
