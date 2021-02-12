from ask import countHowManyCorrect
import pytest

@pytest.mark.parametrize('input_list_, comparison_list_, result', 
    [
        (['a', 'b', 'c'], ['x', 'y', 'z'], 0),
        (['a', 'b'], ['y', 'z'], 0),
        (['a'], ['z'], 0),
        (['a', 'b', 'c'], ['a', 'b', 'c'], 3),
        (['a', 'b'], ['a', 'b'], 2),
        (['a'], ['a'], 1),
        (['a', 'W', 'W'], ['a', 'b', 'c'], 1),
        (['a', 'b', 'c', 'W'], ['a', 'b', 'c', 'd', 'e', 'f'], 3)
    ]
)


def test_countHowManyCorrect(input_list_, comparison_list_, result):
    assert countHowManyCorrect(input_list_, comparison_list_) == result
