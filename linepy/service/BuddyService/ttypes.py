#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
from linepy.service import TalkService

from thrift.transport import TTransport
all_structs = []


class BotType(object):
    RESERVED = 0
    OFFICIAL = 1
    LINE_AT_0 = 2
    LINE_AT = 3

    _VALUES_TO_NAMES = {
        0: "RESERVED",
        1: "OFFICIAL",
        2: "LINE_AT_0",
        3: "LINE_AT",
    }

    _NAMES_TO_VALUES = {
        "RESERVED": 0,
        "OFFICIAL": 1,
        "LINE_AT_0": 2,
        "LINE_AT": 3,
    }


class BuddyOnAirLabel(object):
    ON_AIR = 0
    LIVE = 1

    _VALUES_TO_NAMES = {
        0: "ON_AIR",
        1: "LIVE",
    }

    _NAMES_TO_VALUES = {
        "ON_AIR": 0,
        "LIVE": 1,
    }


class BuddyList(object):
    """
    Attributes:
     - classification
     - displayName
     - totalBuddyCount
     - popularContacts

    """


    def __init__(self, classification=None, displayName=None, totalBuddyCount=None, popularContacts=None,):
        self.classification = classification
        self.displayName = displayName
        self.totalBuddyCount = totalBuddyCount
        self.popularContacts = popularContacts

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.classification = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.totalBuddyCount = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.popularContacts = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = TalkService.ttypes.Contact()
                        _elem5.read(iprot)
                        self.popularContacts.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('BuddyList')
        if self.classification is not None:
            oprot.writeFieldBegin('classification', TType.STRING, 1)
            oprot.writeString(self.classification.encode('utf-8') if sys.version_info[0] == 2 else self.classification)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 2)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
            oprot.writeFieldEnd()
        if self.totalBuddyCount is not None:
            oprot.writeFieldBegin('totalBuddyCount', TType.I32, 3)
            oprot.writeI32(self.totalBuddyCount)
            oprot.writeFieldEnd()
        if self.popularContacts is not None:
            oprot.writeFieldBegin('popularContacts', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.popularContacts))
            for iter6 in self.popularContacts:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BuddyDetail(object):
    """
    Attributes:
     - mid
     - memberCount
     - onAir
     - businessAccount
     - addable
     - acceptableContentTypes
     - capableMyhome
     - freePhoneCallable
     - phoneNumberToDial
     - needPermissionApproval
     - channelId
     - channelProviderName
     - iconType
     - botType
     - showRichMenu
     - richMenuRevision
     - onAirLabel
     - onAirVersion
     - useTheme
     - themeId
     - useBar
     - barRevision
     - useBackground
     - backgroundId
     - statusBarEnabled
     - statusBarRevision
     - searchId
     - blockable

    """


    def __init__(self, mid=None, memberCount=None, onAir=None, businessAccount=None, addable=None, acceptableContentTypes=None, capableMyhome=None, freePhoneCallable=None, phoneNumberToDial=None, needPermissionApproval=None, channelId=None, channelProviderName=None, iconType=None, botType=None, showRichMenu=None, richMenuRevision=None, onAirLabel=None, onAirVersion=None, useTheme=None, themeId=None, useBar=None, barRevision=None, useBackground=None, backgroundId=None, statusBarEnabled=None, statusBarRevision=None, searchId=None, blockable=None,):
        self.mid = mid
        self.memberCount = memberCount
        self.onAir = onAir
        self.businessAccount = businessAccount
        self.addable = addable
        self.acceptableContentTypes = acceptableContentTypes
        self.capableMyhome = capableMyhome
        self.freePhoneCallable = freePhoneCallable
        self.phoneNumberToDial = phoneNumberToDial
        self.needPermissionApproval = needPermissionApproval
        self.channelId = channelId
        self.channelProviderName = channelProviderName
        self.iconType = iconType
        self.botType = botType
        self.showRichMenu = showRichMenu
        self.richMenuRevision = richMenuRevision
        self.onAirLabel = onAirLabel
        self.onAirVersion = onAirVersion
        self.useTheme = useTheme
        self.themeId = themeId
        self.useBar = useBar
        self.barRevision = barRevision
        self.useBackground = useBackground
        self.backgroundId = backgroundId
        self.statusBarEnabled = statusBarEnabled
        self.statusBarRevision = statusBarRevision
        self.searchId = searchId
        self.blockable = blockable

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.mid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.memberCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.onAir = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.businessAccount = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.addable = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.SET:
                    self.acceptableContentTypes = set()
                    (_etype10, _size7) = iprot.readSetBegin()
                    for _i11 in range(_size7):
                        _elem12 = iprot.readI32()
                        self.acceptableContentTypes.add(_elem12)
                    iprot.readSetEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.BOOL:
                    self.capableMyhome = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.BOOL:
                    self.freePhoneCallable = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.phoneNumberToDial = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.BOOL:
                    self.needPermissionApproval = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.channelId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.channelProviderName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I32:
                    self.iconType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I32:
                    self.botType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.BOOL:
                    self.showRichMenu = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.I64:
                    self.richMenuRevision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.I32:
                    self.onAirLabel = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 27:
                if ftype == TType.I32:
                    self.onAirVersion = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.BOOL:
                    self.useTheme = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.STRING:
                    self.themeId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.BOOL:
                    self.useBar = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I64:
                    self.barRevision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.BOOL:
                    self.useBackground = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.STRING:
                    self.backgroundId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.BOOL:
                    self.statusBarEnabled = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 25:
                if ftype == TType.I64:
                    self.statusBarRevision = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 26:
                if ftype == TType.STRING:
                    self.searchId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 28:
                if ftype == TType.BOOL:
                    self.blockable = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('BuddyDetail')
        if self.mid is not None:
            oprot.writeFieldBegin('mid', TType.STRING, 1)
            oprot.writeString(self.mid.encode('utf-8') if sys.version_info[0] == 2 else self.mid)
            oprot.writeFieldEnd()
        if self.memberCount is not None:
            oprot.writeFieldBegin('memberCount', TType.I64, 2)
            oprot.writeI64(self.memberCount)
            oprot.writeFieldEnd()
        if self.onAir is not None:
            oprot.writeFieldBegin('onAir', TType.BOOL, 3)
            oprot.writeBool(self.onAir)
            oprot.writeFieldEnd()
        if self.businessAccount is not None:
            oprot.writeFieldBegin('businessAccount', TType.BOOL, 4)
            oprot.writeBool(self.businessAccount)
            oprot.writeFieldEnd()
        if self.addable is not None:
            oprot.writeFieldBegin('addable', TType.BOOL, 5)
            oprot.writeBool(self.addable)
            oprot.writeFieldEnd()
        if self.acceptableContentTypes is not None:
            oprot.writeFieldBegin('acceptableContentTypes', TType.SET, 6)
            oprot.writeSetBegin(TType.I32, len(self.acceptableContentTypes))
            for iter13 in self.acceptableContentTypes:
                oprot.writeI32(iter13)
            oprot.writeSetEnd()
            oprot.writeFieldEnd()
        if self.capableMyhome is not None:
            oprot.writeFieldBegin('capableMyhome', TType.BOOL, 7)
            oprot.writeBool(self.capableMyhome)
            oprot.writeFieldEnd()
        if self.freePhoneCallable is not None:
            oprot.writeFieldBegin('freePhoneCallable', TType.BOOL, 8)
            oprot.writeBool(self.freePhoneCallable)
            oprot.writeFieldEnd()
        if self.phoneNumberToDial is not None:
            oprot.writeFieldBegin('phoneNumberToDial', TType.STRING, 9)
            oprot.writeString(self.phoneNumberToDial.encode('utf-8') if sys.version_info[0] == 2 else self.phoneNumberToDial)
            oprot.writeFieldEnd()
        if self.needPermissionApproval is not None:
            oprot.writeFieldBegin('needPermissionApproval', TType.BOOL, 10)
            oprot.writeBool(self.needPermissionApproval)
            oprot.writeFieldEnd()
        if self.channelId is not None:
            oprot.writeFieldBegin('channelId', TType.I32, 11)
            oprot.writeI32(self.channelId)
            oprot.writeFieldEnd()
        if self.channelProviderName is not None:
            oprot.writeFieldBegin('channelProviderName', TType.STRING, 12)
            oprot.writeString(self.channelProviderName.encode('utf-8') if sys.version_info[0] == 2 else self.channelProviderName)
            oprot.writeFieldEnd()
        if self.iconType is not None:
            oprot.writeFieldBegin('iconType', TType.I32, 13)
            oprot.writeI32(self.iconType)
            oprot.writeFieldEnd()
        if self.botType is not None:
            oprot.writeFieldBegin('botType', TType.I32, 14)
            oprot.writeI32(self.botType)
            oprot.writeFieldEnd()
        if self.showRichMenu is not None:
            oprot.writeFieldBegin('showRichMenu', TType.BOOL, 15)
            oprot.writeBool(self.showRichMenu)
            oprot.writeFieldEnd()
        if self.richMenuRevision is not None:
            oprot.writeFieldBegin('richMenuRevision', TType.I64, 16)
            oprot.writeI64(self.richMenuRevision)
            oprot.writeFieldEnd()
        if self.onAirLabel is not None:
            oprot.writeFieldBegin('onAirLabel', TType.I32, 17)
            oprot.writeI32(self.onAirLabel)
            oprot.writeFieldEnd()
        if self.useTheme is not None:
            oprot.writeFieldBegin('useTheme', TType.BOOL, 18)
            oprot.writeBool(self.useTheme)
            oprot.writeFieldEnd()
        if self.themeId is not None:
            oprot.writeFieldBegin('themeId', TType.STRING, 19)
            oprot.writeString(self.themeId.encode('utf-8') if sys.version_info[0] == 2 else self.themeId)
            oprot.writeFieldEnd()
        if self.useBar is not None:
            oprot.writeFieldBegin('useBar', TType.BOOL, 20)
            oprot.writeBool(self.useBar)
            oprot.writeFieldEnd()
        if self.barRevision is not None:
            oprot.writeFieldBegin('barRevision', TType.I64, 21)
            oprot.writeI64(self.barRevision)
            oprot.writeFieldEnd()
        if self.useBackground is not None:
            oprot.writeFieldBegin('useBackground', TType.BOOL, 22)
            oprot.writeBool(self.useBackground)
            oprot.writeFieldEnd()
        if self.backgroundId is not None:
            oprot.writeFieldBegin('backgroundId', TType.STRING, 23)
            oprot.writeString(self.backgroundId.encode('utf-8') if sys.version_info[0] == 2 else self.backgroundId)
            oprot.writeFieldEnd()
        if self.statusBarEnabled is not None:
            oprot.writeFieldBegin('statusBarEnabled', TType.BOOL, 24)
            oprot.writeBool(self.statusBarEnabled)
            oprot.writeFieldEnd()
        if self.statusBarRevision is not None:
            oprot.writeFieldBegin('statusBarRevision', TType.I64, 25)
            oprot.writeI64(self.statusBarRevision)
            oprot.writeFieldEnd()
        if self.searchId is not None:
            oprot.writeFieldBegin('searchId', TType.STRING, 26)
            oprot.writeString(self.searchId.encode('utf-8') if sys.version_info[0] == 2 else self.searchId)
            oprot.writeFieldEnd()
        if self.onAirVersion is not None:
            oprot.writeFieldBegin('onAirVersion', TType.I32, 27)
            oprot.writeI32(self.onAirVersion)
            oprot.writeFieldEnd()
        if self.blockable is not None:
            oprot.writeFieldBegin('blockable', TType.BOOL, 28)
            oprot.writeBool(self.blockable)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(BuddyList)
BuddyList.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'classification', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'displayName', 'UTF8', None, ),  # 2
    (3, TType.I32, 'totalBuddyCount', None, None, ),  # 3
    (4, TType.LIST, 'popularContacts', (TType.STRUCT, [TalkService.ttypes.Contact, None], False), None, ),  # 4
)
all_structs.append(BuddyDetail)
BuddyDetail.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'mid', 'UTF8', None, ),  # 1
    (2, TType.I64, 'memberCount', None, None, ),  # 2
    (3, TType.BOOL, 'onAir', None, None, ),  # 3
    (4, TType.BOOL, 'businessAccount', None, None, ),  # 4
    (5, TType.BOOL, 'addable', None, None, ),  # 5
    (6, TType.SET, 'acceptableContentTypes', (TType.I32, None, False), None, ),  # 6
    (7, TType.BOOL, 'capableMyhome', None, None, ),  # 7
    (8, TType.BOOL, 'freePhoneCallable', None, None, ),  # 8
    (9, TType.STRING, 'phoneNumberToDial', 'UTF8', None, ),  # 9
    (10, TType.BOOL, 'needPermissionApproval', None, None, ),  # 10
    (11, TType.I32, 'channelId', None, None, ),  # 11
    (12, TType.STRING, 'channelProviderName', 'UTF8', None, ),  # 12
    (13, TType.I32, 'iconType', None, None, ),  # 13
    (14, TType.I32, 'botType', None, None, ),  # 14
    (15, TType.BOOL, 'showRichMenu', None, None, ),  # 15
    (16, TType.I64, 'richMenuRevision', None, None, ),  # 16
    (17, TType.I32, 'onAirLabel', None, None, ),  # 17
    (18, TType.BOOL, 'useTheme', None, None, ),  # 18
    (19, TType.STRING, 'themeId', 'UTF8', None, ),  # 19
    (20, TType.BOOL, 'useBar', None, None, ),  # 20
    (21, TType.I64, 'barRevision', None, None, ),  # 21
    (22, TType.BOOL, 'useBackground', None, None, ),  # 22
    (23, TType.STRING, 'backgroundId', 'UTF8', None, ),  # 23
    (24, TType.BOOL, 'statusBarEnabled', None, None, ),  # 24
    (25, TType.I64, 'statusBarRevision', None, None, ),  # 25
    (26, TType.STRING, 'searchId', 'UTF8', None, ),  # 26
    (27, TType.I32, 'onAirVersion', None, None, ),  # 27
    (28, TType.BOOL, 'blockable', None, None, ),  # 28
)
fix_spec(all_structs)
del all_structs
