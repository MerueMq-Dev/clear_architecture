from capabilities.robot import create_state
from capabilities.caps import build_caps


def create_robot(
        transfer,
        resources=None):

    state = create_state(
        transfer,
        resources
    )

    return build_caps(state)