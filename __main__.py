import pythoncom, pyHook, datetime, threading, time, sys
import lcore, ecore, main_core
print('initializing the thread.....')
time.sleep(.5)       


def OnKeyboardEventD(event):
    with threading.Lock():
        lcore.objthread_down(event.Key, event.WindowName, datetime.datetime.now())
        return True

def OnKeyboardEventU(event):
    with threading.Lock():
        lcore.objthread_up(event.Key, event.WindowName, datetime.datetime.now())
        return True

def OnKeyboardEventexecD(event):
    with threading.Lock():
        ecore.objthread_down(event.Key, event.WindowName, datetime.datetime.now())
        return True

def OnKeyboardEventexecU(event):
    with threading.Lock():
        ecore.objthread_up(event.Key, event.WindowName, datetime.datetime.now())
        return True


def main():
    try:
        if sys.argv[1] == '-l':
            print('script started in listening mode')
            main_core.dict_from_file()
        elif sys.argv[1] == '-e':
            print('Rading data from the tree, make sure you have enough')
            main_core.dict_from_file()
            print('script started in execution mode...')

    except Exception as e:
        if str(e) == 'list index out of range':
            print('Start the program in listening mode (-l) or execution mode (-e)')
        else:
            print(str(e))
    else:
        if sys.argv[1] == '-l':
            #writing db at each interval - another thread
            lcore.writedb()
            # create a hook manager
            hm = pyHook.HookManager()
            # watch for all keyboard events
            hm.KeyDown = OnKeyboardEventD
            hm.KeyUp = OnKeyboardEventU
            # set the hook
            hm.HookKeyboard()
            # wait forever
            pythoncom.PumpMessages()
        elif sys.argv[1] == '-e':
            #writing db at each interval - currently not configured for execution mode
            #writedb()

            #checking the tree for anomalies in the pattern
            ecore.checkdb()
            # create a hook manager
            hm = pyHook.HookManager()
            # watch for all keyboard events
            hm.KeyDown = OnKeyboardEventexecD
            hm.KeyUp = OnKeyboardEventexecU
            # set the hook
            hm.HookKeyboard()
            # wait forever
            pythoncom.PumpMessages()

if __name__ == '__main__':
    main()