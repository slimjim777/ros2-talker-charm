import os

import charms.apt

from subprocess import (
    check_call,
    check_output,
    CalledProcessError
)
from charmhelpers.core import (
    templating,
    hookenv,
    host
)
from charms.reactive import (
    hook, 
    is_state, 
    set_state,
    when
)

PROJECT = 'ros2-talker'
AVAILABLE = '{}.available'.format(PROJECT)

@hook("install")
def install():
    """
    """
    if is_state(AVAILABLE):
        return


@when('apt.installed.ros-bouncy-ros-base')
@when('apt.installed.python3-colcon-common-extensions')
def grabit():
    # Build and deploy the application
    build_from_source()


def build_from_source():
    """
    Set up the ROS2 workspace and build the package(s)
    """
    hookenv.status_set('maintenance', 'Building application')
    config = hookenv.config()

    check_call(['sh', './scripts/install.sh'])

    hookenv.status_set('maintenance', 'Installation complete')
