"""Safecast Reader Library

(C) 2015-2016 by OpenGeoLabs s.r.o.

Read the file LICENCE.md for details.

.. sectionauthor:: Martin Landa <martin.landa opengeolabs.cz>
"""

import os
import csv
from dateutil import tz
from datetime import datetime

from .exception import SafecastReaderError
from .logger import SafecastReaderLogger

class SafecastReader:
    def __init__(self, filename=None):
        """Constructor.

        Check format, version and deadtime.
        
        :param filename: file name to be imported
        """
        self.filename = filename
        self.format_version = None
        self.deadtime = None
        self.header_line = 0
        self.nlines = 0

        if not self.filename:
            raise SafecastReaderError("Input file not defined")

        try:
            self._fd = open(self.filename)
            self.nlines = self._get_count()
            self.header_line = self._read_header()
            self.nlines -= self.header_line
        except (IOError, SafecastReaderError) as e:
            raise SafecastReaderError("{}".format(e))
        
    def __del__(self):
        """Destructor, close input file.
        """
        if self._fd:
            self._fd.close()
        
    def __iter__(self):
        """Iterate items in row.

        Skip commented lines (#).

        :return: list of processed items
        """
        return csv.reader(filter(lambda row: row[0]!='#', self._fd))
    
    def _read_header(self):
        """Read LOG header and store metadata items.
        """
        # TODO: be less pedantic
        def _read_header_line(line, header_line):
            line = line.rstrip('\r\n')
            if header_line == 0 and line != "# NEW LOG":
                raise SafecastReaderError("Unable to read '{}': "
                                          "Invalid format".format(self.filename))
            elif header_line == 1 : # -> version
                if not line.startswith('# format'):
                    raise SafecastReaderError("Unable to read '{}': "
                                              "Unknown version".format(self.filename))
                else:
                    self.format_version = line.split('=')[1]
            elif header_line == 2: # -> deadtime
                if not line.startswith('# deadtime'):
                    raise SafecastReaderError("Unable to read '{}': "
                                              "Unknown deadtime".format(self.filename))
                else:
                    self.deadtime = line.split('=')[1]

        header_line = 0
        self._fd.seek(0, 0)
        for line in self._fd:
            if line.startswith('#'):
                _read_header_line(line, header_line)
                header_line += 1
            if header_line == 3:
                SafecastReaderLogger.debug("LOG header correct\n")
                break

        return header_line

    def _get_count(self):
        """Get number of lines.

        Inspired by http://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python.
        """
        self._fd.seek(0, 0)
        lines = 0
        buf_size = 1024 * 1024
        read_f = self._fd.read # loop optimization

        buf = read_f(buf_size)
        while buf:
            lines += buf.count('\n')
            buf = read_f(buf_size)

        return lines

    def count(self):
        """Return number of lines."""
        return self.nlines
