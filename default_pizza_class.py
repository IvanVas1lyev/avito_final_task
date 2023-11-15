class Pizza:
    """
    Implementation of default class with empty pizza

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
    def __init__(self, size: str = "L") -> None:
        """
        Initializes default empty pizza

        Parameters
        ----------
        size : str
            Initial size of the pizza
        """
        self.size = size
        self.ingredients = ['Mozzarella', 'Tomato sauce']

    def add_ingredients(self, ingredient: str) -> None:
        """
        Adds an ingredient to the pizza

        Parameters
        ----------
        ingredient : str
            New ingredient
        """
        self.ingredients.append(ingredient)

    def dict(self) -> dict:
        """
        Gives pizza's short info

        Returns
        -------
        list
            Pizza's recept
        """
        return self.ingredients

    def __eq__(self, other) -> bool:
        """
        Сhecks if two pizzas are equal

        Parameters
        ----------
        other : Pizza
            Pizza to compare

        Returns
        -------
        bool
            Pizzas sameness flag
        """
        is_sizes_equal = self.size == other.size
        is_ingredients_equal = self.ingredients == other.ingredients

        return is_sizes_equal and is_ingredients_equal
