import pythoncom, pyHook, datetime
from core import obj_create

def OnKeyboardEventD(event):
    obj_create(event.Key, event.WindowName, datetime.datetime.now(), 1)#3rd parameter is the position of key (down is 1)
    return True

def OnKeyboardEventU(event):
    obj_create(event.Key, event.WindowName, datetime.datetime.now(), 0)#3rd parameter is the position of key (up is 0)
    return True


def main():
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.KeyDown = OnKeyboardEventD
    hm.KeyUp = OnKeyboardEventU
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()

if __name__ == '__main__':
    main()