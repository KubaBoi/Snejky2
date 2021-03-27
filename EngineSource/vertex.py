from Engine.vector import Vector
import math

class Vertex:
    def __init__(self, position):
        self.Position = position
        self.projection = None
        self.distanceFromProjection = 0

    def update(self, camera):
        self.projection = self.getProjection(camera)

    def getProjection(self, camera):
        self.isInFront = self.isInFrontOfCamera(camera)
        x, y = self.findProjection(camera)
        return (x, y)

    #vypocita a vrati souradnice vykresleni na obrazovce
    def findProjection(self, camera):
        G = self.findG(camera)

        g = G.newVector(camera.S)
        if (g.selfLength() != 0):
            #uhel mezi g a u (u S)
            alpha = g.angle(camera.u)

            #uhel mezi g a kolmici na u
            beta = math.pi - (math.pi/2 + alpha)

            x = abs(g.selfLength() * math.sin(alpha))*1000
            y = abs(g.selfLength() * math.sin(beta))*1000

            angle1 = g.angle(camera.u)
            angle2 = g.angle(camera.r)
            
            #zmena plusy a minusy u y
            if (0 <= angle1 <= math.pi/2 and 0 <= angle2 <= math.pi/2): #I. kvadrant
                x = camera.x + x
                y = camera.y + y
            elif (0 <= angle1 <= math.pi/2 and angle2 >= math.pi/2): #II. kvadrant
                x = camera.x - x
                y = camera.y + y      
            elif (angle1 >= math.pi/2 and angle2 >= math.pi/2): #III. kvadrant
                x = camera.x - x
                y = camera.y - y
            elif (angle1 >= math.pi/2 and 0 <= angle2 <= math.pi/2): #IV. kvadran               
                x = camera.x + x
                y = camera.y - y
                
        else:
            x = camera.x #tady byla zmena... byly tu 0
            y = camera.y
            
        x = int(x)
        y = int(y)
        return (x, y)

    #vrati bod, ve kterem se protina primka pohledu s rovinou promitani
    def findG(self, camera):
        """c1 = self.Position.x
        c2 = self.Position.y
        c3 = self.Position.z
        
        u1 = camera.u.x
        u2 = camera.u.y
        u3 = camera.u.z

        r1 = camera.r.x
        r2 = camera.r.y
        r3 = camera.r.z
        
        s1 = camera.S.x
        s2 = camera.S.y
        s3 = camera.S.z"""

        if (self.isInFront):
            g1 = camera.Position.x - self.Position.x
            g2 = camera.Position.y - self.Position.y
            g3 = camera.Position.z - self.Position.z
        else:
            g1 = self.Position.x
            g2 = 0
            g3 = self.Position.z

        #miluju matlab
        try:
            t = (-(self.Position.x*camera.r.y*camera.u.z - self.Position.x*camera.r.z*camera.u.y 
                - self.Position.y*camera.r.x*camera.u.z + self.Position.y*camera.r.z*camera.u.x 
                + self.Position.z*camera.r.x*camera.u.y - self.Position.z*camera.r.y*camera.u.x
                   + camera.r.x*camera.S.y*camera.u.z - camera.r.x*camera.S.z*camera.u.y - camera.r.y*camera.S.x*camera.u.z 
                   + camera.r.y*camera.S.z*camera.u.x + camera.r.z*camera.S.x*camera.u.y - camera.r.z*camera.S.y*camera.u.x)/
                 (g1*camera.r.y*camera.u.z - g1*camera.r.z*camera.u.y - g2*camera.r.x*camera.u.z 
                 + g2*camera.r.z*camera.u.x + g3*camera.r.x*camera.u.y - g3*camera.r.y*camera.u.x))
        except:
            t = 0

        #speak
        #print((c1 + t*g1, c2 + t*g2, c3 + t*g3))

        return Vector(self.Position.x + t*g1,
                      self.Position.y + t*g2,
                      self.Position.z + t*g3)

    def isInFrontOfCamera(self, camera):
        a = self.Position.distance(camera.S)
        ac = self.Position.distance(camera.Position)
        if (a <= ac): return True

        return False

    #metoda vraci upravene souradnice vertexu, ktery je za kamerou
    def fromBack(self, side, bigger, lower):
        bigger *= 50
        lower *= 50
        l = math.sqrt(bigger*bigger + lower*lower)
        if (l > side):
            return math.sqrt(l*l - side*side), side
        else:
            return 0, 0