#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
import hashlib

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

    @staticmethod
    def hash(file_path):
        sha1sum = hashlib.sha1()
        with open(file_path, 'rb') as source:
            block = source.read(2**16)
            while len(block) != 0:
                sha1sum.update(block)
                block = source.read(2**16)
        return sha1sum.hexdigest()
