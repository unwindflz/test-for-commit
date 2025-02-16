import pytest
from src.utils.date_formatter import format_date

class TestDateFormatterIntegration:

    @pytest.mark.parametrize(
        'input_date, expected_output',
        [
            ('2023-01-15', 'January 15, 2023'),
            ('2022-12-31', 'December 31, 2022'),
            ('2023-07-04', 'July 4, 2023')
        ]
    )
    def test_format_date_integration(self, input_date, expected_output):
        result = format_date(input_date)
        assert result == expected_output
