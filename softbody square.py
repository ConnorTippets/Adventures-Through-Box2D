from Box2D.examples.framework import (Framework, Keys, main)
from Box2D import (b2DistanceJointDef, b2EdgeShape, b2FixtureDef, b2PolygonShape, b2_pi, b2RevoluteJointDef)
from Box2D import b2Vec2 as v2

class SoftbodyS(Framework):
    name = "Softbody Test"
    description = "This demonstrates many softbody examples"
    linebodies = []
    squbodies = []
    joints = []

    def __init__(self):
        super(SoftbodyS, self).__init__()

        # The ground
        ground = self.world.CreateBody(
            shapes=b2EdgeShape(vertices=[(-40, 0), (40, 0)])
        )

        fixture = b2FixtureDef(shape=b2PolygonShape(box=(0.5, 0.5)), density=5, friction=0.2)
        col = self.world.CreateBody(shapes=b2PolygonShape(box=(0.5, 0.5)), position=(0, 40))
        cos = self.world.CreateDynamicBody(position=(6, 9), fixtures=fixture)

        for pos in [i+1 for i in range(20, 39)]:
            self.linebodies.append(self.world.CreateDynamicBody(position=(0, pos),fixtures=fixture))
        self.squbodies.append(self.world.CreateDynamicBody(position=(5, 10),fixtures=fixture))
        self.squbodies.append(self.world.CreateDynamicBody(position=(6, 10),fixtures=fixture))
        self.squbodies.append(self.world.CreateDynamicBody(position=(7, 10),fixtures=fixture))
        self.squbodies.append(self.world.CreateDynamicBody(position=(7, 9),fixtures=fixture))
        self.squbodies.append(self.world.CreateDynamicBody(position=(7, 8),fixtures=fixture))
        self.squbodies.append(self.world.CreateDynamicBody(position=(6, 8),fixtures=fixture))
        self.squbodies.append(self.world.CreateDynamicBody(position=(5, 8),fixtures=fixture))
        self.squbodies.append(self.world.CreateDynamicBody(position=(5, 9),fixtures=fixture))
        
        for bodyI in enumerate(self.linebodies):
            bodyI = bodyI[0]
            if not bodyI == len(self.linebodies)-1:
                r = b2RevoluteJointDef(bodyA=self.linebodies[bodyI], bodyB=self.linebodies[bodyI+1], anchor=self.linebodies[bodyI+1].worldCenter)
                jr = self.world.CreateJoint(r)
                self.joints.append(jr)
            else:
                break
        for bodyI in enumerate(self.squbodies):
            bodyI = bodyI[0]
            if self.squbodies[bodyI].position in (v2(5, 10), v2(7, 10), v2(7, 8), v2(5, 8)):
                r = b2DistanceJointDef(bodyA=self.squbodies[bodyI], bodyB=cos, anchorA=self.squbodies[bodyI].worldCenter, anchorB=cos.worldCenter)
                jr = self.world.CreateJoint(r)
                self.joints.append(jr)
            if not bodyI == len(self.squbodies)-1:
                r = b2RevoluteJointDef(bodyA=self.squbodies[bodyI], bodyB=self.squbodies[bodyI+1], anchor=self.squbodies[bodyI+1].worldCenter)
                jr = self.world.CreateJoint(r)
                self.joints.append(jr)
            else:
                break
        r = b2DistanceJointDef(bodyA=self.linebodies[len(self.linebodies)-1], bodyB=col, anchorA=self.linebodies[len(self.linebodies)-1].worldCenter, anchorB=col.worldCenter)
        rt = b2RevoluteJointDef(bodyA=self.squbodies[len(self.squbodies)-1], bodyB=self.squbodies[0], anchor=self.squbodies[0].worldCenter)
        jr = self.world.CreateJoint(r)
        jrt = self.world.CreateJoint(rt)
        self.joints.append(jr)
        self.joints.append(jrt)
main(SoftbodyS)
