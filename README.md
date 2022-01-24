# Arrow Stock Generator
=================================
A script to easily generate stocked arrows in a shop.

## Getting Started
---------------------
1. Clone the repo
2. Create/update/tweak the config file for your setting/shop
3. Run the script inside the module folder 
```
cd modules
python core.py
```
or from the main folder with
```
python modules/core.py config.yaml
```
5. Copy Output and send to your player

NOTE: In Config there are some arrows with an X in their name. I use dndbeyond for most of my campaigns and the ones with an X are ones I haven't created in ddb yet.

### Example Output

Based off committed config

```
## Mundane Arrows ##
25gp/1  Stock:22        Adamantium Arrow
1gp/10  Stock:15        Broadhead Arrow
1gp/10  Stock:36        Hammerhead Arrow
1gp/20  Stock:200       Normal Arrow
10gp/1  Stock:17        Silvered Arrow
1gp/1   Stock:34        Smoking Arrow

## Common Arrows ##
5gp/1   Stock:19        Acid Arrow X
8gp/1   Stock:19        Firestorm Arrow X
10gp/1  Stock:28        Healing Arrow X
15gp/1  Stock:12        Siege Arrow X
7gp/1   Stock:14        Sleep Arrow X
15gp/1  Stock:20        Tracking Arrow X

## Uncommon Arrows ##
23gp/1  Stock:23        Arrow of Unpleasant Herbs
34gp/1  Stock:20        Bullseye Arrow
24gp/1  Stock:31        Crimson Starfall Arrow
35gp/1  Stock:31        Enraging Arrow
21gp/1  Stock:27        Web Arrow
```

## Questions/Issues
---------------------
Please raise any issues or questions as issues on the github project.

## Contributing
---------------------
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

There aren't any right now but if I do create tests, please make sure to update tests as appropriate.

## License
---------------------
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)