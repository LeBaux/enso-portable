# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_InputManager', [dirname(__file__)])
        except ImportError:
            import _InputManager
            return _InputManager
        if fp is not None:
            try:
                _mod = imp.load_module('_InputManager', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _InputManager = swig_import_helper()
    del swig_import_helper
else:
    import _InputManager
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


MESSAGE_WINDOW_CLASS_NAME = _InputManager.MESSAGE_WINDOW_CLASS_NAME
class InputManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, InputManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, InputManager, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == InputManager:
            _self = None
        else:
            _self = self
        this = _InputManager.new_InputManager(_self, )
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _InputManager.delete_InputManager
    __del__ = lambda self : None;
    def run(self): return _InputManager.InputManager_run(self)
    def stop(self): return _InputManager.InputManager_stop(self)
    def enableMouseEvents(self, *args): return _InputManager.InputManager_enableMouseEvents(self, *args)
    def onKeypress(self, *args): return _InputManager.InputManager_onKeypress(self, *args)
    def onSomeKey(self): return _InputManager.InputManager_onSomeKey(self)
    def onSomeMouseButton(self): return _InputManager.InputManager_onSomeMouseButton(self)
    def onExitRequested(self): return _InputManager.InputManager_onExitRequested(self)
    def onMouseMove(self, *args): return _InputManager.InputManager_onMouseMove(self, *args)
    def getQuasimodeKeycode(self, *args): return _InputManager.InputManager_getQuasimodeKeycode(self, *args)
    def setQuasimodeKeycode(self, *args): return _InputManager.InputManager_setQuasimodeKeycode(self, *args)
    def setModality(self, *args): return _InputManager.InputManager_setModality(self, *args)
    def setCapsLockMode(self, *args): return _InputManager.InputManager_setCapsLockMode(self, *args)
    def onTick(self, *args): return _InputManager.InputManager_onTick(self, *args)
    def onInit(self): return _InputManager.InputManager_onInit(self)
    def __disown__(self):
        self.this.disown()
        _InputManager.disown_InputManager(self)
        return weakref_proxy(self)
InputManager_swigregister = _InputManager.InputManager_swigregister
InputManager_swigregister(InputManager)

EVENT_KEY_UP = _InputManager.EVENT_KEY_UP
EVENT_KEY_DOWN = _InputManager.EVENT_KEY_DOWN
EVENT_KEY_QUASIMODE = _InputManager.EVENT_KEY_QUASIMODE
KEYCODE_QUASIMODE_START = _InputManager.KEYCODE_QUASIMODE_START
KEYCODE_QUASIMODE_END = _InputManager.KEYCODE_QUASIMODE_END
KEYCODE_QUASIMODE_CANCEL = _InputManager.KEYCODE_QUASIMODE_CANCEL
KEYCODE_LBUTTON = _InputManager.KEYCODE_LBUTTON
KEYCODE_RBUTTON = _InputManager.KEYCODE_RBUTTON
KEYCODE_CANCEL = _InputManager.KEYCODE_CANCEL
KEYCODE_MBUTTON = _InputManager.KEYCODE_MBUTTON
KEYCODE_BACK = _InputManager.KEYCODE_BACK
KEYCODE_TAB = _InputManager.KEYCODE_TAB
KEYCODE_CLEAR = _InputManager.KEYCODE_CLEAR
KEYCODE_RETURN = _InputManager.KEYCODE_RETURN
KEYCODE_SHIFT = _InputManager.KEYCODE_SHIFT
KEYCODE_CONTROL = _InputManager.KEYCODE_CONTROL
KEYCODE_MENU = _InputManager.KEYCODE_MENU
KEYCODE_PAUSE = _InputManager.KEYCODE_PAUSE
KEYCODE_CAPITAL = _InputManager.KEYCODE_CAPITAL
KEYCODE_KANA = _InputManager.KEYCODE_KANA
KEYCODE_HANGUL = _InputManager.KEYCODE_HANGUL
KEYCODE_JUNJA = _InputManager.KEYCODE_JUNJA
KEYCODE_FINAL = _InputManager.KEYCODE_FINAL
KEYCODE_HANJA = _InputManager.KEYCODE_HANJA
KEYCODE_KANJI = _InputManager.KEYCODE_KANJI
KEYCODE_ESCAPE = _InputManager.KEYCODE_ESCAPE
KEYCODE_CONVERT = _InputManager.KEYCODE_CONVERT
KEYCODE_NONCONVERT = _InputManager.KEYCODE_NONCONVERT
KEYCODE_ACCEPT = _InputManager.KEYCODE_ACCEPT
KEYCODE_MODECHANGE = _InputManager.KEYCODE_MODECHANGE
KEYCODE_SPACE = _InputManager.KEYCODE_SPACE
KEYCODE_PRIOR = _InputManager.KEYCODE_PRIOR
KEYCODE_NEXT = _InputManager.KEYCODE_NEXT
KEYCODE_END = _InputManager.KEYCODE_END
KEYCODE_HOME = _InputManager.KEYCODE_HOME
KEYCODE_LEFT = _InputManager.KEYCODE_LEFT
KEYCODE_UP = _InputManager.KEYCODE_UP
KEYCODE_RIGHT = _InputManager.KEYCODE_RIGHT
KEYCODE_DOWN = _InputManager.KEYCODE_DOWN
KEYCODE_SELECT = _InputManager.KEYCODE_SELECT
KEYCODE_PRINT = _InputManager.KEYCODE_PRINT
KEYCODE_EXECUTE = _InputManager.KEYCODE_EXECUTE
KEYCODE_SNAPSHOT = _InputManager.KEYCODE_SNAPSHOT
KEYCODE_INSERT = _InputManager.KEYCODE_INSERT
KEYCODE_DELETE = _InputManager.KEYCODE_DELETE
KEYCODE_HELP = _InputManager.KEYCODE_HELP
KEYCODE_LWIN = _InputManager.KEYCODE_LWIN
KEYCODE_RWIN = _InputManager.KEYCODE_RWIN
KEYCODE_APPS = _InputManager.KEYCODE_APPS
KEYCODE_NUMPAD0 = _InputManager.KEYCODE_NUMPAD0
KEYCODE_NUMPAD1 = _InputManager.KEYCODE_NUMPAD1
KEYCODE_NUMPAD2 = _InputManager.KEYCODE_NUMPAD2
KEYCODE_NUMPAD3 = _InputManager.KEYCODE_NUMPAD3
KEYCODE_NUMPAD4 = _InputManager.KEYCODE_NUMPAD4
KEYCODE_NUMPAD5 = _InputManager.KEYCODE_NUMPAD5
KEYCODE_NUMPAD6 = _InputManager.KEYCODE_NUMPAD6
KEYCODE_NUMPAD7 = _InputManager.KEYCODE_NUMPAD7
KEYCODE_NUMPAD8 = _InputManager.KEYCODE_NUMPAD8
KEYCODE_NUMPAD9 = _InputManager.KEYCODE_NUMPAD9
KEYCODE_MULTIPLY = _InputManager.KEYCODE_MULTIPLY
KEYCODE_ADD = _InputManager.KEYCODE_ADD
KEYCODE_SEPARATOR = _InputManager.KEYCODE_SEPARATOR
KEYCODE_SUBTRACT = _InputManager.KEYCODE_SUBTRACT
KEYCODE_DECIMAL = _InputManager.KEYCODE_DECIMAL
KEYCODE_DIVIDE = _InputManager.KEYCODE_DIVIDE
KEYCODE_F1 = _InputManager.KEYCODE_F1
KEYCODE_F2 = _InputManager.KEYCODE_F2
KEYCODE_F3 = _InputManager.KEYCODE_F3
KEYCODE_F4 = _InputManager.KEYCODE_F4
KEYCODE_F5 = _InputManager.KEYCODE_F5
KEYCODE_F6 = _InputManager.KEYCODE_F6
KEYCODE_F7 = _InputManager.KEYCODE_F7
KEYCODE_F8 = _InputManager.KEYCODE_F8
KEYCODE_F9 = _InputManager.KEYCODE_F9
KEYCODE_F10 = _InputManager.KEYCODE_F10
KEYCODE_F11 = _InputManager.KEYCODE_F11
KEYCODE_F12 = _InputManager.KEYCODE_F12
KEYCODE_F13 = _InputManager.KEYCODE_F13
KEYCODE_F14 = _InputManager.KEYCODE_F14
KEYCODE_F15 = _InputManager.KEYCODE_F15
KEYCODE_F16 = _InputManager.KEYCODE_F16
KEYCODE_F17 = _InputManager.KEYCODE_F17
KEYCODE_F18 = _InputManager.KEYCODE_F18
KEYCODE_F19 = _InputManager.KEYCODE_F19
KEYCODE_F20 = _InputManager.KEYCODE_F20
KEYCODE_F21 = _InputManager.KEYCODE_F21
KEYCODE_F22 = _InputManager.KEYCODE_F22
KEYCODE_F23 = _InputManager.KEYCODE_F23
KEYCODE_F24 = _InputManager.KEYCODE_F24
KEYCODE_NUMLOCK = _InputManager.KEYCODE_NUMLOCK
KEYCODE_SCROLL = _InputManager.KEYCODE_SCROLL
KEYCODE_LSHIFT = _InputManager.KEYCODE_LSHIFT
KEYCODE_RSHIFT = _InputManager.KEYCODE_RSHIFT
KEYCODE_LCONTROL = _InputManager.KEYCODE_LCONTROL
KEYCODE_RCONTROL = _InputManager.KEYCODE_RCONTROL
KEYCODE_LMENU = _InputManager.KEYCODE_LMENU
KEYCODE_RMENU = _InputManager.KEYCODE_RMENU
KEYCODE_PROCESSKEY = _InputManager.KEYCODE_PROCESSKEY
KEYCODE_ATTN = _InputManager.KEYCODE_ATTN
KEYCODE_CRSEL = _InputManager.KEYCODE_CRSEL
KEYCODE_EXSEL = _InputManager.KEYCODE_EXSEL
KEYCODE_EREOF = _InputManager.KEYCODE_EREOF
KEYCODE_PLAY = _InputManager.KEYCODE_PLAY
KEYCODE_ZOOM = _InputManager.KEYCODE_ZOOM
KEYCODE_NONAME = _InputManager.KEYCODE_NONAME
KEYCODE_PA1 = _InputManager.KEYCODE_PA1
KEYCODE_OEM_CLEAR = _InputManager.KEYCODE_OEM_CLEAR
TICK_TIMER_INTRVL = _InputManager.TICK_TIMER_INTRVL


