class MundaneArrow:
    """
    Represents the stock of a particular Mundane Arrow. If the arrow's stock
    is less than the bundle size, the stock will default to the bundle size.

    ...

    Attributes
    -----------
    name : str
        The name of the arrow type
    price : int
        The arrow's price per bundle
    bundle : int
        Size of bundle of arrows
    stock : int
        How many arrows are in stock

    Methods
    -----------
    toStr : str
        Returns string representation of the arrow
    """

    def __init__(self, name: str, price: int, bundle: int, stock: int):
        """
        Parameters
        -----------
        name : str
            name of arrow
        price : int
            price of bundle of arrows
        bundle : int
            size of a bundle of arrows
        stock : int
            how many arrows are in stock
        """

        self.name = name
        self.price = price
        self.bundle = bundle
        self.stock = self.bundle if self.bundle > stock else stock

    def toStr(self) -> str:
        """Returns string Representation of arrow stock

        Multiples stock by 10 if it's just a normal arrow to simulate them
        being more common.

        Returns
        --------
        str
            String representation of arrows in stock
        """

        stock = self.stock * 10 if self.name == "Normal Arrow" else self.stock
        return f"{str(self.price)}gp/{str(self.bundle)}\tStock:{str(stock)}\t{self.name}"