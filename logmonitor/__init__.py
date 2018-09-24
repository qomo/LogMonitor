# -*- coding:utf-8 -*-
import time


class Logcat(object):
    LOGCAT = None

    def __init__(self):
        self.__is_running = False
        self.__logcat_cmd = 'logcat -d'
        self.__executor = None # 执行logcat的函数
        self.__save_path = r'D:/logcat.log'
        self.__event_monitors = []
        self.__monitor_strs = []
        self.__run_period = 30 # seconds
        
    def getInstance():
        if Logcat.LOGCAT == None:
            Logcat.LOGCAT = Logcat()
        return Logcat.LOGCAT

    def setExecutor(self, executor):
        self.__executor = executor

    def setSavePath(self, save_path):
        # check save_path is valid path
        self.__save_path = save_path

    def run(self):
        self.__is_running = True
        while self.__is_running:
            ret = self.__executor(self.__logcat_cmd)
            for i in ret:
                self._notify(i)
            time.sleep(self.__run_period)

    def stop(self):
        self.__is_running = False

    def _notify(self, raw_log_str):
        for monitor in self.__event_monitors:
            monitor.update(raw_log_str)

    def registerMonitor(self, monitor):
        if monitor in self.__event_monitors:
            return
        self.__event_monitors.append(monitor)
        self.__monitor_strs.append(monitor.getMonitorStr())

    def removeMonitor(self, monitor):
        self.__event_monitors.remove(monitor)
        self.__monitor_strs.remove(monitor.getMonitorStr())
