import pytest

from source.app import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),      
        (-1, 1, 0),    
        (0, 0, 0),      
        (100, 200, 300),
        (-5, -5, -10),  
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected
