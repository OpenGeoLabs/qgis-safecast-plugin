Installation
============

Go to :menuselection:`Plugins --> Manage and Install Plugins`:

.. figure:: images/004_plugins_menu.png
   :width: 400px

   Plugins menu.

You should have **Safecast Plugin** available in QGIS plugins selection
and you can install it:

.. figure:: images/install_005_install_plugin.png

   Plugins menu - install Safecast plugin.
   
and the plugin icon appears in the QGIS toolbar:

.. figure:: images/install_006_Safecast_plugin_in_QGIS.png

   Safecast plugin in QGIS toolbar.

and now the plugin is ready to use.

Graphs support
--------------

In order to display :ref:`graph_tab` *PythonQwt* or *Qwt6* library is
required by Safecast plugin. None of these libraries are part of
standard QGIS installation.

MS Windows
^^^^^^^^^^

Installation procedure depends on how QGIS has been installed. On MS
Windows QGIS can be installed either through *Standalone* or *OSGeo4W
Network* Installer, see `download page
<https://qgis.org/en/site/forusers/download.html>`__ for details.

Standalone Installer
~~~~~~~~~~~~~~~~~~~~

In the case of *Standalone Installer* (QGIS is typically installed in
:file:`C:\Program Files`) open *OSGeo4W Shell* as administrator. Than
from OSGeo4W command prompt run two commands below:

.. code-block:: bash

   py3_env
   pip3 install pythonqwt

OSGeo4W Network Installer
~~~~~~~~~~~~~~~~~~~~~~~~~

*PythonQwt* can be installed throuh *OSGeo4W Network
Installer*. Choose `Advanced Install`. In section `Libs` enable
`python3-pythonqwt` package in order to install it.

.. figure:: images/install_007_osgeo4w_pythonqwt.png

   Install `python3-pythonqwt` from OSGeo4W Network Installer.

Ubuntu Linux
^^^^^^^^^^^^

*Qwt6* library is available only on newer versions of Ubuntu operating
system (19.04 and following). It can be installed by following
command:

.. code-block:: bash

   sudo apt install python3-pyqt5.qwt

On Ubuntu 18.04 install *PythonQwt* library instead:

.. code-block:: bash

   sudo pip3 install PythonQwt
