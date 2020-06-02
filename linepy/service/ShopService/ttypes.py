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


class StickerIdRange(object):
    """
    Attributes:
     - start
     - size

    """


    def __init__(self, start=None, size=None,):
        self.start = start
        self.size = size

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
                if ftype == TType.I64:
                    self.start = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
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
        oprot.writeStructBegin('StickerIdRange')
        if self.start is not None:
            oprot.writeFieldBegin('start', TType.I64, 1)
            oprot.writeI64(self.start)
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin('size', TType.I32, 2)
            oprot.writeI32(self.size)
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


class ProductSimple(object):
    """
    Attributes:
     - productId
     - packageId
     - version
     - onSale
     - validUntil
     - stickerIdRanges
     - grantedByDefault
     - displayOrder

    """


    def __init__(self, productId=None, packageId=None, version=None, onSale=None, validUntil=None, stickerIdRanges=None, grantedByDefault=None, displayOrder=None,):
        self.productId = productId
        self.packageId = packageId
        self.version = version
        self.onSale = onSale
        self.validUntil = validUntil
        self.stickerIdRanges = stickerIdRanges
        self.grantedByDefault = grantedByDefault
        self.displayOrder = displayOrder

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
                    self.productId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.packageId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.onSale = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.validUntil = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.LIST:
                    self.stickerIdRanges = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = StickerIdRange()
                        _elem5.read(iprot)
                        self.stickerIdRanges.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 41:
                if ftype == TType.BOOL:
                    self.grantedByDefault = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 42:
                if ftype == TType.I32:
                    self.displayOrder = iprot.readI32()
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
        oprot.writeStructBegin('ProductSimple')
        if self.productId is not None:
            oprot.writeFieldBegin('productId', TType.STRING, 1)
            oprot.writeString(self.productId.encode('utf-8') if sys.version_info[0] == 2 else self.productId)
            oprot.writeFieldEnd()
        if self.packageId is not None:
            oprot.writeFieldBegin('packageId', TType.I64, 2)
            oprot.writeI64(self.packageId)
            oprot.writeFieldEnd()
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.I64, 3)
            oprot.writeI64(self.version)
            oprot.writeFieldEnd()
        if self.onSale is not None:
            oprot.writeFieldBegin('onSale', TType.BOOL, 4)
            oprot.writeBool(self.onSale)
            oprot.writeFieldEnd()
        if self.validUntil is not None:
            oprot.writeFieldBegin('validUntil', TType.I64, 5)
            oprot.writeI64(self.validUntil)
            oprot.writeFieldEnd()
        if self.stickerIdRanges is not None:
            oprot.writeFieldBegin('stickerIdRanges', TType.LIST, 10)
            oprot.writeListBegin(TType.STRUCT, len(self.stickerIdRanges))
            for iter6 in self.stickerIdRanges:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.grantedByDefault is not None:
            oprot.writeFieldBegin('grantedByDefault', TType.BOOL, 41)
            oprot.writeBool(self.grantedByDefault)
            oprot.writeFieldEnd()
        if self.displayOrder is not None:
            oprot.writeFieldBegin('displayOrder', TType.I32, 42)
            oprot.writeI32(self.displayOrder)
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


class ProductSimpleList(object):
    """
    Attributes:
     - hasNext
     - reinvokeHour
     - lastVersionSeq
     - productList
     - recentNewReleaseDate
     - recentEventReleaseDate

    """


    def __init__(self, hasNext=None, reinvokeHour=None, lastVersionSeq=None, productList=None, recentNewReleaseDate=None, recentEventReleaseDate=None,):
        self.hasNext = hasNext
        self.reinvokeHour = reinvokeHour
        self.lastVersionSeq = lastVersionSeq
        self.productList = productList
        self.recentNewReleaseDate = recentNewReleaseDate
        self.recentEventReleaseDate = recentEventReleaseDate

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
                if ftype == TType.BOOL:
                    self.hasNext = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.reinvokeHour = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.lastVersionSeq = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.productList = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = ProductSimple()
                        _elem12.read(iprot)
                        self.productList.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.recentNewReleaseDate = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.recentEventReleaseDate = iprot.readI64()
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
        oprot.writeStructBegin('ProductSimpleList')
        if self.hasNext is not None:
            oprot.writeFieldBegin('hasNext', TType.BOOL, 1)
            oprot.writeBool(self.hasNext)
            oprot.writeFieldEnd()
        if self.reinvokeHour is not None:
            oprot.writeFieldBegin('reinvokeHour', TType.I32, 2)
            oprot.writeI32(self.reinvokeHour)
            oprot.writeFieldEnd()
        if self.lastVersionSeq is not None:
            oprot.writeFieldBegin('lastVersionSeq', TType.I64, 3)
            oprot.writeI64(self.lastVersionSeq)
            oprot.writeFieldEnd()
        if self.productList is not None:
            oprot.writeFieldBegin('productList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.productList))
            for iter13 in self.productList:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.recentNewReleaseDate is not None:
            oprot.writeFieldBegin('recentNewReleaseDate', TType.I64, 5)
            oprot.writeI64(self.recentNewReleaseDate)
            oprot.writeFieldEnd()
        if self.recentEventReleaseDate is not None:
            oprot.writeFieldBegin('recentEventReleaseDate', TType.I64, 6)
            oprot.writeI64(self.recentEventReleaseDate)
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
all_structs.append(StickerIdRange)
StickerIdRange.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'start', None, None, ),  # 1
    (2, TType.I32, 'size', None, None, ),  # 2
)
all_structs.append(ProductSimple)
ProductSimple.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'productId', 'UTF8', None, ),  # 1
    (2, TType.I64, 'packageId', None, None, ),  # 2
    (3, TType.I64, 'version', None, None, ),  # 3
    (4, TType.BOOL, 'onSale', None, None, ),  # 4
    (5, TType.I64, 'validUntil', None, None, ),  # 5
    None,  # 6
    None,  # 7
    None,  # 8
    None,  # 9
    (10, TType.LIST, 'stickerIdRanges', (TType.STRUCT, [StickerIdRange, None], False), None, ),  # 10
    None,  # 11
    None,  # 12
    None,  # 13
    None,  # 14
    None,  # 15
    None,  # 16
    None,  # 17
    None,  # 18
    None,  # 19
    None,  # 20
    None,  # 21
    None,  # 22
    None,  # 23
    None,  # 24
    None,  # 25
    None,  # 26
    None,  # 27
    None,  # 28
    None,  # 29
    None,  # 30
    None,  # 31
    None,  # 32
    None,  # 33
    None,  # 34
    None,  # 35
    None,  # 36
    None,  # 37
    None,  # 38
    None,  # 39
    None,  # 40
    (41, TType.BOOL, 'grantedByDefault', None, None, ),  # 41
    (42, TType.I32, 'displayOrder', None, None, ),  # 42
)
all_structs.append(ProductSimpleList)
ProductSimpleList.thrift_spec = (
    None,  # 0
    (1, TType.BOOL, 'hasNext', None, None, ),  # 1
    (2, TType.I32, 'reinvokeHour', None, None, ),  # 2
    (3, TType.I64, 'lastVersionSeq', None, None, ),  # 3
    (4, TType.LIST, 'productList', (TType.STRUCT, [ProductSimple, None], False), None, ),  # 4
    (5, TType.I64, 'recentNewReleaseDate', None, None, ),  # 5
    (6, TType.I64, 'recentEventReleaseDate', None, None, ),  # 6
)
fix_spec(all_structs)
del all_structs
