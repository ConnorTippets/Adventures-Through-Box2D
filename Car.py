from Box2D.examples.framework import (Framework, Keys, main)
from Box2D import (b2DistanceJointDef, b2EdgeShape, b2FixtureDef,
                   b2PolygonShape, b2CircleShape, b2RevoluteJointDef, b2_pi)
from math import inf

class Car(Framework):
    name = "Car"
    description = "Car"
    wheels = []

    def __init__(self):
        super(Car, self).__init__()

        ground = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-40, 0), (40, 0)])
        )
        fixtureA = b2FixtureDef(shape=b2PolygonShape(box=(4,1)), density=5, friction=2.5)
        fixtureB = b2FixtureDef(shape=b2CircleShape(radius=1.35), density=5, friction=2.5)
        car = self.world.CreateDynamicBody(position=(-30, 18), fixtures=fixtureA)
        self.wheels.append(self.world.CreateDynamicBody(position=(-32, 19.4), angle=0.5 ** b2_pi, fixtures=fixtureB))
        self.wheels.append(self.world.CreateDynamicBody(position=(-28, 19.4), angle=0.5 ** b2_pi, fixtures=fixtureB))
        for bodyI in enumerate(self.wheels):
            bodyI = bodyI[0]
            r = b2RevoluteJointDef(bodyA=self.wheels[bodyI], bodyB=car, anchor=[self.wheels[bodyI].position[0], self.wheels[bodyI].position[1]-0.6], lowerAngle = 0.5 ** b2_pi, upperAngle = -0.5 ** b2_pi, enableLimit=True, maxMotorTorque = 10, motorSpeed=5, enableMotor=True)
            jr = self.world.CreateJoint(r)

    def Keyboard(self, key):
        if key == Keys.K_d:
            for wheel in self.wheels:
                wheel.linearVelocity = (5,0)
        elif key == Keys.K_a:
            for wheel in self.wheels:
                wheel.linearVelocity = (-5,0)
main(Car)
