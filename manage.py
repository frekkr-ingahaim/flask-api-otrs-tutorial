#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" **Module summary**: Very basic management script for the Flask API
OTRS Tutorial. In a real app, you would register commands to further
automate your work. Check out the Flask-Script, Flask-Runner or the
Flask command line interface (CLI) new in version 0.11.

"""
from api import create_app

import logging
import logging.handlers
import os
import sys
import urllib

from flask import current_app
from flask_debugtoolbar import DebugToolbarExtension

"""Create the application and display the Werkzeug debug toolbar.
The debug toolbar is only enabled in debug mode.

"""
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
toolbar = DebugToolbarExtension(app)

"""By default, the main function is going to get loaded twice.
This is due to the Werkzeug reloader. It spawns a child process so it
can restart the process each time a code changes is detected. This is
actually very handy while developing.
If you want to change this behaviour, uncomment the following line.

"""
#app.debug = False


def setup_logging(log_basedir="logs"):
    """Setup logging. We will log al info into a rotating file log.

    Args:
        log_basedir (str): base/parent directory for the logfiles

    """
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    LOGDIR = os.path.join(BASEDIR,log_basedir)
    
    # Check if the logs directory exists and is writable
    if not os.path.isdir(LOGDIR):
        print('ERROR: Log directory {} does not exist.'.format(LOGDIR))
        sys.exit(1)
    if not os.access(LOGDIR, os.W_OK):
        print('ERROR: No permissions to write to log directory {}.'.format(LOGDIR))
        sys.exit(1)

    # Set the log message format
    fmt = '%(levelname)s - %(asctime)s.%(msecs).03d %(process)d [%(filename)s:%(lineno)d] %(message)s'
    datefmt = '%m%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt)

    # Log to console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    root.addHandler(console_handler)

    # Log to file, use a rotating file
    file_name = os.path.join(LOGDIR, '{}.log'.format("flask_api_otrs") )

    file_handler = logging.handlers.RotatingFileHandler(file_name, backupCount=7)
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)


def list_routes(app):
    """List the registered routes for the app

    Args:
        app (Flask): Flask object

    Returns:
        output (list): List of registered urls

    """
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    return sorted(output)


if __name__=="__main__":
    """ Create logs and instance folder """
    try:
        for _dir in ["logs", "instance"]:
            if not os.path.exists(_dir):
                os.mkdir("logs")
    except Exception as e:
        pass
    
    """Create a logger."""
    setup_logging()
    log = logging.getLogger()

    log.info("-- Registered routes")
    for route in list_routes(app):
        log.info("Route {}".format(route))

    log.info("-- Running application ---")
    app.run()

