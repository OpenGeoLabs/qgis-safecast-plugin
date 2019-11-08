from .exceptions import ReaderError

class ReaderBase:
    """Base reader class.
    """
    def __init__(self, filepath, rb=False):
        self._filepath = filepath

        try:
            flag = 'rb' if rb else 'r'
            self._fd = open(self._filepath, flag)
        except IOError as e:
            raise ReaderError("{}".format(e))

    def __del__(self):
        """Destructor, close input file.
        """
        if self._fd:
            self._fd.close()

    def count(self):
        """Count data items.
        """
        raise NotImplementedError()

    def _next_data_item(self):
        """Read next data item.
        """
        raise NotImplementedError()

    def __iter__(self):
        """Loop through features.
        """
        self._reset()
        return self

    def __next__(self):
        """Return next QgsFeature.
        """
        item = self._next_data_item()
        if not item:
            raise StopIteration

        return item

    def _reset(self):
        """Reset reading.
        """
        self._fd.seek(0, 0)

    def _count(self, counter):
        """Count data items.

        Inspired by http://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python.

        :param counter: counter string
        """
        self._reset()

        lines = 0
        buf_size = 1024 * 1024
        read_f = self._fd.read # loop optimization

        buf = read_f(buf_size)
        while buf:
            lines += buf.count(counter)
            buf = read_f(buf_size)

        return lines

    def attributeDefs(self):
        """Get attribute definitions from file.
        """
        return None
