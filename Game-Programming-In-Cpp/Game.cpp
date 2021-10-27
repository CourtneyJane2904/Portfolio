#include "Game.h"
#include <cmath>
#include <cstdlib>
#include <time.h>
#include <iostream>

Game::Game()
{
	mWindow = nullptr;
	mIsRunning = true;
	// give ball a default center position- an axis starting at 0 would mean the center is at 512, 384 at a 1024 x 768 resolution
	mBallPos = {512,384};
	// give paddle a default center-left position- y should be center but x needs to be near to starting value
	mPaddlePos = {10,384};
	mTicksCount, mPaddleDir = 0;
	// ball starts out moving -200 pixels a second in x direction and 235 pixels a second in y direction
	mBallVel = { 150.0f, 185.0f };
};

bool Game::Init()
{
	/*
	* return True if initialization succeeds, false otherwise
	*/

	// initialize the video subsystem of the SDL library
	int sdlResult = SDL_Init(SDL_INIT_VIDEO);

	// if sdlResult is a value other than 0
	if (sdlResult) {
		// log error and return false
		SDL_Log("Unable to initialize SDL, error: %s", SDL_GetError());
		return false;
	}
	else 
	{
		// proceed to create window
		mWindow = SDL_CreateWindow(
			"Game Programming in C++ (Chapter 1)", // window title
			100, // top left x-coord of window
			100, // top left y-coord of window
			1024, // window width
			768, // height of window
			0 // flags, 0 means none
		);

		// if SDL_CreateWindow returns a nullptr, initialization has failed- return false
		if (!mWindow) {
			SDL_Log("Unable to initialize SDL, error: %s", SDL_GetError());
			return false;
		}
		else {
			// CreateWindow was a success, we can now check CreateRenderer
			mRenderer = SDL_CreateRenderer(
				mWindow, // window to create renderer for
				-1,
				SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC
			);
			// Alike to above- return false if a nullptr was returned
			if (!mRenderer) {
				SDL_Log("Unable to initialize SDL, error: %s", SDL_GetError());
				return false;
			};

			// Exercise 1.2: change code in Game::Init to initialize the positions and velocities of several balls
			// can use mBallVel and mBallPos as base values for this
			// set seed for random function- the default is 1 meaning balls would be the same each time
			srand(time(0));
			// randomly generate 1-5 balls
			int ballTotal = rand() % 5 + 1;
			// for ball in balls, generate diverse mBallPos and mBallVel
			for (int i = 0; i <= ballTotal; i++) {
				// make x-position of ball a random value between 100 and 1009
				mBallPos.x = rand() % (1024 - thickness) + 100;
				// make y-position of ball a random value between 100 and 754
				mBallPos.y = rand() % (768 - thickness) + 100;
				// make x-velocity of ball a random value between -150 and 150
				mBallVel.x = rand() % 200 - 200;
				// make y-velocity of ball a random value between -185 and 185
				mBallVel.y = rand() % 235 -235;
				// insert randomly generated velocity and ball position into allBalls
				allBalls.insert(allBalls.begin(), { mBallPos, mBallVel });
			};
		}
	};
	// there is alot of error checking above- it's probably easier to simply return true if an error wasn't encountered
	return true;
};

void Game::ShutDown()
{
	/* The opposite of Init- destroys the SDL_Window then closes SDL */
	SDL_DestroyWindow(mWindow);
	SDL_DestroyRenderer(mRenderer);
	SDL_Quit();
};

void Game::RunLoop()
{
	/* keeps running iterations of the game loop until IsRunning returns false */
	while (mIsRunning) { ProcIn(); UpdateGame(); GenOut(); };
};

void Game::ProcIn()
{
	SDL_Event evt;
	mPaddleDir = 0;
	// return true if there's an event in the queue
	while(SDL_PollEvent(&evt)){
		switch(evt.type){
			// if quit event found, shut the game down
			case SDL_QUIT: mIsRunning = false; break;
		}
	}

	// get state of keyboard
	const Uint8* state = SDL_GetKeyboardState(NULL);
	// also end loop if escape is pressed
	state[SDL_SCANCODE_ESCAPE] ? mIsRunning == false : true;

	// set mPaddleDir to -1 if paddle mvoes up and +1 if paddle moves down
	if (state[SDL_SCANCODE_UP]) mPaddleDir -= 1;
	if (state[SDL_SCANCODE_DOWN]) mPaddleDir += 1;

}

void Game::GenOut()
{
	/*
	* clear the back buffer to a color (games current buffer)
	* draw game scene
	* swap front and back buffer
	*/

	// a constant pointer to an integer

	// clear back buffer by specifying a colour
	SDL_SetRenderDrawColor(
		mRenderer,
		0, // R
		0, // G
		255, // B
		255 // A
	);

	// clear the back buffer to the current draw color
	SDL_RenderClear(mRenderer);

	// change draw color to white for drawing paddle and ball
	SDL_SetRenderDrawColor(
		mRenderer,
		255, // R
		255, // G
		255, // B
		255 // A
	);
	SDL_Rect tWall{
		0, // top left x
		0, // top left y
		1024, // width
		thickness // height
	};

	SDL_Rect bWall{
		0, // top left x
		768 - thickness, // top left y
		1024, // width
		thickness // height
	};

	SDL_Rect rWall{
		1024 - thickness, // top left x
		thickness, // top left y
		thickness, // width
		1024 // height
	};

	// specify dimensions of rectangle to be drawn at the top of the screen
	SDL_Rect paddle{
		static_cast<int>(mPaddlePos.x - thickness / 2), // top left x
		static_cast<int>(mPaddlePos.y - thickness / 2), // top left y
		thickness, // width
		80 // height
	};

	// convert from center coordindates to top left by subtracting half the width/height from x and y
	for (Ball b : allBalls) {
		SDL_Rect ball{
			static_cast<int>(b.ballPos.x - thickness / 2),
			static_cast<int>(b.ballPos.y - thickness / 2),
			thickness,
			thickness
		};
		SDL_RenderFillRect(mRenderer, &ball);
	}

	SDL_RenderFillRect(mRenderer, &rWall);
	SDL_RenderFillRect(mRenderer, &bWall);
	SDL_RenderFillRect(mRenderer, &tWall);
	// draw wall, passing in SDL_Rect by pointer
	SDL_RenderFillRect(mRenderer, &paddle);

	// swap the front and back buffers
	SDL_RenderPresent(mRenderer);
};

void Game::UpdateGame()
{
	// delta time is the difference in ticks from the last frame converted to seconds
	float deltaTime = (SDL_GetTicks() - mTicksCount) / 1000.0f;
	const int paddleH = 80;
	// update tick count for next frame
	mTicksCount = SDL_GetTicks();
	// update the paddle based on delta time
	if (mPaddleDir) { 
		mPaddlePos.y += mPaddleDir * 300.0f * deltaTime; 
		// ensure paddle doesn't move off-screen
		if (mPaddlePos.y < (paddleH / 2.0f - thickness)) mPaddlePos.y = paddleH / 2.0f + thickness;
		else if (mPaddlePos.y > (768.0f - paddleH / 2.0f - thickness)) mPaddlePos.y = 768.0f - paddleH / 2.0f - thickness;
	};
	// for ball in allBalls
	// loop through references to update the value in realtime (using ambersand); if this isn't desired, omitting the ambersand results in a copy of the object being made
	for (Ball &v : allBalls)
	{
		// handle ball collision with top wall- reverse y direction of ball in event of collision
		if (v.ballPos.y <= thickness && v.ballVel.y < 0.0f) v.ballVel.y *= -1; 
		// reverse bball if it hits the starting point of the right wall and is moving towards the right wall (a positive x velocity)
		else if (v.ballPos.x >= (1024 - thickness) && v.ballVel.x >= 0.0f) v.ballVel.x *= -1;
		// reverse if ball hits the starting point of bottom wall and the ball is moving towards the bottom wall (positive y velocity)
		else if (v.ballPos.y >= (768 - thickness) && v.ballVel.y >= 0.0f) v.ballVel.y *= -1;
		// calc difference between y position of the ball and y position of paddle
		int diff = abs(v.ballPos.y - mPaddlePos.y);
		// handle ball collision with bottom and right walls
		// if y-diff is small enough and
		if (paddleH > diff / 2.0f &&
			// ball is at correct x position and
			v.ballPos.x <= 25.0f && v.ballPos.x >= 20.0f &&
			// ball is moving to the left
			v.ballPos.x >= 20.0f)
		{
			v.ballVel.x *= -1.0f;
		};
		v.ballPos.x += v.ballVel.x * deltaTime;
		v.ballPos.y += v.ballVel.y * deltaTime;
	};

};
