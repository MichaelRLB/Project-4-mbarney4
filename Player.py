from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import *
from CollideObjectBase import SphereCollideObject
from typing import Callable

class Player(SphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float, taskManager: Task, renderer: NodePath):
        super(Player, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 0.5)
        self.taskManager = taskManager
        self.renderer = renderer
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
        self.SetKeyBindings()
        #Call to control class.
    # Forward and backward thrusts (back thrusts still in development)
    def Thrust(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyThrust, 'forward-thrust')
        else:
            self.taskManager.remove('forward-thrust')
    def ApplyThrust(self, task):
        rate = 10
        trajectory = self.renderer.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont
    # Back thrust dosen't work if held down, only if mashed.
    def BackThrust(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyBackThrust, 'backward-thrust')
        else:
            self.taskManager.remove('backward-thrust')
    def ApplyBackThrust(self, task):
        rate = 10
        trajectory = self.renderer.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() - trajectory * rate)       

    # Left and Right turns.
    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'left-turn')
        else:
            self.taskManager.remove('left-turn')
    def ApplyLeftTurn(self, task):
        # Rate = turn speed
        rate = 3
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont          

    def RightTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightTurn, 'right-turn')
        else:
            self.taskManager.remove('right-turn')
    def ApplyRightTurn(self, task):
        # Rate = turn speed
        rate = 3
        self.modelNode.setH(self.modelNode.getH() - rate)
        return Task.cont          
 
    # Left and Right rolls.
    def LeftRoll(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftRoll, 'left-roll')
        else:
            self.taskManager.remove('left-roll')
    def ApplyLeftRoll(self, task):
        # Rate = turn speed
        rate = 3
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont

    def RightRoll(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightRoll, 'right-roll')
        else:
            self.taskManager.remove('right-roll')
    def ApplyRightRoll(self, task):
        # Rate = turn speed
        rate = 3
        self.modelNode.setR(self.modelNode.getR() - rate)
        return Task.cont
 
    # Up and Down turns.
    def UpTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyUpTurn, 'turn-up')
        else:
            self.taskManager.remove('turn-up')
    def ApplyUpTurn(self, task):
        rate = 3
        self.modelNode.setP(self.modelNode.getP() + rate)
        return Task.cont    
 
    def DownTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyDownTurn, 'turn-down')
        else:
            self.taskManager.remove('turn-down')
    def ApplyDownTurn(self, task):
        rate = 3
        self.modelNode.setP(self.modelNode.getP() - rate)
        return Task.cont    

    # Keybinds.
    def SetKeyBindings(self):
        # Key bindings for our spaceship's movement.
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])

        self.accept ('x', self.BackThrust, [1])
        self.accept ('x-up', self.BackThrust, [0])

        self.accept('arrow_left', self.LeftTurn, [1])
        self.accept('arrow_left-up', self.LeftTurn, [0])
        self.accept('a', self.LeftTurn, [1])
        self.accept('a-up', self.LeftTurn, [0])
        
        self.accept('arrow_right', self.RightTurn, [1])
        self.accept('arrow_right-up', self.RightTurn, [0])
        self.accept('d', self.RightTurn, [1])
        self.accept('d-up', self.RightTurn, [0])

        self.accept('q', self.LeftRoll, [1])                     
        self.accept('q-up', self.LeftRoll, [0])

        self.accept('e', self.RightRoll, [1])                     
        self.accept('e-up', self.RightRoll, [0])

        self.accept('arrow_up', self.UpTurn, [1])
        self.accept('arrow_up-up', self.UpTurn, [0])
        self.accept('w', self.UpTurn, [1])
        self.accept('w-up', self.UpTurn, [0])

        self.accept('arrow_down', self.DownTurn, [1])
        self.accept('arrow_down-up', self.DownTurn, [0])
        self.accept('s', self.DownTurn, [1])
        self.accept('s-up', self.DownTurn, [0]) 
        accept: Callable[[str,Callable], None]
        self.accept = accept