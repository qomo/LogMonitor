#-*- coding:utf-8 -*-
from .events import BaseEvent

class BaseEventMonitor(object):
    event_type = "base_event"

    def __init__(self, monitor_str):
        self.__monitor_str = monitor_str
        self.__event_buffer = []

    @staticmethod
    def buildEventMonitor(monitor_str):
        return BaseEventMonitor(monitor_str)

    def update(self, raw_log_str):
        if self.__monitor_str in raw_log_str:
            self.__event_buffer.append(BaseEvent(raw_log_str))

    def getMonitorStr(self):
        return self.__monitor_str

    def getLastEvent(self):
        if not self.__event_buffer:
            return None
        return self.__event_buffer[-1]

    def getEventCount(self):
        return len(self.__event_buffer)
                  
    def cleanBuffer(self):
        self.__event_buffer = []
