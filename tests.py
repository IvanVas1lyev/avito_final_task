import pytest
from click.testing import CliRunner

from pizza_click import order, menu
from pizzas import Pepperoni, Hawaiian, Margherita, PIZZA_NAMES, PIZZA_SIZES


@pytest.mark.parametrize(
    "source, exp",
    [
        ("Margherita", "['Mozzarella', 'Tomato sauce', 'Tomatoes']"),
        ("Pepperoni", "['Mozzarella', 'Tomato sauce', 'Pepperoni']"),
        ("Hawaiian", "['Mozzarella', 'Tomato sauce', 'Chicken', 'Pineapples']")
    ]
)
def test_pizza_dict(source: str, exp: str) -> None:
    """
    Test pizza dict method

    Params
    ------
    sourse : str
        Pizza's name to create class
    exp : str
        Expected pizza's result of .dict() method
    """
    pizza = eval(source)() 
    # кажется, не лучшее решениие, но любые другие,
    # которые я находил, тоже были плохие

    assert str(pizza.dict()) == exp


def test_menu() -> None:
    """
    Test menu
    """
    runner = CliRunner()
    res = runner.invoke(menu)

    assert res.exit_code == 0
    assert "Tomato sauce" in res.output
    assert "Pepperoni" in res.output


@pytest.mark.parametrize(
    "sourse, exp",
    [
        (PIZZA_NAMES[0], f"Start baking {PIZZA_NAMES[0]}!"),
        (PIZZA_NAMES[1], f"Start baking {PIZZA_NAMES[1]}!"),
        (PIZZA_NAMES[2],  f"Start baking {PIZZA_NAMES[2]}!"),
    ]
)
def test_bake(sourse: str, exp: str) -> None:
    """
    Test bake

    Params
    ------
    sourse : str
        Pizza's name to create class
    exp : str
        Expected pizza's result of bake func
    """
    runner = CliRunner()
    res = runner.invoke(order, [sourse, PIZZA_SIZES[0]])

    assert res.exit_code == 0
    assert exp in res.output


def test_order_with_delivery() -> None:
    """
    Test order with delivery
    """
    runner = CliRunner()
    res = runner.invoke(order, [PIZZA_NAMES[0], PIZZA_SIZES[0], "--delivery"])

    assert res.exit_code == 0
    assert f"{PIZZA_NAMES[0]} L size is coming!" in res.output
    assert "Pizza is delivered in" in res.output


def test_order_with_pickup() -> None:
    """
    Test order with pickup
    """
    runner = CliRunner()
    res = runner.invoke(order, [PIZZA_NAMES[1], PIZZA_SIZES[1], "--pickup"])

    assert res.exit_code == 0
    assert f"{PIZZA_NAMES[1]} XL size is ready for pick-up!" in res.output
    assert "Picked up in" in res.output


def test_pizza_class():
    """
    Test pizza's class
    """
    pepperoni_l_size = Pepperoni('L')
    hawaiian_l_size = Hawaiian('L')
    margherita_xl_size = Margherita('XL')

    assert (margherita_xl_size.dict() ==
            ['Mozzarella', 'Tomato sauce', 'Tomatoes'])
    assert (pepperoni_l_size.dict() ==
            ['Mozzarella', 'Tomato sauce', 'Pepperoni'])
    assert (hawaiian_l_size.dict() ==
            ['Mozzarella', 'Tomato sauce', 'Chicken', 'Pineapples'])

    assert pepperoni_l_size == pepperoni_l_size
    assert hawaiian_l_size != margherita_xl_size
