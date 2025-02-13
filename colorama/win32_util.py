# FILE:     autoload/conque_term/conque_win32_util.py
# AUTHOR:   Nico Raffo <nicoraffo@gmail.com>
# WEBSITE:  http://conque.googlecode.com
# MODIFIED: 2011-09-02
# VERSION:  2.3, for Vim 7.0
# LICENSE:
# Conque - Vim terminal/console emulator
# Copyright (C) 2009-2011 Nico Raffo
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

""" Python constants and structures used for ctypes interaction. """

from ctypes import *


# Constants

# show window constants 
SW_FORCEMINIMIZE = 11
SW_HIDE = 0
SW_MAXIMIZE = 3
SW_MINIMIZE = 6
SW_RESTORE = 9
SW_SHOW = 5
SW_SHOWDEFAULT = 10
SW_SHOWMAXIMIZED = 3
SW_SHOWMINIMIZED = 2
SW_SHOWMINNOACTIVE = 7
SW_SHOWNA = 8
SW_SHOWNOACTIVATE = 4
SW_SHOWNORMAL = 1


# Set Console Mode Constants 
ENABLE_PROCESSED_INPUT = 0x0001     # 1
ENABLE_LINE_INPUT = 0x0002          # 2
ENABLE_ECHO_INPUT = 0x0004          # 4
ENABLE_WINDOW_INPUT = 0x0008        # 8
ENABLE_MOUSE_INPUT = 0x0010         # 16
ENABLE_INSERT_MODE = 0x0020         # 32
ENABLE_QUICK_EDIT_MODE = 0x0040     # 64
ENABLE_EXTENDED_FLAGS = 0x0080      # 128


# input event types 
FOCUS_EVENT = 0x0010
KEY_EVENT = 0x0001
MENU_EVENT = 0x0008
MOUSE_EVENT = 0x0002
WINDOW_BUFFER_SIZE_EVENT = 0x0004


# key event modifiers 
CAPSLOCK_ON = 0x0080
ENHANCED_KEY = 0x0100
LEFT_ALT_PRESSED = 0x0002
LEFT_CTRL_PRESSED = 0x0008
NUMLOCK_ON = 0x0020
RIGHT_ALT_PRESSED = 0x0001
RIGHT_CTRL_PRESSED = 0x0004
SCROLLLOCK_ON = 0x0040
SHIFT_PRESSED = 0x0010


# input / output handles 
STDIN  = -10 #STDIN  = c_ulong(-10)
STDOUT = -11 #STDOUT = c_ulong(-11)
STDERR = -12 #STDERR = c_ulong(-12)


CONQUE_WINDOWS_VK = {
    'VK_LBUTTON': 0x0001,
    'VK_RBUTTON': 0x0002,
    'VK_CANCEL': 0x0003,
    'VK_BACK': 0x0008,
    'VK_TAB': 0x0009,
    'VK_CLEAR': 0x000C,
    'VK_RETURN': 0x0D,
    'VK_SHIFT': 0x10,
    'VK_CONTROL': 0x11,
    'VK_MENU': 0x12,
    'VK_PAUSE': 0x0013,
    'VK_CAPITAL': 0x0014,
    'VK_ESCAPE': 0x001B,
    'VK_SPACE': 0x0020,
    'VK_PRIOR': 0x0021,
    'VK_NEXT': 0x0022,
    'VK_END': 0x0023,
    'VK_HOME': 0x0024,
    'VK_LEFT': 0x0025,
    'VK_UP': 0x0026,
    'VK_RIGHT': 0x0027,
    'VK_DOWN': 0x0028,
    'VK_SELECT': 0x0029,
    'VK_PRINT': 0x002A,
    'VK_EXECUTE': 0x002B,
    'VK_SNAPSHOT': 0x002C,
    'VK_INSERT': 0x002D,
    'VK_DELETE': 0x002E,
    'VK_HELP': 0x002F,
    'VK_0': 0x0030,
    'VK_1': 0x0031,
    'VK_2': 0x0032,
    'VK_3': 0x0033,
    'VK_4': 0x0034,
    'VK_5': 0x0035,
    'VK_6': 0x0036,
    'VK_7': 0x0037,
    'VK_8': 0x0038,
    'VK_9': 0x0039,
    'VK_A': 0x0041,
    'VK_B': 0x0042,
    'VK_C': 0x0043,
    'VK_D': 0x0044,
    'VK_E': 0x0045,
    'VK_F': 0x0046,
    'VK_G': 0x0047,
    'VK_H': 0x0048,
    'VK_I': 0x0049,
    'VK_J': 0x004A,
    'VK_K': 0x004B,
    'VK_L': 0x004C,
    'VK_M': 0x004D,
    'VK_N': 0x004E,
    'VK_O': 0x004F,
    'VK_P': 0x0050,
    'VK_Q': 0x0051,
    'VK_R': 0x0052,
    'VK_S': 0x0053,
    'VK_T': 0x0054,
    'VK_U': 0x0055,
    'VK_V': 0x0056,
    'VK_W': 0x0057,
    'VK_X': 0x0058,
    'VK_Y': 0x0059,
    'VK_Z': 0x005A,
    'VK_LWIN': 0x005B,
    'VK_RWIN': 0x005C,
    'VK_APPS': 0x005D,
    'VK_SLEEP': 0x005F,
    'VK_NUMPAD0': 0x0060,
    'VK_NUMPAD1': 0x0061,
    'VK_NUMPAD2': 0x0062,
    'VK_NUMPAD3': 0x0063,
    'VK_NUMPAD4': 0x0064,
    'VK_NUMPAD5': 0x0065,
    'VK_NUMPAD6': 0x0066,
    'VK_NUMPAD7': 0x0067,
    'VK_NUMPAD8': 0x0068,
    'VK_MULTIPLY': 0x006A,
    'VK_ADD': 0x006B,
    'VK_SEPARATOR': 0x006C,
    'VK_SUBTRACT': 0x006D,
    'VK_DECIMAL': 0x006E,
    'VK_DIVIDE': 0x006F,
    'VK_F1': 0x0070,
    'VK_F2': 0x0071,
    'VK_F3': 0x0072,
    'VK_F4': 0x0073,
    'VK_F5': 0x0074,
    'VK_F6': 0x0075,
    'VK_F7': 0x0076,
    'VK_F8': 0x0077,
    'VK_F9': 0x0078,
    'VK_F10': 0x0079,
    'VK_F11': 0x007A,
    'VK_F12': 0x007B,
    'VK_F13': 0x007C,
    'VK_F14': 0x007D,
    'VK_F15': 0x007E,
    'VK_F16': 0x007F,
    'VK_F17': 0x0080,
    'VK_F18': 0x0081,
    'VK_F19': 0x0082,
    'VK_F20': 0x0083,
    'VK_F21': 0x0084,
    'VK_F22': 0x0085,
    'VK_F23': 0x0086,
    'VK_F24': 0x0087,
    'VK_NUMLOCK': 0x0090,
    'VK_SCROLL': 0x0091,
    'VK_LSHIFT': 0x00A0,
    'VK_RSHIFT': 0x00A1,
    'VK_LCONTROL': 0x00A2,
    'VK_RCONTROL': 0x00A3,
    'VK_LMENU': 0x00A4,
    'VK_RMENU': 0x00A5
}

CONQUE_WINDOWS_VK_INV = dict([v, k] for k, v in CONQUE_WINDOWS_VK.items())

CONQUE_WINDOWS_VK_ENHANCED = {
    str(int(CONQUE_WINDOWS_VK['VK_UP'])): 1,
    str(int(CONQUE_WINDOWS_VK['VK_DOWN'])): 1,
    str(int(CONQUE_WINDOWS_VK['VK_LEFT'])): 1,
    str(int(CONQUE_WINDOWS_VK['VK_RIGHT'])): 1,
    str(int(CONQUE_WINDOWS_VK['VK_HOME'])): 1,
    str(int(CONQUE_WINDOWS_VK['VK_END'])): 1
}

def repr_func(self):
    out = '\t{ '
    for x in self._fields_:
        out += ' %s:%s , ' % (x[0], eval('self.' + x[0]))
    return out[:-3] + '}'



class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [("Length", c_ulong),
                ("SecDescriptor", c_void_p),
                ("InheritHandle", c_bool)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class COORD(Structure):
    _fields_ = [("X", c_short),
                ("Y", c_short)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class SMALL_RECT(Structure):
    _fields_ = [("Left", c_short),
                ("Top", c_short),
                ("Right", c_short),
                ("Bottom", c_short)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    _fields_ = [("dwSize", COORD),
                ("dwCursorPosition", COORD),
                ("wAttributes", wintypes.WORD),
                #("wAttributes", c_short),
                ("srWindow", SMALL_RECT),
                ("dwMaximumWindowSize", COORD)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class CHAR_UNION(Union):
    _fields_ = [("UnicodeChar", c_wchar),
                ("AsciiChar", c_char)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class CHAR_INFO(Structure):
    _fields_ = [("Char", CHAR_UNION),
                ("Attributes", c_short)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class KEY_EVENT_RECORD(Structure):
    _fields_ = [("bKeyDown", c_byte),
                ("pad2", c_byte),
                ('pad1', c_short),
                ("wRepeatCount", c_short),
                ("wVirtualKeyCode", c_short),
                ("wVirtualScanCode", c_short),
                ("uChar", CHAR_UNION),
                ("dwControlKeyState", c_int)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class MOUSE_EVENT_RECORD(Structure):
    _fields_ = [("dwMousePosition", COORD),
                ("dwButtonState", c_int),
                ("dwControlKeyState", c_int),
                ("dwEventFlags", c_int)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class WINDOW_BUFFER_SIZE_RECORD(Structure):
    _fields_ = [("dwSize", COORD)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class MENU_EVENT_RECORD(Structure):
    _fields_ = [("dwCommandId", c_uint)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class FOCUS_EVENT_RECORD(Structure):
    _fields_ = [("bSetFocus", c_byte)]

    __repr__ = repr_func

    def to_str(self):
        return ''


class INPUT_UNION(Union):
    _fields_ = [("KeyEvent", KEY_EVENT_RECORD),
                ("MouseEvent", MOUSE_EVENT_RECORD),
                ("WindowBufferSizeEvent", WINDOW_BUFFER_SIZE_RECORD),
                ("MenuEvent", MENU_EVENT_RECORD),
                ("FocusEvent", FOCUS_EVENT_RECORD)]

    __repr__ = repr_func

    def to_str(self):
        return ''

class INPUT_RECORD(Structure):
    _fields_ = [("EventType", c_short),
                ("Event", INPUT_UNION)]

    #__repr__ = repr_func
    def __repr__(self):
        EventTypes = {
            FOCUS_EVENT : "FocusEvent",
            KEY_EVENT   : "KeyEvent",
            MENU_EVENT  : "MenuEvent",
            MOUSE_EVENT : "MouseEvent",
            WINDOW_BUFFER_SIZE_EVENT : "WindowBufferSizeEvent"
        } 
        
        #try:
        event = EventTypes[self.EventType]
        out = '{ %s: %s (%s)\n\t' % ("EventType",
                                      self.EventType,
                                      event)
       
        out += '{ %s: %s,\n\t' % (event,
                                   eval('self.Event.' + event))
        return out[:-2] + '}'
        #except:
        #    return '{ %s: %s { }\n\t' % ("EventType", self.EventType)

    def to_str(self):
        return ''


