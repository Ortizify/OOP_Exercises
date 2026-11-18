
class Head:
    def __init__(self):
        self.eyes = 2
        self.ears = 2
        self.nose = 1
        self.mouth = 1


class Torso:
    def __init__(self):
        self.chest = 1
        self.stomach = 1
        self.back = 1


class Arm:
    def __init__(self, side):
        self.side = side
        self.elbow = 1


class Hand:
    def __init__(self, side):
        self.side = side
        self.fingers = 5

class Leg:
    def __init__(self, side):
        self.side = side
        self.knee = 1



class Feet:
    def __init__(self, side):
        self.side = side
        self.toes = 5



class Human:
    def __init__(self, name):
        self.name = name

        self.head = Head()
        self.torso = Torso()

        self.left_arm = Arm("left")
        self.right_arm = Arm("right")

        self.left_hand = Hand("left")
        self.right_hand = Hand("right")

        self.left_leg = Leg("left")
        self.right_leg = Leg("right")

        self.left_foot = Feet("left")
        self.right_foot = Feet("right")
        
        self.left_arm.hand = self.left_hand
        self.right_arm.hand = self.right_hand

        self.left_leg.foot = self.left_foot
        self.right_leg.foot = self.right_foot



if __name__ == "__main__":
    person = Human("John")

    print("Name:", person.name)
    print("Eyes:", person.head.eyes)
    print("Left arm:", person.left_arm.side)
    print("Left hand fingers:", person.left_arm.hand.fingers)
    print("Right leg:", person.right_leg.side)
    print("Right foot toes:", person.right_leg.foot.toes)
