import pytest
from google_analytics import get_service
from data_setup import set_daterange, set_metrics, set_dimensions


class TestGoogleAnalytics:
    def test_set_datarange(self):
        assert [{"startDate": "2020-01-01", "endDate": "2020-02-01"}] == set_daterange(
            "2020-01-01", "2020-02-01"
        )

    def test_set_metrics(self):
        assert [{"expression": "ga:zzzz"}, {"expression": "ga:yyyy"}] == set_metrics(
            "ga:zzzz", "ga:yyyy"
        )

    def test_set_dimensions(self):
        assert [{"name": "ga:xxxx"}] == set_dimensions("ga:xxxx")


if __name__ == "__main__":
    pytest.main()
