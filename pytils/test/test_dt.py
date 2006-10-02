# -*- coding: utf-8 -*-
# License: GNU GPL2
# Author: Pythy <the.pythy@gmail.com>
"""
Unit-tests for pytils.dt
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

import datetime
import time
import unittest

import pytils 

class DistanceOfTimeInWordsTestCase(unittest.TestCase):
    """
    Test case for pytils.dt.distance_of_time_in_words
    """

    def setUp(self):
        """
        Setting up environment for tests
        """
        self.time = 1156862275.7711999
        self.dtime = {}
        self.updateTime(self.time)

    def updateTime(self, _time):
        """Update all time-related values for current time """
        self.dtime['10sec_ago'] = _time - 10
        self.dtime['1min_ago'] = _time - 60
        self.dtime['10min_ago'] = _time - 600
        self.dtime['1hr_ago'] = _time - 3720
        self.dtime['10hr_ago'] = _time - 36600
        self.dtime['1day_ago'] = _time - 87600
        self.dtime['1day1hr_ago'] = _time - 90600
        self.dtime['2day_ago'] = _time - 87600*2

        self.dtime['in_10sec'] = _time + 10
        self.dtime['in_1min'] = _time + 61
        self.dtime['in_10min'] = _time + 601
        self.dtime['in_1hr'] = _time + 3721
        self.dtime['in_10hr'] = _time + 36601
        self.dtime['in_1day'] = _time + 87601
        self.dtime['in_1day1hr'] = _time + 90601
        self.dtime['in_2day'] = _time + 87600*2 + 1

    def ckDefaultAccuracy(self, typ, estimated):
        """
        Checks with default value for accuracy
        """
        t0 = time.time()
        # --- change state !!! attention
        self.updateTime(t0)
        # ---
        t1 = self.dtime[typ]
        res = pytils.dt.distance_of_time_in_words(from_time=t1, to_time=t0)
        # --- revert state to original value
        self.updateTime(self.time)
        # ---
        self.assertEquals(res, estimated)

    def ckDefaultToTime(self, typ, accuracy, estimated):
        """
        Checks with default value of time
        """
        t0 = time.time()
        # --- change state !!! attention
        self.updateTime(t0)
        # ---
        t1 = self.dtime[typ]
        res = pytils.dt.distance_of_time_in_words(t1, accuracy)
        # --- revert state to original value
        self.updateTime(self.time)
        # ---
        self.assertEquals(res, estimated)

    def testDOTIWDefaultAccuracy(self):
        """
        Unit-test for distance_of_time_in_words with default accuracy
        """
        self.ckDefaultAccuracy("10sec_ago", u"менее минуты назад")
        self.ckDefaultAccuracy("1min_ago", u"1 минуту назад")
        self.ckDefaultAccuracy("10min_ago", u"10 минут назад")
        self.ckDefaultAccuracy("1hr_ago", u"1 час назад")
        self.ckDefaultAccuracy("10hr_ago", u"10 часов назад")
        self.ckDefaultAccuracy("1day_ago", u"1 день назад")
        self.ckDefaultAccuracy("1day1hr_ago", u"1 день назад")
        self.ckDefaultAccuracy("2day_ago", u"2 дня назад")

        self.ckDefaultAccuracy("in_10sec", u"менее чем через минуту")
        self.ckDefaultAccuracy("in_1min", u"через 1 минуту")
        self.ckDefaultAccuracy("in_10min", u"через 10 минут")
        self.ckDefaultAccuracy("in_1hr", u"через 1 час")
        self.ckDefaultAccuracy("in_10hr", u"через 10 часов")
        self.ckDefaultAccuracy("in_1day", u"через 1 день")
        self.ckDefaultAccuracy("in_1day1hr", u"через 1 день")
        self.ckDefaultAccuracy("in_2day", u"через 2 дня")

    def testDOTIWDefaultToTimeAcc1(self):
        """
        Unit-tests for distance_of_time_in_words with default to_time and accuracy=1
        """
        # accuracy = 1
        self.ckDefaultToTime("10sec_ago", 1, u"менее минуты назад")
        self.ckDefaultToTime("1min_ago", 1, u"минуту назад")
        self.ckDefaultToTime("10min_ago", 1,  u"10 минут назад")
        self.ckDefaultToTime("1hr_ago", 1, u"час назад")
        self.ckDefaultToTime("10hr_ago", 1, u"10 часов назад")
        self.ckDefaultToTime("1day_ago", 1, u"вчера")
        self.ckDefaultToTime("1day1hr_ago", 1, u"вчера")
        self.ckDefaultToTime("2day_ago", 1, u"позавчера")

        self.ckDefaultToTime("in_10sec", 1, u"менее чем через минуту")
        self.ckDefaultToTime("in_1min", 1, u"через минуту")
        self.ckDefaultToTime("in_10min", 1, u"через 10 минут")
        self.ckDefaultToTime("in_1hr", 1, u"через час")
        self.ckDefaultToTime("in_10hr", 1, u"через 10 часов")
        self.ckDefaultToTime("in_1day", 1, u"завтра")
        self.ckDefaultToTime("in_1day1hr", 1, u"завтра")
        self.ckDefaultToTime("in_2day", 1, u"послезавтра")
        
    def testDOTIWDefaultToTimeAcc2(self):
        """
        Unit-tests for distance_of_time_in_words with default to_time and accuracy=2
        """
        # accuracy = 2
        self.ckDefaultToTime("10sec_ago", 2, u"менее минуты назад")
        self.ckDefaultToTime("1min_ago", 2, u"минуту назад")
        self.ckDefaultToTime("10min_ago", 2,  u"10 минут назад")
        self.ckDefaultToTime("1hr_ago", 2, u"1 час 2 минуты назад")
        self.ckDefaultToTime("10hr_ago", 2, u"10 часов 10 минут назад")
        self.ckDefaultToTime("1day_ago", 2, u"вчера")
        self.ckDefaultToTime("1day1hr_ago", 2, u"1 день 1 час назад")
        self.ckDefaultToTime("2day_ago", 2, u"позавчера")

        self.ckDefaultToTime("in_10sec", 2, u"менее чем через минуту")
        self.ckDefaultToTime("in_1min", 2, u"через минуту")
        self.ckDefaultToTime("in_10min", 2, u"через 10 минут")
        self.ckDefaultToTime("in_1hr", 2, u"через 1 час 2 минуты")
        self.ckDefaultToTime("in_10hr", 2, u"через 10 часов 10 минут")
        self.ckDefaultToTime("in_1day", 2, u"завтра")
        self.ckDefaultToTime("in_1day1hr", 2, u"через 1 день 1 час")
        self.ckDefaultToTime("in_2day", 2, u"послезавтра")
        
    def testDOTIWDefaultToTimeAcc3(self):
        """
        Unit-tests for distance_of_time_in_words with default to_time and accuracy=3
        """
        # accuracy = 3
        self.ckDefaultToTime("10sec_ago", 3, u"менее минуты назад")
        self.ckDefaultToTime("1min_ago", 3, u"минуту назад")
        self.ckDefaultToTime("10min_ago", 3,  u"10 минут назад")
        self.ckDefaultToTime("1hr_ago", 3, u"1 час 2 минуты назад")
        self.ckDefaultToTime("10hr_ago", 3, u"10 часов 10 минут назад")
        self.ckDefaultToTime("1day_ago", 3,
                                u"1 день 0 часов 20 минут назад")
        self.ckDefaultToTime("1day1hr_ago", 3,
                                u"1 день 1 час 10 минут назад")
        self.ckDefaultToTime("2day_ago", 3,
                                u"2 дня 0 часов 40 минут назад")

        self.ckDefaultToTime("in_10sec", 3, u"менее чем через минуту")
        self.ckDefaultToTime("in_1min", 3, u"через минуту")
        self.ckDefaultToTime("in_10min", 3, u"через 10 минут")
        self.ckDefaultToTime("in_1hr", 3, u"через 1 час 2 минуты")
        self.ckDefaultToTime("in_10hr", 3, u"через 10 часов 10 минут")
        self.ckDefaultToTime("in_1day", 3,
                                u"через 1 день 0 часов 20 минут")
        self.ckDefaultToTime("in_1day1hr", 3,
                                u"через 1 день 1 час 10 минут")
        self.ckDefaultToTime("in_2day", 3,
                                u"через 2 дня 0 часов 40 минут")

    def testDOTIWExceptions(self):
        """
        Unit-tests for testings distance_of_time_in_words' exceptions
        """
        self.assertRaises(TypeError, pytils.dt.distance_of_time_in_words, "test")
        self.assertRaises(TypeError, pytils.dt.distance_of_time_in_words, time.time(), "test")
        self.assertRaises(TypeError, pytils.dt.distance_of_time_in_words, time.time(), 2, "test")
        self.assertRaises(ValueError, pytils.dt.distance_of_time_in_words, time.time(), 0)

class RuStrftimeTestCase(unittest.TestCase):
    """
    Test case for pytils.dt.ru_strftime
    """

    def setUp(self):
        """
        Setting up environment for tests
        """        
        self.date = datetime.date(2006, 8, 25)
    
    def ck(self, format, estimates):
        """
        Checks w/o inflected
        """
        res = pytils.dt.ru_strftime(format, self.date)
        self.assertEquals(res, estimates)

    def ckInflected(self, format, estimates):
        """
        Checks with inflected
        """
        res = pytils.dt.ru_strftime(format, self.date, True)
        self.assertEquals(res, estimates)

    def ckInflectedDay(self, format, estimates):
        """
        Checks with inflected day
        """
        res = pytils.dt.ru_strftime(format, self.date, inflected_day=True)
        self.assertEquals(res, estimates)

    def testRuStrftime(self):
        """
        Unit-tests for pytils.dt.ru_strftime
        """
        self.ck(u"тест %a", u"тест пт")
        self.ck(u"тест %A", u"тест пятница")
        self.ck(u"тест %b", u"тест авг")
        self.ck(u"тест %B", u"тест август")
        self.ckInflected(u"тест %B", u"тест августа")
        self.ckInflected(u"тест выполнен %d %B %Y года",
                          u"тест выполнен 25 августа 2006 года")
        self.ckInflectedDay(u"тест выполнен в %A", u"тест выполнен в пятницу")

    def testRuStrftimeExceptions(self):
        """
        Unit-tests for testing pytils.dt.ru_strftime's exceptions
        """
        self.assertRaises(TypeError, pytils.dt.ru_strftime, time.time())
        self.assertRaises(TypeError, pytils.dt.ru_strftime, u"%Y.%m.%d%", time.time())
        

if __name__ == '__main__':
    unittest.main()
