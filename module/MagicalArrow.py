class MagicalArrow:
    """
    Represents the stock of a particular Magical Arrow.

    ...

    Attributes
    -----------
    name : str
        The name of the arrow type
    price : int
        The arrow's price per arrow
    stock : int
        How many arrows are in stock

    Methods
    -----------
    toStr : str
        Returns string representation of the arrow
    """

    def __init__(self, name, price, stock):
        """
        Parameters
        -----------
        name : str
            name of arrow
        price : int
            price of bundle of arrows
        stock : int
            how many arrows are in stock
        """

        self.name = name
        self.price = price
        self.stock = stock

    def toStr(self) -> str:
        """Returns string Representation of arrow stock

        Multiples stock by 10 if it's just a normal arrow to simulate them
        being more common.

        Returns
        --------
        str
            String representation of arrows in stock
        """

        return f"{str(self.price)}gp/1\tStock:{str(self.stock)}\t{self.name}"