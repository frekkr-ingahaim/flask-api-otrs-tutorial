Flask REST API for OTRS Tutorial
================================

The code is meant to show you how to create a REST API with flask.
I chose to build an interface to OTRS and this project could serve as a
start to create a REST API to access OTRS. Yes, OTRS does have it's own
webservices but this is meant as a tutorial.

Since this is a Flask REST API tutorial, please view it as such and not
as a production type of code. Following improvements are possible:

* Use SQLAlchemy so you can switch to another database for production and
  maybe use SQLite just for testing
* Serve documentation with Nginx/Apache instead of via a Blueprint
* Add more tests to the code
* Measure code coverage with test coverage metrics
* Expand the API with more methods besides a few get API functions.
  A full REST API could include get, post, put and delete functionality
* Provide some means of credential checking (login)
* Change the project layout depending on the scale of your project
* Check your code for style consistency or style guides provided by your
  employer
  
This code is meant as a starting point to show how you could develop
a REST API in Flask/Python. The code as it is, is not meant for production.

Documentation
-------------
The code is documented, and api docs are generated with Sphinx.
If you start the application you'll be able to access the documentation
from the menu @ http://localhost:5000.

Quickstart
----------
You will need to install all the dependencies from the requirements.txt
file with pip in a virtualenv directory.
After you have cloned the code via git, you'll need to set-up a virtualenv
using Python 3. Create a directory and set-up the virtualenv::

    $ git clone <repository url>
    $ cd flask-api-otrs-tutorial
    $ mkdir venv
    $ python3 -m "venv" venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

Create a local config.py file::

    $ touch instance/config.py

You start the application via the manage.py script::

    $ python manage.py

Flask will run on http://localhost:5000.
You can visit this website (back-end) to learn more and see some basic calls.

Tests
-----
Some basic testing is provided in the tests folder. Just enough testing
to show you how you could test your REST API.
To run the test from the project root::

    $ python -m "unittest" discover

Help
----
If you find errors in the code or have some suggestions, you can drop
me `a line <mailto:tutorial@ictforce.be>`_. 
An article on this project should be published on `my site <https://www.ictforce.be>`_.

License
-------
Distributed under the MIT license, see LICENSE file for the full text.
