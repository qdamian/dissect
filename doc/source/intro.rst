Introduction
============

Example usage
-------------

Given hello.py:

.. literalinclude:: hello.py

We can run it and get info about the function calls:

.. runblock:: pycon

    >>> import dissect
    ... entities = []
    ... dissect.run('hello.py', entities.append)
    ... call = [e for e in entities if e.type == 'FunctionCall']
    ... print len(call)
    ... print call[0].function.name
    ... print call[1].function.name
    ... print call[1].parent.function.name
    ... print call[1].parent == call[0]
    ... print call[0].parent.name
