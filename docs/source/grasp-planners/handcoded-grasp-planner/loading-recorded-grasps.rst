Loading Recorded Grasps
=======================

The recommended way to use Grasplan is via `mobipick labs <https://github.com/DFKI-NI/mobipick_labs>`_.

You can use the `mobipick api <https://github.com/DFKI-NI/mobipick_api>`_ or the
`rqt tables demo <https://github.com/DFKI-NI/mobipick_labs/tree/noetic/rqt_tables_demo>`_ to access all grasplan functionality:

``roslaunch rqt_tables_demo rqt_tables_demo.launch namespace:=mobipick world_config:=moelk_tables``

replace ``moelk_tables`` with the name of your world configuration (e.g. ``cic_tables``).

For more documentation on pick and place pipeline, please refer to the :ref:`functionality` section.
