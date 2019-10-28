acbenchmark
===========

Script to run browsertime against Firefox Desktop on a few websites.

Used as a playground to test features like network throttling,
prefs tweakings etc..

::

   $ git clone https://github.com/tarekziade/acbenchmark
   $ cd acbenchmark
   $ virtualenv .
   $ bin/python setup.py develop
   $ bin/acb --iteration 2 --name tinap_rust
