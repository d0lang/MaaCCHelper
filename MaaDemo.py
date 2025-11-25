from maa.event_sink import EventSink
from maa.tasker import Tasker
from maa.toolkit import Toolkit
from maa.context import Context, ContextEventSink
from maa.resource import Resource
from maa.controller import AdbController

from maa.custom_action import CustomAction
from maa.custom_recognition import CustomRecognition

resource = Resource()

def mainTask():
    user_path = "./"
    Toolkit.init_option(user_path)

    adb_devices = Toolkit.find_adb_devices()
    if not adb_devices:
        print("No ADB device found.")
        exit()
    device = adb_devices[0]
    print(device)
    controller = AdbController(
        adb_path = device.adb_path,
        address = device.address,
        screencap_methods=device.screencap_methods,
        input_methods=device.input_methods,
        config = device.config
    )
    controller.post_connection().wait()

    # 截图
    # images = controller.post_screencap().get()
    # controller.post_click(112,736)
    resource_path = "resource"
    res_job = resource.post_bundle(resource_path)
    res_job.wait()
    print(res_job.succeeded)

    tasker = Tasker()
    tasker.bind(resource, controller)
    for i in range(0,2):
        tasker.post_task("刷取好感度").wait().get()
    # tasker.controller.post_click(1045, 660)