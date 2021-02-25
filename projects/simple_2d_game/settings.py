class Settings():

    def __init__(self):
        self.screen_width = 1300
        self.screen_height = 800
        self.bgColor = (230, 230, 230)
    
        # ship settings
        self.shipSpeedFactor = 10

        # alien settings
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1: right, -1: left


        # bullet
        self.bulletSpeedFactor = 13
        self.bulletWidth = 3
        self.bulletHeight = 10
        self.bulletColor = 60, 60, 60
        self.bulletsAllowed = 13