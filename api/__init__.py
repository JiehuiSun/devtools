# -*- coding: utf-8 -*-


from sanic.request import Request
from sanic.response import json, text
from sanic.views import HTTPMethodView

from . import errors


class Api(HTTPMethodView):
    decorators = []

    def __init__(self, *args, **kwargs):
        self.params_dict: dict = {}
        self.request: Request = None
        self.key: str = None
        self.data: dict = None
        self.call_method: str = None

    async def dispatch_request(self, *args, **kwargs):
        self.request = args[0]
        self.key = kwargs.get("key")
        await self._handle_params()
        await self._dispatch()
        method = getattr(self, self.call_method, None)
        if not method:
            raise errors.MethodError()

        _pre_h = await self._pre_handle()
        if _pre_h:
            return _pre_h
        result = await method()

        await self._after_handle()

        if isinstance(result, dict):
            return json(result)
        elif isinstance(result, str):
            return text(result)
        else:
            return result

    async def _handle_params(self, *args, **kwargs):
        """
        处理参数
        """
        if self.request.method.lower() != 'get':
            self.data = self.request.json
        else:
            self.data = dict(self.request.query_args)

    async def _dispatch(self, *args, **kwargs):
        self.call_method = self.request.method.lower()
        if self.call_method == 'get' and not self.key:
            self.call_method = 'list'

    async def _pre_handle(self, *args, **kwargs): ...

    async def _after_handle(self, *args, **kwargs): ...

    def ret(self, data: dict = None) -> dict:
        """json res"""
        return {
            "errCode": 0,
            "errMsg": "OK",
            "data": data
        }

    def error(self, errcode: int, errmsg: str = None) -> dict:
        """"""
        if not errmsg and errcode:
            errmsg = errors.API_ERROR.get(errcode)
            if not errmsg:
                errmsg = errors.API_ERROR[10101]
        return {
            "errCode": errcode,
            "errMsg": errmsg
        }
