# Berkeley Artificial Intellegience CS Course: Pac-Man Search 

## Topic 
Course project in Intro to AI focused on utilizing graph algorithms and seacrh heurestics for our Pac-man agent
`Dependencies` : `python 2.7` `util.py`

## Tasks
**`Search.py`** 
- Depth First Search 
- Breadth First Search
- Uniform Cost Search 
- A* Search 

**`SearchAgents.py`** 
- Corners Representation
- Corners Heuristic 
- Eating Food Hueristic 
- Suboptimal Search 


## Descriptions 
#### Depth First Search 
 Located in `Search.py` -> `depthFirstSearch(problem)` 
 To test search agent run: 
 ```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
 ```

#### Breadth First Search 
  Located in 'Search.py -> `bredthFirstSearch(problem)`
  to test search agent run: 
  ```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
  ```
  
  ...
