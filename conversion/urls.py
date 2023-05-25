# -*- coding: utf-8 -*-

from .views import Dict2JsonView

routing_dict = dict()

routing_dict["/v1/dict2json/"] = Dict2JsonView

routing_dict.update(routing_dict)
