// ----------------------------------------------------------------
// From Game Programming in C++ by Sanjay Madhav
// Copyright (C) 2017 Sanjay Madhav. All rights reserved.
// 
// Released under the BSD License
// See LICENSE in root directory for full details.
// ----------------------------------------------------------------

#include "Ship.h"
#include "CollisionComponent.h"
#include "InputComponent.h"
#include "Game.h"
#include "Actor.h"
#include "Laser.h"
#include <ctime>

Ship::Ship(Game* game)
	:Actor(game)
	,mLaserCooldown(0.0f)
{
	// Create a sprite component
	sc->SetTexture(game->GetTexture("Assets/Ship.png"));
	// Create an input component and set keys/speed
	InputComponent* ic = new InputComponent(this);
	ic->SetForwardKey(SDL_SCANCODE_W);
	ic->SetBackKey(SDL_SCANCODE_S);
	ic->SetClockwiseKey(SDL_SCANCODE_A);
	ic->SetCounterClockwiseKey(SDL_SCANCODE_D);
	ic->SetMaxForwardSpeed(15000.0f);
	ic->SetMass(3.0f);
	ic->SetMaxAngularSpeed(Math::TwoPi);
}

void Ship::UpdateActor(float deltaTime)
{
	mLaserCooldown -= deltaTime;
	// if the ship was paused during the previous execution of this function
	if (paused)
	{
		SetState(EPaused);
		Vector2 centerPosit;
		centerPosit.x = 612 - 62;
		centerPosit.y = 384 - 62;
		// trigger a two second delay before making the ship visible again
		// additional logic would be needed here in a real game to account for collisions that occur when the ship is invisible
		Uint32 ticksCount = SDL_GetTicks() + 2000;
		while (!SDL_TICKS_PASSED(SDL_GetTicks(), ticksCount))
			;
		sc->SetTexture(GetGame()->GetTexture("Assets/Ship.png"));
		SetState(EActive);
		SetRotation(0);
		SetPosition(centerPosit);
		paused = false;
	}
	// test collision of all asteroids
	for (auto ast : GetGame()->GetAsteroids())
	{
		// if asteroid has collided
		if (AsteroidCollision(ast))
		{
			SetState(EPaused);
			Vector2 newPos = ast->GetPosition();
			// this moves the colliding asteroid 150 along the x and y axis, avoiding repeating collisions
			// as the asteroids wrap around this can be done
			newPos.x += 150;
			newPos.y += 150;
			ast->SetPosition(newPos);
			// pause the ship
			// prepare the center position
			
			// move ship to middle of screen
			sc->SetTexture(nullptr);
			// set state back to active (visibility is updated when function next executed)
			// set paused to true
			paused = true;
			SetState(EActive);
			break;
		}
	}
}

void Ship::ActorInput(const uint8_t* keyState)
{
	if (keyState[SDL_SCANCODE_SPACE] && mLaserCooldown <= 0.0f)
	{
		// Create a laser and set its position/rotation to mine
		Laser* laser = new Laser(GetGame());
		laser->SetPosition(GetPosition());
		laser->SetRotation(GetRotation());

		// Reset laser cooldown (half second)
		mLaserCooldown = 0.5f;
	}
}

bool Ship::AsteroidCollision(class Asteroid* ast)
{
	// create a collision component
	std::vector<Actor*> actors = { ast, this };
	CollisionComponent* cc = new CollisionComponent(actors);
	return cc->CollisionDetected();
}
