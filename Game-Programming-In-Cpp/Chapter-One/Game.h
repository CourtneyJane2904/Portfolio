#pragma once
#include "SDL2\include\SDL.h"
#include <vector>

// a 2d vector structure for use in recording the positions of objects
struct Vector2 { float x, y; };
// excercise 1.2: create a Ball struct that contains two Vector2- one for position, one for velocity
struct Ball { Vector2 ballPos, ballVel; };
// thickness needs to be used in multiple game methods so put here out of laziness
const int thickness = 15;

class Game
{
	/*
	* Create instance of game class to interface with game
	*/
	public:
		Game();
		// init game
		bool Init();
		// run game loop until game is over
		void RunLoop();
		// shut game down
		void ShutDown();

	private:
		void ProcIn();
		void UpdateGame();
		void GenOut();

		// Create a window with SDL, mWindow is a pointer to the window
		SDL_Window* mWindow;
		// mRenderer is a pointer to a rendering functionalty
		SDL_Renderer* mRenderer;
		// return whether the game is still running
		bool mIsRunning;
		// 2d vectors to record the position of the ball and paddle
		Vector2 mBallPos, mPaddlePos, mBallVel;
		// unsigned int to record ticks count 
		Uint32 mTicksCount;
		int mPaddleDir;
		// exercise 1.2: create a std::vector<Ball> member variable to store different balls
		// std::vector is a sequence container that encapsulates dynamic sized arrays
		std::vector<Ball> allBalls;
};