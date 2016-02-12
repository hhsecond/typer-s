import pythoncom, pyHook, datetime, threading
from core import objthread

def OnKeyboardEventD(event):
    with threading.Lock():
        objthread(event.Key, event.WindowName, datetime.datetime.now(), 1)#3rd parameter is the position of key (down is 1)
        return True

def OnKeyboardEventU(event):
    with threading.Lock():
        objthread(event.Key, event.WindowName, datetime.datetime.now(), 0)#3rd parameter is the position of key (up is 0)
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


'''import pythoncom, pyHook, datetime, threading
from core import objthread
listt = []
def OnKeyboardEventD(event):
    vald = 'with threading.Lock():'
    vald = vald + 'objthread(' + event.Key + ', ' + event.WindowName + ', ' + str(datetime.datetime.now()) + ', ' + str(1) + ')'#3rd parameter is the position of key (down is 1)
    listt.append(vald)
    if event.Key == 'Escape':
        f = open('indata.txt', 'w+')
        f.write(str(listt))
        f.close
    return True

def OnKeyboardEventU(event):
    valu = 'with threading.Lock():'
    valu =  valu + 'objthread(' + event.Key + ', ' + event.WindowName + ', ' + str(datetime.datetime.now()) + ', ' + str(0) + ')'
    listt.append(valu)
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
'''
if __name__ == '__main__':
    main()