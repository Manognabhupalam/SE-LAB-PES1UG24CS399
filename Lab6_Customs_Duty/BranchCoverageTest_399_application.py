
import pytest
from customs_duty import duty_rate, total_duty, clearance_channel


# 1. DUTY RATE - TRUE AND FALSE BRANCHES

def test_prohibited_category():
    with pytest.raises(ValueError):
        duty_rate("narcotics", "US")


def test_allowed_category():
    assert duty_rate("electronics", "FTA") == 0.10


def test_electronics_fta():
    assert duty_rate("electronics", "FTA") == 0.10


def test_electronics_non_fta():
    assert duty_rate("electronics", "US") == 0.20


def test_clothing_fta():
    assert duty_rate("clothing", "FTA") == 0.05


def test_clothing_non_fta():
    assert duty_rate("clothing", "US") == 0.12


def test_books_category():
    assert duty_rate("books", "US") == 0


def test_unknown_category():
    assert duty_rate("furniture", "US") == 0.15


# 2. TOTAL DUTY - TRUE AND FALSE BRANCHES

def test_negative_import_value():
    with pytest.raises(ValueError):
        total_duty("electronics", -100, "US", False)


def test_valid_import_value():
    assert total_duty("electronics", 2000, "US", False) == 400


def test_gift_at_limit():
    assert total_duty("electronics", 5000, "US", True) == 0


def test_gift_above_limit():
    assert total_duty("electronics", 6000, "FTA", True) == 100


def test_non_gift_at_limit():
    assert total_duty("electronics", 1000, "US", False) == 0


def test_non_gift_above_limit():
    assert total_duty("electronics", 2000, "US", False) == 400


def test_minimum_duty_applied():
    assert total_duty("clothing", 5001, "FTA", True) == 50


def test_zero_duty_no_minimum():
    assert total_duty("books", 6000, "US", True) == 0


def test_duty_above_minimum():
    assert total_duty("electronics", 2000, "US", False) == 400


# 3. CLEARANCE CHANNEL - TRUE AND FALSE BRANCHES

def test_prohibited_item_refused():
    assert clearance_channel(500, "weapons", True) == "refuse"


def test_non_prohibited_item():
    assert clearance_channel(5000, "electronics", True) == "green"


def test_value_above_100000():
    assert clearance_channel(150000, "electronics", True) == "inspect"


def test_value_below_100000():
    assert clearance_channel(50000, "electronics", True) == "green"


def test_above_20000_without_documents():
    assert clearance_channel(30000, "electronics", False) == "inspect"


def test_above_20000_with_documents():
    assert clearance_channel(30000, "electronics", True) == "green"


def test_exactly_20000_without_documents():
    assert clearance_channel(20000, "electronics", False) == "green"
