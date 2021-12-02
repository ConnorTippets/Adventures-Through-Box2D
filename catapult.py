from Box2D.examples.framework import (Framework, Keys, main)
from Box2D import (b2DistanceJointDef, b2EdgeShape, b2FixtureDef,
                   b2PolygonShape, b2CircleShape, b2RevoluteJointDef, b2_pi)
from math import inf

class Catapult(Framework):
    name = "Catapult"
    description = "This demonstrates the physics of a catapult"
    bodies = []
    joints = []

    def __init__(self):
        super(Catapult, self).__init__()

        ground = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-2000, 0), (2000, 0)])
        )

        fixtureA = b2FixtureDef(shape=b2PolygonShape(box=(12, 1)), density=0.5, friction=1)
        fixtureB = b2FixtureDef(shape=b2PolygonShape(box=(0.5, 0.5)), density=3, friction=1)
        fixtureC = b2FixtureDef(shape=b2PolygonShape(box=(3,3)), density=5, friction=1.5)
        self.bodies.append(self.world.CreateBody(shapes=b2PolygonShape(box=(3, 12)), position=(0,12)))
        self.bodies.append(self.world.CreateDynamicBody(position=(0,24), fixtures=fixtureA))
        [self.bodies.append(self.world.CreateDynamicBody(position=(10,6), fixtures=fixtureB)), self.bodies.append(self.world.CreateDynamicBody(position=(16,6), fixtures=fixtureC))]
        r = b2RevoluteJointDef(bodyA=self.bodies[0], bodyB=self.bodies[1], anchor=self.bodies[1].worldCenter, lowerAngle=-0.9**b2_pi, upperAngle=0.9**b2_pi, enableLimit=True)
        jr = self.world.CreateJoint(r)
        self.joints.append(jr)
main(Catapult)
        
