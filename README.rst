===============================
pc4BIMS : Pack Circles for BIMS
===============================

.. |made-with-python| image:: https://img.shields.io/badge/Made%20with-Python-brightgreen.svg?style=flat-square
   :target: https://www.python.org/

.. |PyPI| image:: https://img.shields.io/pypi/v/pc4bims.svg
   :target: https://pypi.python.org/pypi/pc4bims

.. |License| image:: https://img.shields.io/badge/License-BSD%202--Clause-brightgreen.svg?style=flat-square
   :target: https://github.com/aarizat/FiguresInRTD/blob/master/LICENS

.. |docs| image:: https://readthedocs.org/projects/pc4bims/badge/?version=latest
   :target: https://pc4bims.readthedocs.io/en/latest/?badge=latest

.. |orcid| image:: https://img.shields.io/badge/id-0000--0003--0619--8735-brightgreen.svg?style=flat-square
   :target: https://orcid.org/0000-0003-0619-8735

|made-with-python| |PyPI| |docs| |License| |ORCID|

``pc4bims`` is an application software in **Python 3** to create circle packing
in arbitrary polygons.


.. figure:: https://rawgit.com/aarizat/pc4bims/master/figures/Figure_1.svg
        :alt: plot example1


Features
--------

* Free software: `BSD-2-Clause <https://opensource.org/licenses/BSD-2-Clause>`_.
* Documentation: https://pc4bims.readthedocs.io.
* PyPI: https://pypi.python.org/pypi/pc4bims

Requirements
------------

The code was written in Python 3. The packages `numpy <http://www.numpy.org/>`_,
`scipy <https://www.scipy.org/>`_, `matplotlib <https://matplotlib.org/>`_
and `triangle <http://dzhelil.info/triangle/index.html#>`_ are
required for using ``pc4bims``. All of them are
downloadable from the PyPI repository by opening a terminal and typing the
following code lines:


::

    pip install numpy
    pip install scipy
    pip install matplotlib
    pip install triangle


Installation
------------


To install ``pc4bims`` open a terminal and type:

::

    pip install pc4bims


Example
-------

To produce the plot shown above execute the following script

::

    from numpy import array
    from pc4bims.slope import NaturalSlope
    from pc4bims.circlepacking import CirclePacking as CP
    surfaceCoords = array([[-2.4900, 18.1614],
                           [0.1022, 17.8824],
                           [1.6975, 17.2845],
                           [3.8909, 15.7301],
                           [5.8963, 14.3090],
                           [8.1183, 13.5779],
                           [9.8663, 13.0027],
                           [13.2865, 3.6058],
                           [20.2865, 3.6058],
                           [21.4347, 3.3231],
                           [22.2823, 2.7114],
                           [23.4751, 2.2252],
                           [24.6522, 1.2056],
                           [25.1701, 0.2488]])
    slopeGeometry = NaturalSlope(surfaceCoords)
    boundCoords = slopeGeometry.boundCoords
    circlePacking = CP(boundCoords, 2)
    circlePacking.plot()


