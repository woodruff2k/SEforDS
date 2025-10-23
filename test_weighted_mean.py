from ch07_functions import weighted_mean


def test_weighted_mean():
    """
    list_a = [1, 2, 4]
    list_b = [1, 2, 4]
    result = weighted_mean(list_a, list_b)
    """
    result = weighted_mean([1, 2, 4], [1, 2, 4])
    assert result == 3
    empty_list_result = weighted_mean([], [])
    assert not empty_list_result
    wrong_types_result = weighted_mean(["one", 2, 4], [1, 2, 4])
    assert not empty_list_result
