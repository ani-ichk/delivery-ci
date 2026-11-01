import pytest
from delivery import calculate_delivery


# Обычная доставка: обычные и граничные суммы
@pytest.mark.parametrize("subtotal, expected", [
    (0, 300),
    (999, 300),
    (1000, 150),
    (4999, 150),
    (5000, 0),
])
def test_regular_delivery(subtotal, expected):
    assert calculate_delivery(subtotal) == expected

# Экспресс-доставка: те же суммы, плюс 250 рублей
@pytest.mark.parametrize("subtotal, expected", [
    (0, 550),
    (999, 550),
    (1000, 400),
    (4999, 400),
    (5000, 250),
])
def test_express_delivery(subtotal, expected):
    assert calculate_delivery(subtotal, express=True) == expected

# Отрицательная сумма
@pytest.mark.parametrize("subtotal", [-1, -1000])
def test_negative_subtotal(subtotal):
    with pytest.raises(ValueError):
        calculate_delivery(subtotal)

# Некорректный тип subtotal
@pytest.mark.parametrize("subtotal", ["100", 10.5, None, True])
def test_wrong_subtotal_type(subtotal):
    with pytest.raises(TypeError):
        calculate_delivery(subtotal)

# Некорректный тип express
@pytest.mark.parametrize("express", ["yes", 1, None])
def test_wrong_express_type(express):
    with pytest.raises(TypeError):
        calculate_delivery(100, express=express)