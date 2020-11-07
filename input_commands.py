# https://qiita.com/safin/items/09e41718f60d126aa99d



import ctypes

ULONG_PTR = ctypes.POINTER(ctypes.c_ulong)

# マウスイベントの情報
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ULONG_PTR)]


class INPUT(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("mi", MOUSEINPUT)]



LPINPUT = ctypes.POINTER(INPUT)

SendInput = ctypes.windll.user32.SendInput
SendInput.argtypes = (ctypes.c_uint, LPINPUT, ctypes.c_int)
SendInput.restype = ctypes.c_uint

x, y = 400, 400
x = x * 65536 // 1920
y = y * 65536 // 1080
#_mi = MOUSEINPUT(x, y, 0, (0x0001 | 0x8000), 0, None)
_mi = MOUSEINPUT(x, y, 0, (0x0002), 0, None)
SendInput(1, INPUT(0, _mi), ctypes.sizeof(INPUT))
_mi = MOUSEINPUT(x, y, 0, (0x0004), 0, None)
SendInput(1, INPUT(0, _mi), ctypes.sizeof(INPUT))