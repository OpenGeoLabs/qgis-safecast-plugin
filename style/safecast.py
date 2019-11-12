import os

from . import Style

class SafecastStyle(Style):
    def __init__(self):
        super(SafecastStyle, self).__init__()

        stylePath = os.path.join(os.path.dirname(__file__), "safecast")
        self._styles = [
            {'name' : '0.08 - 10.00 microSv/h',
             'file' : os.path.join(stylePath, 'normal.qml')
            },
            {'name' : '0.05 - 200.00 microSv/h',
             'file' : os.path.join(stylePath, 'high.qml')
            }
        ]
