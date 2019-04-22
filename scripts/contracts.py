# -*- coding: utf-8 -*-

from collections import namedtuple

Contract_tuple = namedtuple('Contract', ['address', 'abi'])
Contract_tuple.__new__.__defaults__ = (None, None)


COMPLIER = Contract_tuple('0x7f8601798ffb0861b167739a1dd23303a313c62d', loads([{"constant":false,"inputs":[],"name":"kill","outputs":[],"type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"burnedValueOf","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"_owner","type":"address"}],"name":"delegate","outputs":[],"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"type":"function"},{"constant":false,"inputs":[{"name":"_token","type":"address"},{"name":"_value","type":"uint256"}],"name":"burn","outputs":[],"type":"function"}]))

VCU = Contract_tupleloads('0x259E4B009a1611F47231975BF9f5a585c70fe591', loads())
