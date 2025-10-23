from ch07_functions import fit_trendline


def test_fit_trendline():
    data = [1, 2, 3]
    timestamps = [2020, 2021, 2022]
    slope, r_squared = fit_trendline(timestamps, data)
    assert slope == 1
    assert r_squared == 1
