""" pyedm

.. module:: pyedm
    :synopsis: tools for emobon-datamanagement

.. moduleauthor:: Marc Portier <marc.portier@gmail.com>

"""

from .tools import MyModel
from .__version__ import __version__
import logging

__all__ = ['MyModel', '__version__']

log = logging.getLogger(__name__)
# log.addHandler(logging.NullHandler())
