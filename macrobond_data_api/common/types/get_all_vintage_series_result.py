# get_all_vintage_series_result


from typing import TYPE_CHECKING, Any, Dict, Sequence

from macrobond_data_api.common.types.vintage_series import VintageSeries

if TYPE_CHECKING:  # pragma: no cover
    from pandas import DataFrame  # type: ignore

__pdoc__ = {
    "GetAllVintageSeriesResult.__init__": False,
}


class GetAllVintageSeriesResult(Sequence[VintageSeries]):
    """
    The result of downloading all vintages of a time series.
    """

    __slots__ = ("series", "series_name")

    series: Sequence[VintageSeries]
    series_name: str

    def __init__(
        self,
        series: Sequence[VintageSeries],
        series_name: str,
    ) -> None:
        super().__init__()
        self.series = series
        """A sequence of time series corresponding to the vintages."""
        self.series_name = series_name
        """The name of the requested series."""

    def to_pd_data_frame(self) -> "DataFrame":
        """
        Return the result as a Pandas DataFrame.
        """
        import pandas  # pylint: disable=import-outside-toplevel

        data = list(map(lambda s: s.values_to_pd_series(), self))
        data_frame = pandas.concat(data, axis=1, keys=[s.revision_time_stamp for s in self])
        data_frame = data_frame.sort_index()
        return data_frame

    def to_dict(self) -> Dict[str, Any]:
        """
        Return the result as a dictionary.
        """
        return {
            "series_name": self.series_name,
            "series": tuple(map(lambda x: x.to_dict(), self)),
        }

    def __repr__(self):
        return "GetAllVintageSeriesResult series_name: " + self.series_name

    def __getitem__(self, key):
        return self.series[key]

    def __len__(self) -> int:
        return len(self.series)
