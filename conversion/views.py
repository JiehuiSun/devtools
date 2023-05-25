# -*- coding: utf-8 -*-


from api import Api


class Dict2JsonView(Api):
    async def post(self):
        return self.ret()
