#! /usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum


class MessageType(Enum):
    SUCCESS = 'green'
    INFO = 'blue'
    WARNING = 'yellow'
    ERROR = 'red'
