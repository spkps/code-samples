A .map file is an XML document containing a representation of a linked series of rooms, each of which may contain an object. Here's an example:
``` xml
<map>
 <room id="1" name="arboretum" east="2" />
 <room id="2" name="foyer" west="1" east="3"/>
 <room id="3" name="dungeon" west="2" south="4" north="5">
 <object name="rubber chicken"/>
 </room>
 <room id="4" name="solarium" north="3">
 <object name="pulley"/>
 </room>
 <room id="5" name="closet" west="6" south="3"/>
 <room id="6" name="dining room" east="5" north="7">
 <object name="banjo"/>
 </room>
 <room id="7" name="cinema" south="6">
 <object name="stapler"/>
 </room>
</map>
```
For each room the values of the attributes North, East, South, and West are the IDs of the room you find by moving in each one of those directions. 

For the example above room 1 is connected with room 2 with a door on its East wall. 

A .goal file is a plain text document containing, on the first line, a starting room name, and the name of a sought object on every following line. Here's an example:
```
arboretum
stapler
pulley
```
Write a command-line tool which accepts a .map file and a .goal file and outputs a route from the starting room that allows you to pick up all the sought objects, in the following format, including any unspecified objects that you happen to pick up along the way:
```
east
east
rubber chicken
south
pulley (1/2)
north
north
west
banjo
north
stapler (2/2)
```
