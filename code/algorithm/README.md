# Algoritme

### greedy.py
The Greedy algorithm in this case means that each station must be connected to the nearest station. The starting station is random. An example is: The Hague Central: ["Delft": 13.0, "Gouda": 18.0, "Leiden Central": 12.0]. The Hague Central would then have to be connected with Leiden Central since it has the shortest travel time.

When this search algorithm has reached the maximum time frame of 2 hours, it is stored as 1 route. Then a new starting station (random) is searched for and the process is repeated. A line route is only created when all connections have been used with a maximum of 7 route. If this is not the case, it will start blank again.

### random.py
Since it is completely random, it must be taken into account that each station must be connected to the corresponded station. The first station is selected randomly with the Random module. Where 1 of the 22 train stations is chosen. From here, the algorithm must travel a route, whereby the stations can travel a valid route. For example, [Alkmaar, Hoorn] is a connection, however [Alkmaar, The Hague] is not a connection. So it is important that there is a Key-Value with the stations.
