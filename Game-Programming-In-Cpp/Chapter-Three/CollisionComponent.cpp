#include "CollisionComponent.h"
#include <iostream>

CollisionComponent::CollisionComponent(std::vector<Actor*> actors)
{
	// create circle from provided actors for collision check
	for (Actor* actor : actors) actorsAsCircles.emplace_back(new CircleComponent(actor));
};

bool CollisionComponent::CollisionDetected()
{
	// check if two actors collide and return true if so
	
	// create a vector between the two centers and calculate magnitude of vector
	// given points p and q, treat as vectors and peform vector subtraction
	
	// subtract two vectors to find vector between two points (e.g. distabce between teo points)
	// vector between two centers
	Vector2 centersVector = actorsAsCircles[0]->GetCenter() - actorsAsCircles[1]->GetCenter();
	// magnitude of vector between two centers 
	int vectMag = centersVector.LengthSq();
	// 
	actorsAsCircles[0]->SetRadius(32.0f);
	actorsAsCircles[1]->SetRadius(32.0f);
	int radiiDiff = pow((actorsAsCircles[0]->GetRadius() + actorsAsCircles[1]->GetRadius()), 2.0);
	// to check for intersection, compare the distance of the vector to the sum of the circle's radii
	return vectMag <= radiiDiff;
}