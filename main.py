import pyautogui
import time

LEFT_SIDE = (237, 659)
BANDANA = (242, 95, 87)
SIDE_BRANCH_LOCATIONS = {
    'left': (247, 628),
    'right': (472, 628),
}
BRANCH_COLOR = {
    'left': (71, 36, 11),
    'right': (70, 35, 11),
}


class KickYaChopBot:

    def __init__(self):
        self.current_side = 'left'

    def set_current_side(self):
        if pyautogui.pixel(*LEFT_SIDE) == BANDANA:
            self.current_side = 'left'
        else:
            self.current_side = 'right'

    def branch_above_exists(self):
        pixel_color = pyautogui.pixel(*SIDE_BRANCH_LOCATIONS.get(self.current_side))
        if pixel_color == BRANCH_COLOR.get(self.current_side):
            return True

    def switch_side(self):
        self.current_side = 'right' if self.current_side == 'left' else 'left'

    def chop(self):
        if self.branch_above_exists():
            self.switch_side()
        pyautogui.hotkey(self.current_side)

    def run(self):
        while True:
            try:
                self.chop()
                time.sleep(.02)
            except OSError:
                pass


if __name__ == '__main__':
    print('Starting in 3 seconds...')
    time.sleep(3)

    bot = KickYaChopBot()
    bot.run()
