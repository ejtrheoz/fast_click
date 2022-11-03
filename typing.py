import win32api
import win32con
import time
import keyboard


while True:
    try:
        if keyboard.is_pressed('k'):
            break
    except:
        break


state_left = win32api.GetKeyState(0x01)

while 1:
	a = win32api.GetKeyState(0x01)
	if a != state_left:
		break 

win32api.keybd_event(0x34, 0,0,0)
win32api.keybd_event(0x34,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(0x35, 0,0,0)
win32api.keybd_event(0x35,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(0x30, 0,0,0)
win32api.keybd_event(0x30,0 ,win32con.KEYEVENTF_KEYUP ,0)

time.sleep(0.2)
state_left = win32api.GetKeyState(0x01)
while 1:
	a = win32api.GetKeyState(0x01)
	if a != state_left:
		break 

win32api.keybd_event(0x31, 0,0,0)
win32api.keybd_event(0x31,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(0x34, 0,0,0)
win32api.keybd_event(0x34,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(0x38, 0,0,0)
win32api.keybd_event(0x38,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(0x38, 0,0,0)
win32api.keybd_event(0x38,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(0x35, 0,0,0)
win32api.keybd_event(0x35,0 ,win32con.KEYEVENTF_KEYUP ,0)
win32api.keybd_event(0x34, 0,0,0)
win32api.keybd_event(0x34,0 ,win32con.KEYEVENTF_KEYUP ,0)


