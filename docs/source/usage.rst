Usage
=====

.. _installation:

Installation
------------

To use fastTG, first install it using pip:

.. code-block:: console

   (.venv) $ pip install fastTG

Creating recipes
----------------

To load a temporal graph from an edgelist,
you can use the ``ftg.load_graph()`` function:

.. autofunction:: ftg.load_graph()

.. The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
.. or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
.. will raise an exception.

.. .. autoexception:: lumache.InvalidKindError

.. For example:

.. >>> import lumache
.. >>> lumache.get_random_ingredients()
.. ['shells', 'gorgonzola', 'parsley']

