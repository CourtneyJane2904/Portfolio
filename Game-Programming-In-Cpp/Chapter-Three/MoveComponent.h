// ----------------------------------------------------------------
// From Game Programming in C++ by Sanjay Madhav
// Copyright (C) 2017 Sanjay Madhav. All rights reserved.
// 
// Released under the BSD License
// See LICENSE in root directory for full details.
// ----------------------------------------------------------------

#pragma once
#include "Component.h"
#include "Math.h"
#include <vector>

class MoveComponent : public Component
{
	public:
		// Lower update order to update first
		MoveComponent(class Actor* owner, int updateOrder = 10);

		void Update(float deltaTime) override;
	
		float GetAngularSpeed() const { return mAngularSpeed; }
		float GetForwardSpeed() const { return mForwardSpeed; }
		void SetAngularSpeed(float speed) { mAngularSpeed = speed; }
		void SetForwardSpeed(float speed) { mForwardSpeed = speed; }

		// new member vars as per exercise 3.3
		float GetMass() const{ return mMass; }
		Vector2 GetForces() { return mForces; }
		Vector2 GetVel() { return mVel; }

		void SetMass(float m) { mMass = m; }
		void AddToForces(Vector2 force) { mForces += force; }
		void ClearForces() { mForces.x = 0; mForces.y = 0; }
		void SetVel(Vector2 vel) { mVel = vel; }
	private:
		// Controls rotation (radians/second)
		// a mass, sum of forces and velocity as member variables
		float mAngularSpeed; float mForwardSpeed; 
		float mMass = 2.00f;
		// force, acceleration, velocity and position all represented by vectors
		Vector2 mForces;
		Vector2 mVel;
		Vector2 mAccel;
};