"""Arrow Stock Generator

This script generates and prints out a list of arrows in stock for a shop with
magical arrows using a config. The config can be updated with what arrows to be
included in the generation, the chance of them being in stock by rarity, the
price of each arrow by rarity, and the potential variance in prices.

Parameters
-----------
configFilename : str
    The relative path and name of the config file from where the script
    is being run from. This will default to "../config.yaml" which is included
    in the repo but will only work if the module is run from inside the module
    folder.
"""

from yaml import safe_load
from sys import argv

from StockDice import StockDice
from MundaneArrow import MundaneArrow
from MagicalArrow import MagicalArrow
from helper import isArrowInStock, getPriceWithVariance, getAlphabeticalArrowList

def processMagicalArrows(rarity: str, rarityEnglish = "") -> None:
    """Processes and prints a list of magical arrows

    Gets config, processes and prints out any magical arrows from a given list
    that are deemed that there should be stock of. Nothing will print,
    including header, if none of the arrows are in stock.  

    Parameters
    -----------
    rarity : str
        List of arrows to retrieve from the config
    rarityEnglish : str, optional
        Optional. Human readable name of the list of arrows to print. If
        this is not used the rarity parameter will be capitalized and used.
    """

    title = (rarityEnglish if rarityEnglish else rarity.capitalize())

    # Config values for the list
    arrows = dictionary[rarity]['arrows']
    chance = int(dictionary[rarity]['chance'])
    stock = StockDice(dictionary[rarity]['stock'])
    price = int(dictionary[rarity]['price'])
    variance = int(dictionary[rarity]['variance'])

    if len(arrows) < 1:
        return

    ## Generate Stock
    inStock = []
    for a in getAlphabeticalArrowList(arrows):
        if isArrowInStock(chance):
            inStock.append(MagicalArrow( a['name'], getPriceWithVariance(price, variance), stockDice.roll()
            ))

    ## Print Stock if any
    if len(inStock) > 0:
        print("")
        print(f"## {str(title)} Arrows ##")
        for a in inStock:
            print(a.toStr())

if __name__ == '__main__':

    # Load config
    configFilename = "../config.yaml"
    if len(argv) > 1:
        configFilename = argv[1] if argv[1] else "../config.yaml"
    stream = open(f"{configFilename}",'r')
    dictionary = safe_load(stream)

    # Get Mundane Arrows from config
    arrows = dictionary['mundane']['arrows']
    chance = int(dictionary['mundane']['chance'])
    stockDice = StockDice(dictionary['mundane']['stock'])

    # Stock and Print Mundane Arrows
    print("## Mundane Arrows ##")
    for a in getAlphabeticalArrowList(arrows):
        arrow = MundaneArrow(
            a['name'], a['price'], a['bundle'], 
            stockDice.roll())
        print(arrow.toStr())

    # Process Magical Arrows by rarity
    processMagicalArrows("common")
    processMagicalArrows("uncommon")
    processMagicalArrows("rare")
    processMagicalArrows("veryrare", "Very Rare")
    processMagicalArrows("legendary")
