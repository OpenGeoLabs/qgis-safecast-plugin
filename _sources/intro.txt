Introduction
============

.. _bgeigie:

The `Safecast bGeigie Nano
<https://en.wikipedia.org/wiki/Safecast_(organization)#bGeigie_Nano>`__
is a portable radiation sensor with GPS designed for citizen radiation
monitoring (car, bike, on foot etc.). It records dose rate values
along with appropriate date/time and GPS coordinates every 5 seconds
and writes it on built-in microSD card.

.. _ader:

bGeigie Nano is equipped with a pancake Geiger-Müller tube. A recorded
number of pulses per time interval is automatically converted to the
dose rate. The calculation is based on a device calibration, using
Cs-137 source and a resulting physical variable. A resulting physical
variable is called for simplicity just "dose rate", although in actual
truth it is "ambient dose equivalent rate" (`ADER
<https://en.wikipedia.org/wiki/Absorbed_dose>`__) to be measured in
*microSv/h* (microSievert per hour).

The current Safecast solution contains bGeigie portable devices and
online services to process the measurements and display them in an
`interactive map <http://safecast.org/tilemap/>`__. However, as in
many cases a reliable internet connection is not available. An offline
solution is required, not only for monitoring in distant areas, but
also for possible use of bGeigies to provide supporting data for
crisis management in case of radiation accident.
