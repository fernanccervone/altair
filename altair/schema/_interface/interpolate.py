# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T


class Interpolate(T.Enum):
    """One of ['linear', 'linear-closed', 'step', 'step-before', 'step-after', 'basis', 'basis-open', 'basis-closed', 'cardinal', 'cardinal-open', 'cardinal-closed', 'bundle', 'monotone']"""
    def __init__(self, default_value=T.Undefined, **metadata):
        super(Interpolate, self).__init__(['linear', 'linear-closed', 'step', 'step-before', 'step-after', 'basis', 'basis-open', 'basis-closed', 'cardinal', 'cardinal-open', 'cardinal-closed', 'bundle', 'monotone'],
                                    default_value=default_value,
                                    **metadata)