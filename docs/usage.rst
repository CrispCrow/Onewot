Getting Started
===============

Installation
------------
Install Onewot from PyPi with the following command:

.. code-block:: bash

	python -m pip install -U onewot
	# Windows users may need to use this instead...
	py -3 -m pip install -U onewot

----

Updating
--------

.. code-block:: bash

	pip install --upgrade onewot

----

Start up client
---------------

.. code-block:: python

	import onewot

	client = onewot.WOTBClient(application='...')

----

Example
-------

.. code-block:: python

	import onewot

	client = onewot.WOTBClient(application='...', language=onewot.Language.ENGLISH)

	print(client.fetch_user(152870490))
