# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_ENCODING_ASCII = 0
PARAMS_ENCODING_UNICODE = 1
PARAMS_MIN_THRESHOLD = 2

class Params:

    def __init__(self):
        self.__dict__['threshold'] = 4
        self.__dict__['maximum'] = 0
        self.__dict__['encoding'] = PARAMS_ENCODING_ASCII
        self.__dict__['start'] = 0
        self.__dict__['end'] = 0
        self.__dict__['file'] = ''

    def __getattr__(self, name):
        if name == 'threshold':
            return self.__dict__['threshold']
        if name == 'maximum':
            return self.__dict__['maximum']
        if name == 'encoding':
            return self.__dict__['encoding']
        if name == 'start':
            return self.__dict__['start']
        if name == 'end':
            return self.__dict__['end']
        if name == 'file':
            return self.__dict__['file']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'threshold':
            self.__dict__['threshold'] = value
        elif name == 'maximum':
            self.__dict__['maximum'] = value
        elif name == 'encoding':
            self.__dict__['encoding'] = value
        elif name == 'start':
            self.__dict__['start'] = value
        elif name == 'end':
            self.__dict__['end'] = value
        elif name == 'file':
            self.__dict__['file'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_THRESHOLD, self.__dict__['threshold'])
        submsg.AddU32(MSG_KEY_PARAMS_MAXIMUM, self.__dict__['maximum'])
        submsg.AddU8(MSG_KEY_PARAMS_ENCODING, self.__dict__['encoding'])
        submsg.AddU64(MSG_KEY_PARAMS_START, self.__dict__['start'])
        submsg.AddU64(MSG_KEY_PARAMS_END, self.__dict__['end'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_FILE, self.__dict__['file'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['threshold'] = submsg.FindU32(MSG_KEY_PARAMS_THRESHOLD)
        except:
            pass

        try:
            self.__dict__['maximum'] = submsg.FindU32(MSG_KEY_PARAMS_MAXIMUM)
        except:
            pass

        try:
            self.__dict__['encoding'] = submsg.FindU8(MSG_KEY_PARAMS_ENCODING)
        except:
            pass

        try:
            self.__dict__['start'] = submsg.FindU64(MSG_KEY_PARAMS_START)
        except:
            pass

        try:
            self.__dict__['end'] = submsg.FindU64(MSG_KEY_PARAMS_END)
        except:
            pass

        self.__dict__['file'] = submsg.FindString(MSG_KEY_PARAMS_FILE)