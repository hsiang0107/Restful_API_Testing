import random
import string
import time
import datetime

G_UUIDMaxNum = 16**36


class Generator(object):
    '''
    A base class for all item generator
    '''
    def __init__(self, dict_setting):
        """
        Constructor
        """
        self.dictSetting = dict_setting

    def GetNext(self):
        """
        Give the next value
        """
        raise NotImplementedError("Not Implemented")


class ListGen(Generator):
    """
    Generate Result based on a list. Round-robin.
    """
    def __init__(self , list_data):
        self.listData = list_data
        self.intIndex = 0
        self.intDatLen = len(list_data)

    def GetNext(self):
        if self.intIndex >= self.intDatLen:
            self.intIndex = 0

        str_result = self.listData[self.intIndex]
        self.intIndex += 1
        return str_result


class SeqGen(Generator):
    """
    Generate Result Based on a sequence. Now support only String.
    """
    G_INT = "int"
    G_TIME = "time"

    def __init__(self, str_template, str_seq_type):
        self.strTemplate = str_template

        if str_seq_type == self.__class__.G_INT:
            self.objBase = 0
            self.__GetNext = self.__GetNextInt

        elif str_seq_type == self.__class__.G_TIME:
            # Start time of today
            self.objBase = time.mktime(datetime.date.today().timetuple())
            self.__GetNext = self.__GetNextTime

    def __GetNextInt(self):
        self.objBase += 1
        return self.objBase

    def __GetNextTime(self):
        str_time = time.strftime("%H:%M:%S", time.localtime(self.objBase))
        self.objBase += 1
        return str_time

    def GetNext(self):
        return self.strTemplate % self.__GetNext()


def funcCreateRandomTUID():
    """
    Random Generate TUID : 12 - 8 - 4 - 4 - 4
    """

    str_uuid = '%036x'.upper() % random.randrange(G_UUIDMaxNum)
    return str('-').join([str_uuid[0:12], str_uuid[12:20], str_uuid[20:24], str_uuid[24:28], str_uuid[28:]])


def funcCreateRandomString(int_length):
    """
    Random Generate String
    """
    return lambda: ''.join(random.choice(string.ascii_uppercase) for x in range(int_length))


if __name__ == '__main__':
    objReturn = SeqGen(datetime.date.today().strftime("%Y-%m-%d") + " %s", SeqGen.G_TIME)
    print(objReturn.GetNext())
    print(objReturn.GetNext())
    print(objReturn.GetNext())
