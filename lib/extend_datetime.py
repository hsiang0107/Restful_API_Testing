import datetime
import time
from lib.ConfigHelper import ConfigHelper


class ExtendDateTime(object):
    time_format = ConfigHelper().get_data_from_config('Time Format')
    date_format = time_format.split(' ')[0] + ' 00:00:00'

    @classmethod
    def current_time(cls):
        return datetime.datetime.now().strftime(cls.time_format)

    @classmethod
    def today(cls):
        return datetime.datetime.now().strftime(cls.date_format)

    @classmethod
    def get_date_by_offset(cls, offset, base_time=datetime.datetime.now()):
        if isinstance(base_time, str):
            base_time = datetime.datetime.strptime(base_time, cls.time_format)
        if isinstance(offset, datetime.timedelta):
            target_date = base_time + offset
        else:
            delta = datetime.timedelta(days=int(offset[1:]))
            target_date = eval("base_time %s delta" % offset[0])
        return target_date

    @classmethod
    def get_time_stamp_by_offset(cls, offset):
        target_date = cls.get_date_by_offset(offset)
        return str(time.mktime(target_date.timetuple())).split('.')[0]
