# -*- coding=UTF-8 -*-
"""Disable nuke crash handling.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


def _main():
    import logging
    import os
    import subprocess
    import sys
    from six.moves import configparser

    __dirname__ = os.path.abspath(os.path.dirname(__file__))

    config = configparser.SafeConfigParser()
    config.optionxform = unicode
    config.read([os.path.join(__dirname__, 'config.ini')])

    def _set_env(key, value):
        if os.getenv(key) == value:
            return
        if sys.platform == 'win32':
            subprocess.call(['setx', key, value])
        os.environ[key] = value
        logging.debug('Set enviroment variable: %s = %s', key, value)

    for k, v in config.items('env'):
        _set_env(k, v)

    logging.info('Disabled nuke crash handling.')


if __name__ == '__main__':
    _main()

del _main
