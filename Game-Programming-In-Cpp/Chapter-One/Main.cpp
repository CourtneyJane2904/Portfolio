#include "Game.h"

int main(int argc, char ** argv)
{
	// create instance of Game class
	Game game;
	// attempt to initialize the game, storing the result in bool variable success
	bool success = game.Init();
	// if initialization was a success, begin game loop, else shut the game down
	success ? game.RunLoop() : game.ShutDown();
	return 0;
}