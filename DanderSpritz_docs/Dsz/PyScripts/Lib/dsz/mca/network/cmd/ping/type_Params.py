# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.IpAddr
import mcl.object.MclTime

class Params:

    def __init__(self):
        self.__dict__['dstAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['broadcast'] = False
        self.__dict__['timeout'] = mcl.object.MclTime.MclTime()
        self.__dict__['dstHost'] = ''

    def __getattr__(self, name):
        if name == 'dstAddr':
            return self.__dict__['dstAddr']
        if name == 'broadcast':
            return self.__dict__['broadcast']
        if name == 'timeout':
            return self.__dict__['timeout']
        if name == 'dstHost':
            return self.__dict__['dstHost']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'dstAddr':
            self.__dict__['dstAddr'] = value
        elif name == 'broadcast':
            self.__dict__['broadcast'] = value
        elif name == 'timeout':
            self.__dict__['timeout'] = value
        elif name == 'dstHost':
            self.__dict__['dstHost'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddIpAddr(MSG_KEY_PARAMS_DEST_ADDRESS, self.__dict__['dstAddr'])
        submsg.AddBool(MSG_KEY_PARAMS_BROADCAST, self.__dict__['broadcast'])
        submsg.AddTime(MSG_KEY_PARAMS_TIMEOUT, self.__dict__['timeout'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DEST_HOST, self.__dict__['dstHost'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['dstAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_DEST_ADDRESS)
        try:
            self.__dict__['broadcast'] = submsg.FindBool(MSG_KEY_PARAMS_BROADCAST)
        except:
            pass

        self.__dict__['timeout'] = submsg.FindTime(MSG_KEY_PARAMS_TIMEOUT)
        self.__dict__['dstHost'] = submsg.FindString(MSG_KEY_PARAMS_DEST_HOST)