#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 10:53
# @File    : jd_try.py
# @Project : 京东试用

class JdTry:

    def __init__(self, pt_pin, pt_key):
        self._cookies = {
            'pt_pin': pt_pin,
            'pt_key': pt_key
        }
