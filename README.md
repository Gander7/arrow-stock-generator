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

```
## Mundane Arrows ##
25gp/1  Stock:34        Adamantium Arrow
1gp/10  Stock:10        Broadhead Arrow
1gp/10  Stock:21        Hammerhead Arrow
1gp/20  Stock:240       Normal Arrow
10gp/1  Stock:18        Silvered Arrow
1gp/1   Stock:26        Smoking Arrow

## Common Arrows ##
8gp/1   Stock:23        Acid Arrow X
12gp/1  Stock:33        Cold Arrow X
9gp/1   Stock:7 Healing Arrow X
6gp/1   Stock:8 Lightning Arrow X
9gp/1   Stock:33        Mind Piercer Arrow X
11gp/1  Stock:34        Necrotic Arrow X
12gp/1  Stock:34        Radiant Arrow X
11gp/1  Stock:31        Siege Arrow X
13gp/1  Stock:27        Sleep Arrow X

## Uncommon Arrows ##
20gp/1  Stock:17        Enraging Arrow
20gp/1  Stock:19        Sand Arrow X
36gp/1  Stock:33        Web Arrow
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