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
  
 #### Uniform Cost Search
  Located in 'Search.py -> `uniformCostSearch(problem)`
  to test search agent run: 
  ```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
  ```
  
 #### A*
  Located in 'Search.py -> `aStarSearch(problem)`
  to test search agent run: 
  ```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
  ```
  
 #### Corners Problem
  Located in 'searchAgents.py' 
  to test search agent run: 
  ```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
  ```
  
  
 #### Corner Heuristic
  Located in 'searchAgents.py' 
  to test search agent run: 
  ```
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
  ```
  
  
 #### Food Heuristic
  Located in 'searchAgents.py' 
  to test search agent run: 
  ```
python pacman.py -l testSearch -p AStarFoodSearchAgent
  ```


#### Suboptimal Search
  Located in 'searchAgents.py' 
  to test search agent run: 
  ```
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
  ...

