Pyramid Switchboard Demo App
==============================

Demonstration application for the Pyramid Switchboard add on.

Running the Demo
----------------

- Create a virtualenv::

    $ virtualenv2.6 --no-site-packages /path/to/my/venv

  Hereafter ``/path/to/my/venv`` will be referred to as $VENV in steps
  below.

- Get a checkout of pyramid_switchboard::

    $ git clone git://github.com/switchboardpy/pyramid_switchboard.git

- ``cd`` to the newly checked out pyramid_switchboard package::

    $ cd pyramid_switchboard

- Run ``setup.py develop`` using the virtualenv's ``python`` command::

    $ $VENV/bin/python setup.py develop

- While your working directory is still ``pyramid_switchboard``, cd to the
  ``demo`` directory and run *its* ``setup.py develop``::

    $ cd demo
    $ $VENV/bin/python setup.py develop


- Start the demo application::

    $ $VENV/bin/python demo.py

- Visit http://localhost:8080 in a browser to see the demo.
