# -*- coding: utf-8 -*-

"""
    100xx: public system
    101xx: public service
    20xxx: conversion
"""


class BaseError(Exception):
    errno = 10000
    errmsg = 'system error'

    def __init__(self, errmsg=None):
        if errmsg:
            self.errmsg = errmsg


# 业务错误码
API_ERROR = {
    0: "OK",
}
