#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 21:17
# @Author  : Paulson
# @File    : test.py
# @Software: PyCharm
# @define  : function

from redis_util import get_today, get_visit_num_all, get_visit_num_today, inc_visit_num

if __name__ == '__main__':
    inc_visit_num()
    print(get_visit_num_all())
    print(get_visit_num_today())
    print(get_today())