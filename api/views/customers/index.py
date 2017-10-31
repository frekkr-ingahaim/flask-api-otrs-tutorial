# -*- coding: utf-8 -*-
from api.blueprints import bp_customer

from flask import render_template, jsonify, request, Response, current_app

from datetime import datetime, timedelta

"""If using a Postgres database, uncomment the following line and
comment the sqlite3 line.

"""
# import psycopg2
import sqlite3
import logging

log = logging.getLogger()

customer_fields = [
    "customer_id",
    "name",
    "street",
    "zip",
    "city",
    "country",
    "url",
    "comments",
    "valid_id",
    "create_time",
    "create_by",
    "change_time",
    "change_by" ]
"""This list of fields is a match for the table columns of the
customer_company table in OTRS. For this tutorial, the tables was
creatin in SQLite.

"""

@bp_customer.route("/")
def get_customers():
    """Used to return a list of customers filtered on the search parameter
    Gets the search value from the request. You can manually add the search
    part by including '?search=<searchterm>' after the /customers/ link.

    Returns:
        Returns a 'Response' object containing the list of customers.

    """
    search = request.args.get('search')
    log.debug("Searching '{}'".format(search))
    customer = _get_customers(search)
    if customer is not None and len(customer) > 0:
        cust = [ cust_t[0] for cust_t in customer]
        log.debug(cust)
    else:
        cust = None
    resp = jsonify(cust)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

@bp_customer.route("/info")
def get_customer_info():
    """Get the info of a customer. Expects a complete customer name
    Gets the search value from the request. You can manually add the search
    part by including '?search=<searchterm>' after the /customers/info/ link.

    Returns:
        Returns a 'Response' object containing a dictionary with the company information

    """
    customer = request.args.get('search')
    log.debug("Searching '{}'".format(customer))
    cust_info = _get_customer_info(customer)

    if cust_info is not None and len(cust_info) == 1:
        log.debug("Customer data found")
        cust_d = dict(zip(customer_fields, *cust_info))
    else:
        log.debug("No customer data found or more than one possible client.")
        cust_d = None

    resp = jsonify(cust_d)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


def _execute_sql(sql):
    """Helper function to execute the SQL commands. We use SQLite but
    the code is easily changed to connect to another database such as
    PostgreSQL. If you want to use a Postgres database, you need to set
    the following vars in instance/config or change them in class
    Config. They need to be loaded on the program start::

        DATABASE_NAME - dbname: the database name (database is a deprecated alias)
        DATABASE_USER - user: user name used to authenticate
        DATABASE_PASSWORD - password: password used to authenticate
        DATABASE_HOST - host: database host address (defaults to UNIX socket if not provided)
        DATABASE_PORT - port: connection port number (defaults to 5432 if not provided)

    An exception can occur When the connection to the database fails or
    executing the SQL produces an error.

    """
    try:
        """
        # Uncomment this block of code if you want to use PostgreSQL and have set the correct
        # settings in instance/config.py. The settings are used to create the CON_PARAM dictionary
        # for the connect function.
        # For testing reason, these settings are also logged to console & file, so if using this in a
        # production environment, please do not use the 2 logging lines to prevent writing these in cleartext
        CON_PARAM = { 'dbname': current_app.config['DATABASE_NAME'],
                      'user': current_app.config['DATABASE_USER'],
                      'password': current_app.config['DATABASE_PASSWORD'],
                      'host': current_app.config['DATABASE_HOST'],
                      'port': current_app.config['DATABASE_PORT']
        }
        # Only uncomment these lines if you're not trying to connect to a production database!
        # log.debug("DEBUG = {}".format(current_app.config['DEBUG']))
        # log.debug("CON_PARAM {}".format(CON_PARAM))
        """

        """Connect to the test database. If using a Postgres database,
        uncomment the following line.

        """
        # conn = psycopg2.connect(**CON_PARAM)
        conn = sqlite3.connect(current_app.config['DATABASE'])

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Run sql
        cur.execute(sql)
        res = cur.fetchall()
        return res
    except Exception as e:
        log.error("execute_sql(): error while connecting to the database or executing the sql")
        log.error(str(e))
    finally:
        # Close communication with the database
        cur.close()
        conn.close()


def _get_customers(name):
    """Search the database for customers who's name contains 'name'.

    Args:
        name (str): Name or part of the name to filter the customers

    Returns:
        Return a tuple of customers filtered on the name (part)

    """

    sql="""select customer_id
    from customer_company
    where LOWER(customer_id) like LOWER('%{}%')""".format(name)
    return _execute_sql(sql)


def _get_customer_info(customer):
    """Retrieve the customer info

    Args:
        customer (str): Name of the customer

    Returns:
        Return a list of customers filtered on the customer name

    """

    sql="""select *
    from customer_company
    where LOWER(customer_id) like LOWER('%{}%')""".format(customer)
    return _execute_sql(sql)
