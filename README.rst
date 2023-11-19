================
pytest-skipuntil
================

.. image:: https://img.shields.io/pypi/v/pytest-skipuntil.svg
    :target: https://pypi.org/project/pytest-skipuntil
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-skipuntil.svg
    :target: https://pypi.org/project/pytest-skipuntil
    :alt: Python versions

.. image:: https://ci.appveyor.com/api/projects/status/github/bp72/pytest-skipuntil?branch=master
    :target: https://ci.appveyor.com/project/bp72/pytest-skipuntil/branch/master
    :alt: See Build Status on AppVeyor

A simple pytest plugin to skip the tests with deadline in a simple way

----

Features
--------

* Use this marker to specify the deadline for the skip: a convenient decorator to prevent skipping tests and never going back to fix them. When the deadline is behind, the test will start failing again.


Requirements
------------

* pytest
* python>=3.8


Installation
------------

You can install "pytest-skipuntil" via `pip`_ from `PyPI`_::

    $ pip install pytest-skipuntil

Usage
-----

* Use it as a decorator for the test that you want to skip::


    @pytest.mark.skip_until(
        deadline=datetime(2023, 12, 11),
        msg='This test requires a fix, but I can't do it right now :('
    )
    def test_something():
        ...

The test will be skipped until 11/12/2023, but it will start failing again after this date, so you'll be
reminded to make a fix.


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-skipuntil" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/bp72/pytest-skipuntil/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
