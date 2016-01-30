import pythoncom, pyHook, datetime
from test import key, dict_create

def OnKeyboardEventD(event):
    print('#####################Event Down##############################')
    print('Time:',datetime.datetime.now().strftime('%S:%f'))
    print('WindowName:',event.WindowName)
    print('Key:', event.Key)
    # return True to pass the event to other handlers
    return True
def OnKeyboardEventU(event):
    print('****************************Event Up***************************')
    print('Time:',datetime.datetime.now().strftime('%S:%f'))
    print('WindowName:',event.WindowName)
    print('Key:', event.Key)
    # return True to pass the event to other handlers
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

if name == __main__:
    main()