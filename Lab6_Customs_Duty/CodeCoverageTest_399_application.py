import pytest
from customs_duty import duty_rate, total_duty, clearance_channel


# 1. DUTY RATE TEST CASES

def test_prohibited_item():
    with pytest.raises(ValueError):
        duty_rate("weapons", "US")


def test_electronics_fta():
    assert duty_rate("electronics", "FTA") == 0.10


def test_electronics_non_fta():
    assert duty_rate("electronics", "US") == 0.20


def test_clothing_fta():
    assert duty_rate("clothing", "FTA") == 0.05


def test_clothing_non_fta():
    assert duty_rate("clothing", "US") == 0.12


def test_books_duty_free():
    assert duty_rate("books", "US") == 0


def test_other_category():
    assert duty_rate("furniture", "US") == 0.15


# 2. TOTAL DUTY TEST CASES

def test_negative_value():
    with pytest.raises(ValueError):
        total_duty("electronics", -100, "US", False)


def test_gift_below_limit():
    assert total_duty("electronics", 4000, "US", True) == 0


def test_gift_above_limit():
    assert total_duty("electronics", 6000, "FTA", True) == 100


def test_non_gift_below_limit():
    assert total_duty("electronics", 500, "US", False) == 0


def test_non_gift_above_limit():
    assert total_duty("electronics", 2000, "US", False) == 400


def test_minimum_duty():
    assert total_duty("clothing", 5001, "FTA", True) == 50


# 3. CLEARANCE CHANNEL TEST CASES

def test_prohibited_clearance():
    assert clearance_channel(500, "weapons", True) == "refuse"


def test_high_value_inspection():
    assert clearance_channel(150000, "electronics", True) == "inspect"


def test_missing_documents_inspection():
    assert clearance_channel(30000, "electronics", False) == "inspect"


def test_green_channel():
    assert clearance_channel(5000, "electronics", True) == "green"