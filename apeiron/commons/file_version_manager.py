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
    def eq_txt(file_path_to_save, text):
        file_sha1 = FileVersionManager.hash(file_path_to_save)
        txt_sha1 = hashlib.sha1((text+"\n").encode('utf-8')).hexdigest()
        print(file_sha1)
        print(txt_sha1)
        if file_sha1 is txt_sha1:
            return True
        else :
            return False

    @staticmethod
    def exist(file_path):
        if not file_path.exists():
            Message.info("File not exist")
            return True
        else:
            Message.info("The file exist at: "+file_path.as_posix())
            return False

    @staticmethod
    def hash(file_path, mode='sha1'):
        h = hashlib.new(mode)
        with open(file_path, 'rb') as file:
            block = file.read(512)
            while block:
                h.update(block)
                block = file.read(512)

        return h.hexdigest()
