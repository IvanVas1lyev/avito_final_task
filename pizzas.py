from default_pizza_class import Pizza


PIZZA_NAMES = [
    "Margherita",
    "Pepperoni",
    "Hawaiian"
]

PIZZA_SIZES = [
    "L",
    "XL"
]


class Margherita(Pizza):
    def __init__(self, size: str = "L"):
        """
        Initializes pizza Margherita

        Parameters
        ----------
        size : str
            Initial size of the pizza

        Attributes
        ----------
        size : str
            Size of the pizza
         ingredients : list
            Ingredients of the pizza
        """
        super().__init__(size)

        self.add_ingredients('Tomatoes')


class Pepperoni(Pizza):
    def __init__(self, size: str = "L"):
        """
        Initializes pizza Pepperoni

        Parameters
        ----------
        size : str
            Initial size of the pizza

        Attributes
        ----------
        size : str
            Size of the pizza
         ingredients : list
            Ingredients of the pizza
        """
        super().__init__(size)

        self.name = "Pepperoni"
        self.add_ingredients('Pepperoni')


class Hawaiian(Pizza):
    def __init__(self, size: str = "L"):
        """
        Initializes pizza Hawaiian

        Parameters
        ----------
        size : str
            Initial size of the pizza

        Attributes
        ----------
        size : str
            Size of the pizza
         ingredients : list
            Ingredients of the pizza
        """
        super().__init__(size)

        self.add_ingredients('Chicken')
        self.add_ingredients('Pineapples')


if __name__ == "__main__":
    p_L = Pepperoni('L')
    m_XL = Margherita('XL')
    h_XL = Hawaiian('XL')

    p_L_1 = Pepperoni('L')

    print(p_L.dict())
    print(h_XL.dict())

    print(h_XL == m_XL)
    print(p_L_1 == p_L)
