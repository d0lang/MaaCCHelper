from maa.toolkit import Toolkit
class Linker:
    def __init__(self):
        user_path = "./"
        Toolkit.init_option(user_path)

    adb_devices = Toolkit.find_adb_devices()