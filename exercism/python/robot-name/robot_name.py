class Robot(object):
    def __init__(self):
        Robot.reset(self)
    
    def reset(self):
        import random
        random.seed()
        alpha_population = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.name = ''.join(random.choices(alpha_population, k=2)) + str(random.randint(100, 999))
