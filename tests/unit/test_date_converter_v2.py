import pytest
from src.utils.date_converter import convert_date


def test_convert_date_valid():
    assert convert_date('2023-01-01', '%Y-%m-%d', '%d/%m/%Y') == '01/01/2023'
    assert convert_date('01/01/2023', '%d/%m/%Y', '%Y-%m-%d') == '2023-01-01'


def test_convert_date_invalid_format():
    with pytest.raises(ValueError):
        convert_date('2023-01-01', '%Y/%m/%d', '%d/%m/%Y')


def test_convert_date_empty_input():
    with pytest.raises(ValueError):
        convert_date('', '%Y-%m-%d', '%d/%m/%Y')


def test_convert_date_none_input():
    with pytest.raises(TypeError):
        convert_date(None, '%Y-%m-%d', '%d/%m/%Y')
