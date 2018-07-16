import struct
import array
from random import randint, choice
from uuid import uuid4


class Error(Exception):
    pass


class DecodeError(Error):
    pass


class EncodeError(Error):
    pass


(tSTRING, tWSTRING, tBYTE, tINT16, tUINT16, tINT32, tUINT32, tGROUP_START, tGROUP_END) = list(range(1, 8)) + [100, 101]
(tGROUP_START_TAG, tGROUP_ITEM_START_TAG, tGROUP_ITEM_END_TAG, tGROUP_END_TAG) = list(range(1, 5))
X_STRING = 1
X_WSTRING = 2
X_BYTE = 3
X_INT16 = 4
X_UINT16 = 5
X_INT32 = 6
X_UINT32 = 7
X_INT64 = 8
X_UINT64 = 9
X_GROUP_START = 100
X_GROUP_END = 101


def randstr(max_len=32):
    chars = [chr(i) for i in list(range(ord('A'), ord('Z')+1)) + list(range(ord('a'), ord('z')+1))]
    return ''.join([choice(chars) for x in range(randint(1, max_len))])


class IPGen:
    def __init__(self):
        self.ClassA = 10
        self.ClassB = 1
        self.ClassC = 1
        self.ClassD = 1

    def GetIP(self):
        ip = '%d.%d.%d.%d' % (self.ClassA, self.ClassB, self.ClassC, self.ClassD)
        self.ClassD += 1
        if self.ClassD == 255:
            self.ClassD = 1
            self.ClassC += 1
            if self.ClassC == 255:
                self.ClassC = 0
                self.ClassB += 1
                if self.ClassB == 255:
                    self.ClassB = 0
                    self.ClassA += 1
        return ip


IPGen = IPGen()


def randip():
    global IPGen
    return IPGen.GetIP()


def tuid(s=str(uuid4()).upper()):
    s = s.replace('-', '')
    return str('-').join([s[0:12], s[12:20], s[20:24], s[24:28], s[28:]])


class MCPItemBase:
    def __init__(self, field_id, type, length, data, is_network_order):
        self.ID = int(field_id)
        self.Type = type
        self.Length = length
        self.Data = data
        self.ByteOrder = is_network_order is True and '!' or '='

    def Size(self):
        pass

    def Pack(self):
        buf = array.array('B')
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.ID))
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.Type))
        return buf

    def tostring(self):
        pass


class MCPItemINT16(MCPItemBase):
    def __init__(self, id, data, is_network_order):
        if data == '':
            data = 0
        MCPItemBase.__init__(self, id, tINT16, 2, int(data), is_network_order)

    def Size(self):
        return 4 + 4 + 4 + 2

    def tostring(self):
        return "\nID: %d, Type: %d, Length:%d, Data:%d" % (self.ID, self.Type, self.Length, self.Data)

    def Pack(self):
        buf = MCPItemBase.Pack(self)
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.Length))
        buf.fromstring(struct.pack(self.ByteOrder+'h', self.Data))
        return buf.tostring()


class MCPItemUINT16(MCPItemBase):
    def __init__(self, id, data, is_network_order):
        MCPItemBase.__init__(self, id, tUINT16, 2, int(data), is_network_order)

    def Size(self):
        return 4 + 4 + 4 + 2

    def tostring(self):
        return "\nID: %d, Type: %d, Length:%d, Data:%d" % (self.ID, self.Type, self.Length, self.Data)

    def Pack(self):
        buf = MCPItemBase.Pack(self)
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.Length))
        buf.fromstring(struct.pack(self.ByteOrder+'H', self.Data))
        return buf.tostring()


class MCPItemINT32(MCPItemBase):
    def __init__(self, id, data, is_network_order):
        MCPItemBase.__init__(self, id, tINT32, 4, int(data), is_network_order)

    def Size(self):
        return 4 + 4 + 4 + 4

    def tostring(self):
        return "\nID: %d, Type: %d, Length:%d, Data:%d" % (self.ID, self.Type, self.Length, self.Data)

    def Pack(self):
        buf = MCPItemBase.Pack(self)
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.Length))
        buf.fromstring(struct.pack(self.ByteOrder+'i', self.Data))
        return buf.tostring()


class MCPItemUINT32(MCPItemBase):
    def __init__(self, id, data, is_network_order):
        MCPItemBase.__init__(self, id, tUINT32, 4, int(data), is_network_order)

    def Size(self):
        return 4 + 4 + 4 + 4

    def tostring(self):
        return "\nID: %d, Type: %d, Length:%d, Data:%d" % (self.ID, self.Type, self.Length, self.Data)

    def Pack(self):
        buf = MCPItemBase.Pack(self)
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.Length))
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.Data))
        return buf.tostring()


class MCPItemGroupTag(MCPItemBase):
    def __init__(self, id, is_group_start, is_network_order):
        if is_group_start:
            MCPItemBase.__init__(self, id, tGROUP_START, 0, 0, is_network_order)
        else:
            MCPItemBase.__init__(self, id, tGROUP_END, 0, 0, is_network_order)

    def Size(self):
        return 4 + 4

    def GetDataLength(self):
        return 0

    def Pack(self):
        buf = MCPItemBase.Pack(self)
        return buf.tostring()

    def tostring(self):
        return "\nID: %d, Type: Group" % self.ID


class MCPItemByte(MCPItemBase):
    def __init__(self, id, data, is_network_order):
        MCPItemBase.__init__(self, id, tBYTE, len(data), data, is_network_order)

    def Size(self):
        return 4 + 4 + 4 + len(self.Data)

    def tostring(self):
        return "\nID: %d, Type: %d, Length:%d, Data:%s" % (self.ID, self.Type, self.Length, self.Data)

    def Pack(self):
        buf = MCPItemBase.Pack(self)
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.Length))
        buf.fromstring(self.Data)
        return buf.tostring()


class MCPItemString(MCPItemBase):
    def __init__(self, id, data, is_network_order):
        MCPItemBase.__init__(self, id, tSTRING, len(data), data, is_network_order)
        self.Data = data
        self.Length = len(self.Data)
        self.PackedDataLength = self.__packData(self.Data)[1]

    def Size(self):
        return 4 + 4 + 4 + self.PackedDataLength

    def tostring(self):
        return "\nID: %d, Type: tSTRING, Length:%d, Data:%s" % (self.ID, self.Length, self.Data)

    def Pack(self):
        buf = MCPItemBase.Pack(self)
        packed_str, length = self.__packData(self.Data)
        buf.fromstring(struct.pack(self.ByteOrder+'I', length))
        buf.fromstring(packed_str)
        s = buf.tostring()
        return s

    def __packData(self, data):
        encode_data = self.Data + '\0'
        if not all(ord(c) < 128 for c in encode_data):
            encode_data = str.decode('utf-8')
        a = array.array('B')
        a.fromstring(struct.pack(self.ByteOrder+str(len(encode_data))+'s', encode_data))
        packed_str = a.tostring()
        return packed_str, len(packed_str)


class MCPItemWString(MCPItemBase):
    def __init__(self, id, data, is_network_order):
        MCPItemBase.__init__(self, id, tWSTRING, len(data), data, is_network_order)
        self.Data = data
        self.Length = len(self.Data)
        self.PackedDataLength = self.__packData(self.Data)[1]

    def Size(self):
        return 4 + 4 + 4 + self.PackedDataLength

    def Pack(self):
        buf = MCPItemBase.Pack(self)
        packed_str, length = self.__packData(self.Data)
        buf.fromstring(struct.pack(self.ByteOrder+'I', length))
        buf.fromstring(packed_str)
        s = buf.tostring()
        return s

    def __packData(self, data):
        """
        if all(ord(c) < 128 for c in self.Data):
            encodData = self.Data + '\x00'
        else:
            encodData = self.Data.decode('utf-8').encode('utf-16') + '\x00'
        strBuf = buffer(encodData)
        a = array.array('B')
        for i in range(len(strBuf)):
            a.fromstring(struct.pack(self.ByteOrder+'H', ord(strBuf[i:i+1])))
        packedStr = a.tostring()
        """
        temp = self.Data
        if type(temp) == bytes:
            temp = temp.decode()
        encode_data = temp + '\x00'
        packed_str = encode_data.encode('utf-16be')  # be is for network byte order
        return packed_str, len(packed_str)

    def tostring(self):
        return "\nID: %d, Type: tWSTRING, Length:%d, Data:%s" % (self.ID, self.Length, self.Data)


class MCPGroupItem:
    """Represents a MCP group"""
    def __init__(self, is_network_order):
        self.items = []
        self.ByteOrder = is_network_order is True and '!' or '='

    def Add(self, mcp_item):
        self.items.append(mcp_item)

    def Size(self):
        size = 4 + 4 + 4 + 4
        for i in self.items:
            size += i.Size()
        return size

    def Pack(self):
        buf = array.array("B")
        buf.fromstring(struct.pack(self.ByteOrder+'I', 3001))
        buf.fromstring(struct.pack(self.ByteOrder+'I', tGROUP_START))
        for i in self.items:
            buf.fromstring(i.Pack())
        buf.fromstring(struct.pack(self.ByteOrder+'I', 3001))
        buf.fromstring(struct.pack(self.ByteOrder+'I', tGROUP_END))
        return buf.tostring()


class MCPGroup:
    def __init__(self, id, is_network_order):
        self.ID = id
        self.ByteOrder = is_network_order is True and '!' or '='
        self.items = []

    def AddGroupItem(self, mcp_group_item):
        self.items.append(mcp_group_item)

    def Size(self):
        size = 4 + 4 + 4 + 4
        for i in self.items:
            size += i.Size()
        return size

    def Pack(self):
        buf = array.array("B")
        self.Size() # to calculate the size
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.ID))
        buf.fromstring(struct.pack(self.ByteOrder+'I', tGROUP_START))
        for i in self.items:
            buf.fromstring(i.Pack())
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.ID))
        buf.fromstring(struct.pack(self.ByteOrder+'I', tGROUP_END))
        return buf.tostring()


class MCPMessage:
    _pack_cache_dict = dict()
    _pack_composite_cache_dict = dict()
    "Represents a MCP message"
    def __init__(self, is_network_order):
        self.MessageLength = 0
        self.ByteOrder = is_network_order is True and '!' or '='
        self.items = []

    def Add(self, mcp_item):
        self.items.append(mcp_item)

    def Size(self):
        self.MessageLength = 0
        for i in self.items:
            self.MessageLength += i.Size()
        return self.MessageLength

    def Pack(self):
        self.Size()  # to calculate the size
        hash_key_src_tuple = tuple([self.ByteOrder, self.MessageLength]+self.items)
        hash_key = hash(hash_key_src_tuple)
        ret = self._pack_cache_dict.get(hash_key)
        if ret is not None:
            return ret
        buf = array.array("B")
        buf.fromstring(struct.pack(self.ByteOrder+'I', self.MessageLength))
        for i in self.items:
            buf.fromstring(i.Pack())
        ret = buf.tostring()
        self._pack_cache_dict[hash_key] = ret
        return ret

    def PackToComposite(self):
        buf = array.array("B")
        for i in self.items:
            buf.fromstring(i.Pack())
        return buf.tostring()


def ParseMCPGroup(buf, pos, mcp_group, is_network_order, cb=None):
    def Nothing(id, dataType, dataLen, isInterMsg, data, groupIndex=0):
        pass

    byte_order = is_network_order is True and '!' or '='
    cb = callable(cb) and cb or Nothing
    ID = struct.unpack(byte_order+'I', buf[pos:pos+4])[0]
    pos += 4
    TYPE = struct.unpack(byte_order+'I', buf[pos:pos+4])[0]
    pos += 4
    if ID == mcp_group.ID:
        cb(ID, TYPE, 0, True, None, tGROUP_END_TAG)
        return mcp_group, pos
    pos -= 8
    while True:    # at least one group item
        ID = struct.unpack(byte_order+'I', buf[pos:pos+4])[0]
        pos += 4
        TYPE = struct.unpack(byte_order+'I', buf[pos:pos+4])[0]
        pos += 4
        if ID == mcp_group.ID:  # reach the end of the group
            cb(ID, TYPE, 0, True, None, tGROUP_END_TAG)
            break
        cb(ID, TYPE, 0, True, None, tGROUP_ITEM_START_TAG)
        pos -= 8
        mcp_group_item = MCPGroupItem(is_network_order)  # create a new group item
        while TYPE != tGROUP_END:
            mcp_msg_item, pos = ParseMCPItem(buf, pos, is_network_order, True, cb)
            TYPE = mcp_msg_item.Type
            if TYPE != tGROUP_END:
                mcp_group_item.Add(mcp_msg_item)

        mcp_group.AddGroupItem(mcp_group_item)
    return mcp_group, pos


def ParseMCPItem(buf, pos, is_network_order, is_inter_msg=False, cb=None):
    def Nothing(id, dataType, dataLen, isInterMsg, data, groupTag = 0):
        pass
    byte_order = is_network_order is True and '!' or '='
    cb = callable(cb) and cb or Nothing
    ID = struct.unpack(byte_order+'I', buf[pos:pos+4])[0]
    pos += 4
    TYPE = struct.unpack(byte_order+'I', buf[pos:pos+4])[0]
    pos += 4
    if TYPE is tGROUP_START:
        mcp_group = MCPGroup(ID, is_network_order)
        cb(ID, TYPE, 0, is_inter_msg, None, tGROUP_START_TAG)
        return ParseMCPGroup(buf, pos, mcp_group, is_network_order, cb)
    if TYPE is tGROUP_END:
        cb(ID, TYPE, 0, is_inter_msg, None, tGROUP_ITEM_END_TAG)
        return MCPItemGroupTag(ID, False, is_network_order), pos
    Length = struct.unpack(byte_order+'I', buf[pos:pos+4])[0]
    pos += 4
    Data = ''
    if TYPE is tSTRING:
        if Length > 0:
            Data = buf[pos:pos+Length]
            pos += Length
        cb(ID, TYPE, Length, is_inter_msg, Data)
        return MCPItemString(ID, Data, is_network_order), pos
    elif TYPE is tBYTE:
        if Length > 0:
            Data = buf[pos:pos+Length]
            pos += Length
        cb(ID, TYPE, Length, is_inter_msg, Data)
        ParseCasMessage(Data, False, cb)
        return MCPItemByte(ID, Data, is_network_order), pos
    elif TYPE is tWSTRING:
        if Length > 0:
            tmpS = buf[pos: pos+Length]
            unpackS = struct.unpack(byte_order + 'h'*(Length//2), buf[pos: pos+Length])
            unpackA = array.array('B')
            for c in unpackS:
                unpackA.append(c)
            Data = unpackA.tostring() # make utf-16
            Data = Data[:-1]
            pos += Length
        else:
            Data = ''
        cb(ID, TYPE, Length, is_inter_msg, Data)
        return MCPItemWString(ID, Data, is_network_order), pos
    elif TYPE is tINT16:
        if Length > 0:
            Data = struct.unpack(byte_order + 'h', buf[pos:pos+2])[0]
            pos += 2
        else:
            Data = 0
        cb(ID, TYPE, Length, is_inter_msg, Data)
        return MCPItemINT16(ID, Data, is_network_order), pos
    elif TYPE in (tUINT16, 1001):
        if Length > 0:
            Data = struct.unpack(byte_order+'H', buf[pos:pos+2])[0]
            pos += 2
        else:
            Data = 0
        cb(ID, TYPE, Length, is_inter_msg, Data)
        return MCPItemUINT16(ID, Data, is_network_order), pos
    elif TYPE is tINT32:
        if Length > 0:
            Data = struct.unpack(byte_order+'i', buf[pos:pos+4])[0]
            pos += 4
        else:
            Data = 0
        cb(ID, TYPE, Length, is_inter_msg, Data)
        return MCPItemINT32(ID, Data, is_network_order), pos
    elif TYPE is tUINT32:
        if Length > 0:
            Data = struct.unpack(byte_order+'I', buf[pos:pos+4])[0]
            pos += 4
        else:
            Data = 0
        cb(ID, TYPE, Length, is_inter_msg, Data)
        return MCPItemUINT32(ID, Data, is_network_order), pos
    cb(ID, TYPE, Length, is_inter_msg, None)
    return MCPItemByte(ID, Data, is_network_order), pos


def ParseMCPMessage(data, is_network_order, cb=None):
    mcp_msgs = []
    buf = memoryview(data)
    size = len(data)
    pos = 0
    while pos < size:
        mcp_msg = MCPMessage(is_network_order)
        pos += 4
        while pos < size:
            mcp_msg_item, pos = ParseMCPItem(buf, pos, is_network_order, False, cb)
            mcp_msg.Add(mcp_msg_item)

        mcp_msgs.append(mcp_msg)
    return mcp_msgs


def ParseCasMessage(data, is_network_order, cb=None):
    mcp_msgs = []
    buf = buffer(data)
    size = len(data)
    pos = 0
    while pos < size:
        mcp_msg = MCPMessage(is_network_order)
        epos = pos + size
        while pos < epos:
            mcp_msg_item, pos = ParseMCPItem(buf, pos, is_network_order, False, cb)
            mcp_msg.Add(mcp_msg_item)
            mcp_msgs.append(mcp_msg)

    for mcp_msg in mcp_msgs:
        for items in mcp_msg.items:
            print(type(items))
            if items is MCPGroup:
                for item in items.items:
                    if item is MCPGroupItem:
                        for i in item.items:
                            if i is MCPItemByte:
                                ParseCasMessage(i.Data, is_network_order, cb)
    return mcp_msgs
