#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
from enum import Enum

from pathlib import Path
from apeiron.commons.message_type import MessageType
from apeiron.commons.message import Message
from apeiron.commons.file_version_manager import FileVersionManager

class Files(Enum):
    SAVE_OK = 0
    SAVE_ERROR_FILE_EXIST = 1
    FAILURE = 2
    FILE_EXIST = 3
    FILE_NOT_EXIST = 4
