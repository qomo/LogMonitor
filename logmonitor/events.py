#-*- coding:utf-8 -*-
import re, datetime

class BaseEvent(object):
    event_type = "base_event"
    
    def __init__(self, raw_log_str, timeformat='%m-%d %H:%M:%S.%f',
                 time_re_parttern='^\d+-\d+ \d+:\d+:\d+.\d+'):
        self.__raw_log_str = raw_log_str
        self.__timeformmat = timeformat
        self.__time_re_parttern = time_re_parttern
        self.__timestamp = self._parseTimestamp()

    def _parseTimestamp(self):
        match = re.search(self.__time_re_parttern, self.__raw_log_str)
        dt = datetime.datetime.strptime(match.group(), self.__timeformmat)
        return dt.replace(datetime.datetime.now().year)

    def getEventType(self):
        return self.event_type

    def getTimestamp(self):
        return self.__timestamp
