import pytest
from seasons import convert_date

def test_convert_date():
    assert convert_date("2022-02-08") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_date("2021-02-08") == "One million, fifty-one thousand, two hundred minutes"

    with pytest.raises(SystemExit):
        convert_date("January 1, 1999")
