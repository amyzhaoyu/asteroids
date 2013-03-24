ASTEROIDS Homework - CIS 399-04
Amy (Zhao) Yu
April 1, 2008


*************************************************
*						*
*    Provided files included with submission    *
*						*
*************************************************

asteroid_small.bmp
background.jpg
big_asteroid.bmp
falcon.bmp
shot.bmp
asteroids.py

*************************************************
*						*
*		Running the program		*
*						*
*************************************************
To run the game, simply run asteroids.py (no arguments are necessary).

From the command line type: python asteroids.py


*************************************************
*						*
*  Object and Method Descriptions: asteroid.py	*
*						*
*************************************************
Global variables: GAME_WIDTH, GAME_HEIGHT

Asteroid:

__init__(self, background, screen, size, x, y)
load appropriate images depending on size parameter (1 = small, 2 = large), set background, screen, and x, y positions (if size = 1 otherwise set random x and y), set speed to 1.5

update(self, asteroids, shots)
move asteroid across screen, check for collisions with shot and either break/destroy asteroid as appropriate. returns dirtyRects to be updated

draw(self)
draw asteroid onto the screen

Shot:

__init__(self, background, screen, angle, x, y)
load shot image, set background, screen, and x, y positions. set speed to 4.00

update(self)
move shot across the screen, returns dirtyRecs to be updated

draw(self)
draws shot onto the screen

Ship:

__init__(self, background, screen)
load ship image, set background and screen, initialize speed, angle, and rotation to 0, set initial position to center of screen

get_input(self, event, asteroids, shots)
get key pressed, move/accelerate/decelerate ship, or fire shots as appropriate, returns a rect to be updated if the user presses ESC to move the ship

update(self)
update self.rect as the ship moves across the playing field, decelerate the ship slowly (if nothing happens, the ship decelerates along its current vector)

draw(self)
draws ship onto the screen

simpleGame:

__init__(self)
initializes new game - set dimensions, captions, background image, clock, new list of asteroids containing 2 big asteroids, empty list of shots, level = 1, create a new Ship

updateBackground(self, dirtyRects)
paint over dirtyRects with background

eventLoop(self)
update Ship, asteroids and shots as game is being played, introduce new level when all asteroids at current level have been destroyed

drawBackground
draws the background

*************************************************
*						*
*		  Game Design			*
*						*
*************************************************
Play Instructions:

The game begins with 2 asteroids that enter the playing field from a random side of the game window on a random vector. The player's ship is originally positioned in the middle of the screen facing to the right. 

To rotate the ship, press the LEFT and RIGHT arrow buttons. To accelerate the ship along its current vector, press the UP arrow button. To decelerate the ship along its current vector, press the DOWN arrow. To teleport the ship to a random location on the playing field, press ESC. To shoot an asteroid, aim the ship's front at the desired asteroid and release a shot by pressing SPACE. Players have unlimited numbers of shots. 

When a large asteroid is hit by a shot, it breaks up into three smaller asteroids. When a small asteroid is hit by a shot, it is destroyed and disappears off the playing field. When all the asteroids on the playing field have been destroyed, the player automatically moves up a level and more large asteroids appear. At level 1, the player encounters two asteroids, at level 2, 3 asteroids, etc. etc. Each new level starts with one more large asteroid than the previous level. 

When the ship hits either an asteroid or a shot, the game automatically exits.

Close the window to quit the game.

*************************************************
*						*
*		  Miscellaneous			*
*						*
*************************************************

For debugging purposes, as the event loop runs, the game prints out:

* starting location and angle of the asteroids
* location, angle and speed of the ship
* key events when a key is pressed
* messages when a shot is fired or when the ship collides with an asteroid or shot
* the contents of the Asteroids list when an asteroid is removed
