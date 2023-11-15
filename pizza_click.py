import click
from pizzas import Pepperoni, Margherita, Hawaiian, PIZZA_NAMES, PIZZA_SIZES
from log import log


@click.group()
def cli():
    """
    Cli for pizza
    """
    pass


@cli.command()
@click.argument('pizza_name')
@click.argument('pizza_size')
@click.option('--delivery', is_flag=True)
@click.option("--pickup", is_flag=True)
def order(pizza_name: str, pizza_size: str, delivery: bool, pickup: bool):
    """
    Order pizzas with delivery and pickup option

    Parameters
    ----------
    pizza_name : str
        Name of pizza in order
    pizza_size : str
        Size of pizza in order
    delivery : bool
        Is order for delivery
    pickup : bool
        Is order for pickup
    """
    if pizza_name not in PIZZA_NAMES:
        click.echo('No such pizza in the menu 😔')
        return
    if pizza_size not in PIZZA_SIZES:
        click.echo('No such pizza size in the menu 😔')
        return

    bake(pizza_name)

    if delivery:
        deliver(pizza_name, pizza_size)
    elif pickup:
        pick(pizza_name, pizza_size)
    else:
        click.echo('Where to put this pizza now... 😔')


@log("Baked in {:.0f} minutes!")
def bake(pizza_name: str) -> None:
    """
    Bakes pizza
    
    Parameters
    ----------
    pizza_name : str
        Name of pizza in order
    """
    click.echo(f"Start baking {pizza_name}!")


@log("Pizza is delivered in {:.0f} minutes!")
def deliver(pizza_name: str, pizza_size: str) -> None:
    """
    Delivers baked pizza

    Parameters
    ----------
    pizza_name : str
        Name of pizza in order
    pizza_size : str
        Size of pizza in order
    """
    click.echo(f"{pizza_name} {pizza_size} size is coming!")


@log("Picked up in {:.0f} minutes!")
def pick(pizza_name: str, pizza_size: str) -> None:
    """
    Controls process of customer pick-up
    
    Parameters
    ----------
    pizza_name : str
        Name of pizza in order
    pizza_size : str
        Size of pizza in order
    """
    click.echo(f"{pizza_name} {pizza_size} size is ready for pick-up!")


@cli.command()
def menu() -> None:
    """
    Shows pizza menu
    """
    margherita = Margherita()
    pepperoni = Pepperoni()
    hawaiian = Hawaiian()

    click.echo('Menu:')
    click.echo(f'• 🍅 Margherita : {", ".join(margherita.ingredients)}')
    click.echo(f'• 🍕 Pepperoni : {", ".join(pepperoni.ingredients)}')
    click.echo(f'• 🍍 Hawaiian : {", ".join(hawaiian.ingredients)}')


if __name__ == '__main__':
    cli()
