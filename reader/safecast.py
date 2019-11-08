"""Safecast Reader Library

(C) 2015-2019 by OpenGeoLabs s.r.o.

Read the file LICENCE.md for details.

.. sectionauthor:: Martin Landa <martin.landa opengeolabs.cz>
"""
from builtins import object

import os
import csv
from dateutil import tz
from datetime import datetime

from .exceptions import ReaderError
from .logger import ReaderLogger
from . import ReaderBase

class SafecastReader(ReaderBase):
    """Reader class for reading Safecast format (LOG files).
    """
    def __init__(self, filepath):
        """Constructor.

        Check format, version and deadtime.
        
        :param filepath: file name to be imported
        """
        self.format_version = None
        self.deadtime = None
        self.nlines = 0

        try:
            super(SafecastReader, self).__init__(filepath)
            self.nlines = self._count('\n')
            self.nlines -= self._read_header()
        except (IOError, ReaderError) as e:
            raise ReaderError("{}".format(e))
        
    def _next_data_item(self):
        """Read next data item.
        """
        while True:
            line = self._fd.readline().rstrip(os.linesep)
            if not line:
                # EOF
                return None
            if not line.startswith('#'):
                return list(csv.reader([line]))[0]

    def _read_header(self):
        """Read LOG header and store metadata items.
        """
        # TODO: be less pedantic
        def _read_header_line(line, header_line):
            line = line.rstrip('\r\n')
            if header_line == 0 and line != "# NEW LOG":
                raise ReaderError("Unable to read '{}': "
                                  "Invalid format".format(self.filename))
            elif header_line == 1 : # -> version
                if not line.startswith('# format'):
                    raise ReaderError("Unable to read '{}': "
                                      "Unknown version".format(self.filename))
                else:
                    self.format_version = line.split('=')[1]
            elif header_line == 2: # -> deadtime
                if not line.startswith('# deadtime'):
                    raise ReaderError("Unable to read '{}': "
                                      "Unknown deadtime".format(self.filename))
                else:
                    self.deadtime = line.split('=')[1]

        header_line = 0
        self._reset()
        for line in self._fd:
            if line.startswith('#'):
                _read_header_line(line, header_line)
                header_line += 1
            if header_line == 3:
                ReaderLogger.debug("LOG header correct\n")
                break

        return header_line

    def count(self):
        """Get data item count.
        """
        return self.nlines
