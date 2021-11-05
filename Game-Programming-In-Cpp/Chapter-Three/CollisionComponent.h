#pragma once
#include "CircleComponent.h"
#include "Actor.h"
#include <vector>

// inherit public members from CircleComponent
class CollisionComponent
{
	// check if actor collides with actor passed to constructor
	// this is done by making the two actors circles 
	// then create a vector between the two centers and calculate magnitude of vector
		// and compare against sum of two circle's radii
			// if magnitude/distance is less than sum of the circles radii, there's a collision
	public:
		// constructor- pass in actor to check for collision against
		CollisionComponent(std::vector<class Actor*> actors);

		// returns true if collision is detected
		bool CollisionDetected();
	private:
		// create circle component from two actors
		class CircleComponent* actorAsCircle;
		std::vector<CircleComponent*> actorsAsCircles;
		Vector2 distanceBetweenCenters;
};