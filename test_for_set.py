import pytest

@pytest.mark.parametrize(
   "days", [{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}]
)
def test1(days):
    assert len(days) == 7

@pytest.mark.parametrize(
   "days", [{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}]
)
def test2(days):
    try:
        assert "September" in days
    except AssertionError:
        pass


def test3():
    days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
    days1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
    assert days.issubset(days1)