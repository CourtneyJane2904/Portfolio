// ----------------------------------------------------------------
// From Game Programming in C++ by Sanjay Madhav
// Copyright (C) 2017 Sanjay Madhav. All rights reserved.
// 
// Released under the BSD License
// See LICENSE in root directory for full details.
// ----------------------------------------------------------------

#include "MoveComponent.h"
#include "Actor.h"

MoveComponent::MoveComponent(class Actor* owner, int updateOrder)
:Component(owner, updateOrder)
,mAngularSpeed(0.0f)
,mForwardSpeed(0.0f)
{
	
}

void MoveComponent::Update(float deltaTime)
{
	if (!Math::NearZero(mAngularSpeed))
	{
		float rot = mOwner->GetRotation();
		rot += mAngularSpeed * deltaTime;
		mOwner->SetRotation(rot);
	}
	
	// change to calculate an acceleration from forces, a velocity from acceleration
	// and a position from velocity
	if (!Math::NearZero(mForwardSpeed))
	{
		// calc acceleration from forces (speed in this case)
		// turn speed into a force vector by multiplying the GetForward vector by the mForwardSpeed scalar
		Vector2 force = mOwner->GetForward() * mForwardSpeed;
		// add forward force to forces
		AddToForces(force);
		// position should initially be the current position of the ship
		Vector2 pos = mOwner->GetPosition();
		// calculate velocity from acceleration (the explicit technique of Euler integration) 
		// acceleration = force / mass
		mAccel = GetForces() * (1 / GetMass());
		// calculate velocity from acceleration (the implicit technique of Euler integration)
		SetVel(mAccel * deltaTime);
		// calc position using velocity
		pos += GetVel() * deltaTime;

		// (Screen wrapping code only for asteroids)
		if (pos.x < 0.0f) { pos.x = 1022.0f; }
		else if (pos.x > 1024.0f) { pos.x = 2.0f; }

		if (pos.y < 0.0f) { pos.y = 766.0f; }
		else if (pos.y > 768.0f) { pos.y = 2.0f; }

		mOwner->SetPosition(pos);
		ClearForces();
	}
}
