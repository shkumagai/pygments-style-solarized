Install
=======

Using PyPI and pip
------------------
::

   $ (sudo) pip install pygments-style-solarized

Manual
------
::

   $ git clone git://github.com/shkumagai/pygments-style-solarized
   $ cd pygments-style-solarized
   $ (sudo) python setup.py install

Usage Sample
------------
::

   >>> from pygments.formatter import HtmlFormatter
   >>> HtmlFormatter(style='solarizedlight').style
   <class 'pygments_style_solarized.light.LightStyle'>
   >>> HtmlFormatter(style='solarizeddark').style
   <class 'pygments_style_solarized.light.DarkStyle'>


Export the style as CSS
-----------------------
::

   pygmentize -S solarized-light -f html > solarizedlight.css

