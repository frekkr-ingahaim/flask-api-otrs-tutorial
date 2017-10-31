# -*- coding: utf-8 -*-
from flask import Flask

from config.default import config
from api.blueprints import all_blueprints

from importlib import import_module
import logging


def create_app(config_name="default"):
    """Create the flask app::
    
        - load the default config
        - load a local config if present
        - register the blueprints
        - setup the logger
        - log the routes
        
    Args:
        config_name (str): configuration to load
        
    Returns:
        The Flask object
        
    """ 
    app = Flask(__name__, instance_relative_config=True)
    
    # Load the default configuration    
    app.config.from_object(config[config_name])

    # Load the configuration from the instance folder if one exists
    app.config.from_pyfile('config.py', silent=True)

    # Register favicon
    app.add_url_rule('/favicon.ico', 'favicon', lambda: app.send_static_file('favicon.ico'))
    
    # Register the blueprints
    for bp in all_blueprints:    
        import_module(bp.import_name)
        app.register_blueprint(bp)
    return app
