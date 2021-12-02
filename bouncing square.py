from Box2D.examples.framework import (Framework, Keys, main)
from Box2D import (b2DistanceJointDef, b2EdgeShape, b2FixtureDef,
                   b2PolygonShape, b2CircleShape, b2RevoluteJointDef, b2_pi)
from math import inf

class Bouncing(Framework):
    name = "Bouncing Squares"
    description = "basically bouncing squares"

    def __init__(self):
        super(Bouncing, self).__init__()

        ground = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-40, 0), (40, 0)])
        )
        
        # Fixtures
        corner1 = self.world.CreateBody(shapes=b2PolygonShape(box=(0.5, 0.5)), position=(-30, 30))
        corner2 = self.world.CreateBody(shapes=b2PolygonShape(box=(0.5, 0.5)), position=(-30, 20))
        corner3 = self.world.CreateBody(shapes=b2PolygonShape(box=(0.5, 0.5)), position=(-20, 20))
        corner4 = self.world.CreateBody(shapes=b2PolygonShape(box=(0.5, 0.5)), position=(-20, 30))
        bouncers = b2FixtureDef(shape=b2PolygonShape(box=(0.5, 0.5)), density=5, friction=1)
        box = b2FixtureDef(shape=b2PolygonShape(box=(1,1)), density=5, friction=1)

        # Define positions
        positions1 = [(-30, 29), (-30, 28), (-30, 27), (-30, 26), (-30, 25), (-30, 24), (-30, 23), (-30, 22), (-30, 21)]
        positions2 = [(-29, 20), (-28, 20), (-27, 20), (-26, 20), (-25, 20), (-24, 20), (-23, 20), (-22, 20), (-21, 20)]
        positions3 = [(-20, 21), (-20, 22), (-20, 23), (-20, 24), (-20, 25), (-20, 26), (-20, 27), (-20, 28), (-20, 29), (-20, 30)]
        positions4 = [(-21, 30), (-22, 30), (-23, 30), (-24, 30), (-25, 30), (-26, 30), (-27, 30), (-28, 30), (-29, 30)]

        # Bodies
        self.bodies1 = []
        self.bodies2 = []
        self.bodies3 = []
        self.bodies4 = []
        for pos in positions1:
            self.bodies1.append(self.world.CreateDynamicBody(position=pos, fixtures=bouncers))
        for pos in positions2:
            self.bodies2.append(self.world.CreateDynamicBody(position=pos, fixtures=bouncers))
        for pos in positions3:
            self.bodies3.append(self.world.CreateDynamicBody(position=pos, fixtures=bouncers))
        for pos in positions4:
            self.bodies4.append(self.world.CreateDynamicBody(position=pos, fixtures=bouncers))
        player = self.world.CreateDynamicBody(position=(-25, 25), fixtures=box)

        # Joints
        for bodyI in enumerate(self.bodies1):
            bodyI = bodyI[0]
            if not bodyI == len(self.bodies1)-1:
                r = b2RevoluteJointDef(bodyA=self.bodies1[bodyI], bodyB=self.bodies1[bodyI+1], anchor=self.bodies1[bodyI+1].worldCenter)
                jr = self.world.CreateJoint(r)
            else:
                break
        for bodyI in enumerate(self.bodies2):
            bodyI = bodyI[0]
            if not bodyI == len(self.bodies2)-1:
                r = b2RevoluteJointDef(bodyA=self.bodies2[bodyI], bodyB=self.bodies2[bodyI+1], anchor=self.bodies2[bodyI+1].worldCenter)
                jr = self.world.CreateJoint(r)
            else:
                break
        for bodyI in enumerate(self.bodies3):
            bodyI = bodyI[0]
            if not bodyI == len(self.bodies3)-1:
                r = b2RevoluteJointDef(bodyA=self.bodies3[bodyI], bodyB=self.bodies3[bodyI+1], anchor=self.bodies3[bodyI+1].worldCenter)
                jr = self.world.CreateJoint(r)
            else:
                break
        for bodyI in enumerate(self.bodies4):
            bodyI = bodyI[0]
            if not bodyI == len(self.bodies4)-1:
                r = b2RevoluteJointDef(bodyA=self.bodies4[bodyI], bodyB=self.bodies4[bodyI+1], anchor=self.bodies4[bodyI+1].worldCenter)
                jr = self.world.CreateJoint(r)
            else:
                break
        r1 = b2DistanceJointDef(bodyA=corner1, bodyB=self.bodies4[len(self.bodies4)-1], anchorA=corner1.worldCenter, anchorB=self.bodies4[len(self.bodies4)-1].worldCenter)
        r2 = b2DistanceJointDef(bodyA=corner1, bodyB=self.bodies1[0], anchorA=corner1.worldCenter, anchorB=self.bodies1[0].worldCenter)
        r3 = b2DistanceJointDef(bodyA=corner2, bodyB=self.bodies1[len(self.bodies1)-1], anchorA=corner2.worldCenter, anchorB=self.bodies1[len(self.bodies1)-1].worldCenter)
        r4 = b2DistanceJointDef(bodyA=corner2, bodyB=self.bodies2[0], anchorA=corner2.worldCenter, anchorB=self.bodies2[0].worldCenter)
        r5 = b2DistanceJointDef(bodyA=corner3, bodyB=self.bodies3[0], anchorA=corner3.worldCenter, anchorB=self.bodies3[0].worldCenter)
        r6 = b2DistanceJointDef(bodyA=corner3, bodyB=self.bodies2[len(self.bodies2)-1], anchorA=corner3.worldCenter, anchorB=self.bodies2[len(self.bodies2)-1].worldCenter)
        r7 = b2DistanceJointDef(bodyA=corner4, bodyB=self.bodies3[len(self.bodies3)-1], anchorA=corner4.worldCenter, anchorB=self.bodies3[len(self.bodies3)-1].worldCenter)
        r8 = b2DistanceJointDef(bodyA=corner4, bodyB=self.bodies4[0], anchorA=corner4.worldCenter, anchorB=self.bodies4[0].worldCenter)
        rs = [r1, r2, r3, r4, r5, r6, r7, r8]
        for r in rs:
            jr = self.world.CreateJoint(r)
main(Bouncing)
