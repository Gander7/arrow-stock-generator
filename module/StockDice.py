from random import randint

class StockDice:
    """
    Represents Dice used for generating amount of stock
    
    ...

    Attributes
    -----------
    numOfDice : int
        Number of Dice to roll
    dieSize : int
        Size of dice to roll. i.e. 20 sided dice

    Methods
    -----------
    roll() : int
        Rolls the configured dice(2d20) and returns the sum
    """

    def __init__(self, stockDieString: str):
        """
        Parameters
        -----------
        stockDieString : str
            String representation of dice to roll delimited by a 'd'. 
            Valid Examples: 2d20, 5d8, 3d4, 7d10, 1d12
            Invalid Examples: 20, d10, 10d, 3e40

        Raises
        -----------
        ValueError
            If the stock die is not in an acceptable pattern.
        """
        
        import re
        pattern = re.compile("^[1-9][0-9]*d[1-9][0-9]*$")
        if pattern.match(stockDieString) == None:
            raise ValueError("Invalid Stock Dice Pattern.")

        splitString = stockDieString.split("d")
        self.numOfDice = int(splitString[0])
        self.dieSize = int(splitString[1])

    def roll(self) -> int:
        """Returns how many arrows should be in stock.

        Rolls the dice to determine how many of that arrow should
        be in stock.

        Returns
        --------
        int
            How many arrows should be in stock based on given dice.
        """

        result = 0
        for _ in range(0, self.numOfDice):
            result += randint(1, self.dieSize)
        return result