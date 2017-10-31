# -*- coding: utf-8 -*-
""" Create the Blueprints for the api routes.
We use a factory function to create the Blueprints and add those to
a global variable all_blueprints
"""
from flask import Blueprint
from flask import abort, render_template

import logging

log = logging.getLogger()


def _factory(partial_module_string, url_prefix):
    """Generates blueprint objects for view modules.

    Args:
        partial_module_string (str): string representing a view module
        without the absolute path.

        url_prefix (str): URL prefix passed to the blueprint.

    Returns:
        Blueprint. Blueprint instance for a view module.

    """
    name = partial_module_string
    import_name = 'api.views.{}'.format(partial_module_string)
    template_folder = 'templates'
    blueprint = Blueprint(name, import_name, template_folder=template_folder, url_prefix=url_prefix)
    return blueprint

bp_main = _factory('home.index', '')
bp_customer = _factory('customers.index', '/customers')
bp_errors = Blueprint('errors', __name__)


"""Error views: register the error pages"""
@bp_errors.app_errorhandler(400)
def handle_400(err):
    """Generate error 400 Bad Request"""
    logging.debug("400 Bad Request error")
    return render_template('400.html'), 400

@bp_errors.app_errorhandler(403)
def handle_403(err):
    """Generate error 403 Forbidden"""
    logging.debug("403 Forbidden error")
    return render_template('403.html'), 403

@bp_errors.app_errorhandler(404)
def handle_404(err):
    """Generate 404 Not found"""
    logging.debug("404 Not found error")
    return render_template('404.html'), 404

@bp_errors.app_errorhandler(500)
def handle_500(err):
    """Generate 500 Internal Server Error"""
    logging.debug("500 Internal Server Error error")
    return render_template('500.html'), 500


all_blueprints = (bp_main, bp_customer, bp_errors)
"""list: list of all Blueprints."""
