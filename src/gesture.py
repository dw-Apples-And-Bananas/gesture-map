import platform
from zero_hid import Keyboard, KeyCodes
keyboard = Keyboard()

def get(points):
    start = points[0]
    end = points[-1]
    diffx = start[0] - end[0]
    diffy = start[1] - end[1]
    # list temp, check for collisions
    results = []
    gestures = {
        "up": diffy > 100 and inxy(points, 50, 0),
        "down": diffy < -100 and inxy(points, 50, 0),
        "left": diffx > 100 and inxy(points, 50, 1),
        "right": diffx < -100 and inxy(points, 50, 1),
    }
    for gesture in gestures:
        if gestures[gesture]:
            results.append(gesture)
    return results

def inxy(points, _range, xy):
    start = points[0]
    for point in points:
        diff = start[xy] - point[xy]
        if diff < -_range or diff > _range:
            return False
    return True

def run(gesture):
    funcs = {
        "tap1": [print, ["tap1"]],
        "tap2": [keyboard.press, [[KeyCodes.MOD_LEFT_CONTROL], KeyCodes.KEY_Z]],
        "tap3": [keyboard.press, [[0x12], KeyCodes.KEY_Z]],
        "tap4": [print, ["tap4"]],
        "tap5": [print, ["tap5"]],
        "hold": [keyboard.press, [[KeyCodes.MOD_LEFT_SHIFT], 0, False]],
        "up": [keyboard.press, [[KeyCodes.MOD_LEFT_CONTROL], KeyCodes.KEY_Z]],
        "down": [keyboard.press, [[0x12], KeyCodes.KEY_Z]],
        "left": [keyboard.press, [[], KeyCodes.KEY_L]],
        "right": [keyboard.press, [[], KeyCodes.KEY_R]],
        "release": [keyboard.release, []],
    }
    func, args = funcs[gesture]
    if platform.system() == "Linux":
        func(*args)
    else:
        print(func, args)
