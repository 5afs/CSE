class Camera(object):
    def __init__(self, lens_cap, zoom, focus, button, pictures_left):
        # These are things that a WaterGun has.
        # All of these should be relevant to our program.
        self.lens_cap = lens_cap
        self.zoom = zoom
        self.focus = focus
        self.button = button
        self.pictures_left = pictures_left

    def get_in_focus(self):
        self.focus = True
        print("Your camera is now in focus.")

    def shoot(self):
        if self.button:
            if self.focus and self.pictures_left:
                print("You took a picture!")
                self.pictures_left -= 1
            elif not self.pictures_left:
                print("You have no more film left.")
            elif not self.focus:
                print("Your camera is not in focus.")
                self.get_in_focus()
        else:
            print("You cannot take a picture.")


my_camera = Camera(True, 0, False, True, 10)
catherine_camera = Camera(False, 0, True, True, 1)

my_camera.shoot()
catherine_camera.shoot()
