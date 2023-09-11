from pizza import Pizza, Margherita, Hawaiian, Pepperoni
from decorator import log
import click


@log("Вашу пиццу приготовили за")
def bake(pizza: Pizza) -> None:
    """Готовят пиццу"""
    pass


@log("Ваша пицца будет доставлена через")
def deliever(pizza: Pizza) -> None:
    """Достовляет пиццу"""
    pass


def cli():
    pass


@log("Вы забрали пиццу за")
def pickup(pizza: Pizza) -> None:
    """Самовывоз"""
    pass


@click.command()
def menu():
    """
    Выводит меню пиццы.

    """
    menu = {}
    menu["Marherita"] = Margherita("L")
    menu["Pepperoni"] = Pepperoni("L")
    menu["Hawaiian"] = Hawaiian("L")
    emoji = ["🧀", "🥩", "🍍"]
    p = ""
    k = 0
    for i in menu.keys():
        text = f" -- {i} {emoji[k]}: {', '.join(menu[i].dict().keys())}\n"
        p = p + text
        k += 1
    print("Меню пиццы:")
    print(p)


@click.command()
@click.option('--delivery', default=False, is_flag=True, help='Флаг для доставки')
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
def order(delivery: bool, pizza: Pizza, size: str):
    """
    Информация для вашего заказа.

    """
    menus = {}
    sizes = ["L", "XL"]
    menus["margherita"] = Margherita(size)
    menus["pepperoni"] = Pepperoni(size)
    menus["hawaiian"] = Hawaiian(size)
    if pizza not in menus:
        print("😦В нашем меню нет такой пиццы, пожалуйста, выберете другую пиццу из нашего меню😦")
        return
    if size not in sizes:
        print("😛Выберете другой размер для пиццы😛")
        return
    bake(menus[pizza])
    if delivery:
        deliever(menus[pizza])
    else:
        pickup(menus[pizza])
        print("🍕Приятного аппетита, заказывайте почаще у нас пиццу!🍕")


if __name__ == "__main__":
    cli = click.Group()
    cli.add_command(menu)
    cli.add_command(order)
    cli()
