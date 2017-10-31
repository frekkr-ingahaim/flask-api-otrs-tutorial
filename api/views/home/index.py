# -*- coding: utf-8 -*-
from api.blueprints import bp_main

from flask import render_template, jsonify, request, current_app, abort

import logging
import os

log = logging.getLogger()

@bp_main.route('/', methods=['GET'])
def index():
    """Back-end index page. Use the search submenu to see an example of
    the JSON data returned.

    Returns:
        The rendered index page

    """
    return render_template("index.html")


"""The following functions are meant to show you how the debug
functionality of Werkzeug works, and how you can return certain http
status codes. These codes are then handled by the functions specified
in blueprint.py

"""

@bp_main.route('/debug')
def debug():
    """Test the debugging in the application. Should provide a nice
    traceback

    """
    log.debug("Debug view reached")
    assert current_app.debug == False, "Don't panic! You're here by request of debug()"



@bp_main.route('/exception')
def exception():
    """Test the debugging in the application. Should provide a nice
    traceback for a generated exception

    """
    log.debug("Exception view reached")
    raise Exception("Exception caught. Provide some meaningful text.")


@bp_main.route('/error')
def error():
    """Test the error handling of an internal server error (400 http
    status code.

    """
    log.debug("Error view reached")
    return abort(500)


@bp_main.route('/invalid')
def invalid():
    """Test the error handling of an invalid request (400 http status
    code.

    """
    log.debug("Invalid view reached")
    return abort(400)


@bp_main.route('/forbidden')
def forbidden():
    """Test the error handling of an forbidden request (403 http status
    code.

    """
    log.debug("Forbidden view reached")
    return abort(403)
