from random import randint

def isArrowInStock(chance: int) -> bool:
    """Returns a boolean given the chance that an arrow is in stock

    Randomizes and returns whether the arrow is in stock given the 
    chance that it should be in stock.

    Parameters
    ---------
    chance : int 
        The percentage(in whole numbers) that the arrow should be in stock

    Returns
    -------
    bool
        Whether or not there should be arrows in stock
    """

    return randint(1, 100) <= chance

def getPriceWithVariance(price: int, variance: int) -> int:
    """Gets a Varied Price

    Returns a price with a whole number random variance (-/+) given a 
    maximum variance from the stated price.

    Parameters
    ----------
    price : int
        The price of the arrow before variance
    variance : int
        The whole number that the price can possibly be varied by postively
        or negatively.

    Returns
    --------
    int
        The price after variance has been included
    """

    return price + randint(variance * -1, variance)

def getAlphabeticalArrowList(arrows: list) -> list:
    """Returns a list of arrows sorted by name
    
    Parameters
    -----------
    arrows : list
        List to be sorted

    Returns
    --------
    list
        List sorted by name property
    """

    return sorted(arrows, key=lambda x: x['name'])