from Box2D.examples.framework import (Framework, Keys, main)
from Box2D import (b2DistanceJointDef, b2EdgeShape, b2FixtureDef,
                   b2PolygonShape, b2CircleShape, b2RevoluteJointDef, b2_pi)
import Box2D
from math import log, inf

class Test(Framework):
    name = "Test"
    description = "Test"
    size = 80
    bodies = []
    joints = []

    def __init__(self):
        super(Test, self).__init__()
        size = self.size

        # The ground
        ground = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-(size), 0), (size, 0)])
        )
        wallo = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-(size), 0), (-(size), size)])
        )
        wallt = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(size, 0), (size, size)])
        )

        fixtureA = b2FixtureDef(shape=b2PolygonShape(box=(0.5, 0.5)), density=1, friction=0)
        fixtureB = b2FixtureDef(shape=b2CircleShape(radius=[(round(size/24) if size >= 40 else round(size/12)) if size >= 10 else (round(size/2.5))][0]), density=1, friction=0)
        edgeo = self.world.CreateBody(shapes=b2PolygonShape(box=(0.5,0.5)), position=(-(size), size))
        edget = self.world.CreateBody(shapes=b2PolygonShape(box=(0.5,0.5)), position=(size, size))

        for pos in [i+1 for i in range(-(size), size)]:
            self.bodies.append(self.world.CreateDynamicBody(position=(pos, size),fixtures=fixtureA))
        self.bodies.append(self.world.CreateDynamicBody(position=(0, size+20),fixtures=fixtureB))

        deo = b2DistanceJointDef(bodyA=edgeo, bodyB=self.bodies[0], anchorA=edgeo.worldCenter, anchorB=self.bodies[0].worldCenter)
        det = b2DistanceJointDef(bodyA=edget, bodyB=self.bodies[len(self.bodies)-2], anchorA=edget.worldCenter, anchorB=self.bodies[len(self.bodies)-2].worldCenter)
        [self.world.CreateJoint(deo), self.world.CreateJoint(det)]
        
        for bodyI in enumerate(self.bodies):
            bodyI = bodyI[0]
            if not bodyI == len(self.bodies)-2:
                r = b2RevoluteJointDef(bodyA=self.bodies[bodyI], bodyB=self.bodies[bodyI+1], anchor=self.bodies[bodyI+1].worldCenter)
                jr = self.world.CreateJoint(r)
                self.joints.append(jr)
            else:
                break
main(Test)
