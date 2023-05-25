# -*- coding: utf-8 -*-


from sanic import Sanic


app = Sanic.get_app("devtools")

__all__ = ["app"]
