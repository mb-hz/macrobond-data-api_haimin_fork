# -*- coding: utf-8 -*-

# pylint: disable = missing-module-docstring

from typing import Optional, Tuple
from typing_extensions import TypedDict


class VintageValuesResponse(TypedDict, total=False):
    """A time series with times of change"""

    vintageTimeStamp: Optional[str]
    """The time when this version of the series was recorded"""

    dates: Tuple[str, ...]
    """The dates of the vintage series."""

    values: Tuple[Optional[float], ...]
    """The values of the vintage series. Missing values are represented by null."""
