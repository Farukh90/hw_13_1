import pytest
from src.classes import Category
from src.classes import Product


@pytest.fixture()
def test_category_without_list():
    return Category('Шоколадная продукция', 'продукция из фабрики уилли уонка')


@pytest.fixture()
def test_category_with_list():
    return Category('Шоколадная продукция', 'продукция из фабрики уилли уонка', ['снукерс', 'киндер сюрприз'])


@pytest.fixture()
def test_product_float_price():
    return Product('киндер сюрприз', 'молочный шоколад, внутри игрушка', 120.2, 33)

@pytest.fixture()
def test_product_int_price():
    return Product('киндер сюрприз', 'молочный шоколад, внутри игрушка', 120, 33)



def test_init_without_list(test_category_without_list):
    assert test_category_without_list.name == 'Шоколадная продукция'
    assert test_category_without_list.description == 'продукция из фабрики уилли уонка'


def test_init_with_list(test_category_with_list):
    assert test_category_with_list.name == 'Шоколадная продукция'
    assert test_category_with_list.description == 'продукция из фабрики уилли уонка'
    assert test_category_with_list.products == ['снукерс', 'киндер сюрприз']


def test_init_float_price(test_product_float_price):
    assert test_product_float_price.name == 'киндер сюрприз'
    assert test_product_float_price.description == 'молочный шоколад, внутри игрушка'
    assert test_product_float_price.price == 120.2
    assert test_product_float_price.in_stock == 33

def test_init_int_price(test_product_int_price):
    assert test_product_int_price.name == 'киндер сюрприз'
    assert test_product_int_price.description == 'молочный шоколад, внутри игрушка'
    assert test_product_int_price.price == 120
    assert test_product_int_price.in_stock == 33