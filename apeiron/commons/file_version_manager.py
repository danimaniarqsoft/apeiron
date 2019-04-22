#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
from pathlib import Path
from apeiron.commons.message import Message
from apeiron.commons.message_type import MessageType

class FileVersionManager:

    @staticmethod
    def diff(left_file, right_file):
        pass

    @staticmethod
    def exist(file_path):
        if not file_path.exists():
            Message.info("File not exist")
            return True
        else:
            Message.info("The file exist at: "+file_path.as_posix())
            return False