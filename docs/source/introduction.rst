Introduction
============

Grasplan is open source, it's code can be located at `Github <https://github.com/aprilprojecteu/grasplan>`_.

At the moment, Grasplan is available for ROS1 noetic distro and loosely coupled to the `mobipick robot <https://github.com/dfKI-NI/mobipick>`_,
so you can use many of the tools but if you are not using the mobipick robot, you will have to adapt some of the code to your needs.

Grasplan was developed as part of the EU APRIL project.

.. figure:: images/logo/april_eu_logo.png
   :alt: eu flag
   :align: center

   APRIL Project EU: multipurpose robotics for mAniPulation of defoRmable materIaLs in manufacturing processes.

For more information, please visit the `APRIL project website <https://aprilproject.eu/>`_.

To see a video of grasplan in action, see `our mobipick labs video <https://youtu.be/4-GgOg2nuGE?si=U86BsRT2yU7hPPBe>`_,
jump to 3:10 for the grasping part.

What is Grasplan?
-----------------

As the name hints, Grasplan is a library for grasp planning with currently two grasp planners implemented:

- :ref:`handcoded-grasp-planner`
- :ref:`simple-pregrasp-planner`

See section :ref:`grasp-planners` for more information.

We mostly use the :ref:`handcoded-grasp-planner`, therefore it's state should be more stable.

Apart from providing (simple) grasp planning, Grasplan also a wrapps MoveIt pick and place functionality, plus some extra tools to:

- record and edit grasps via custom gui and optionally physics based simulator (Gazebo).
- build a "grasplan" planning scene (with custom gui) which is defined as a set of boxes in 3D space that later gets converted into a MoveIt planning scene.
- loads pre-recorded grasps and configuration from yaml files to call moveit pick action server with appropriate parameters.
- samples free place poses and calls moveit place action server with appropriate parameters to place an object in 3D space.
- insert.py script - a workaround to drop objects in a container by calling place action with a pose just above the container.

Other secondary tools include:

- gripper mesh visualization in RViz.
- "grasplan" planning scene visualization in RViz.
