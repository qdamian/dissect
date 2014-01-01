.. image:: https://travis-ci.org/qdamian/dissect.png?branch=master
  :target: https://travis-ci.org/qdamian/dissect

.. image:: https://coveralls.io/repos/qdamian/dissect/badge.png?branch=master
  :target: https://coveralls.io/r/qdamian/dissect?branch=master


dissect
=======

This library is meant to be used by `depict`_.

It uses `astroid`_ to represent the source code of the program in a tree structure (package -> module -> class -> function -> block -> line).

It uses the standard library `tracer`_ to represent the program execution in a tree structure (thread -> function call -> function call).

And it relates the two trees (function call -> function).

Contact
-------

Feel free to email me at qdamian@gmail.com

---

Copyright 2014, Damian Quiroga

.. _depict: https://github.com/qdamian/depict
.. _astroid: https://bitbucket.org/logilab/astroid
.. _tracer: http://docs.python.org/2/library/sys.html#sys.settrace
