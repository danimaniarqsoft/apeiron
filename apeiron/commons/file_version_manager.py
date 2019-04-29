#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
import hashlib
import difflib
import re

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
        txt_sha1 = hashlib.sha1(text.encode()).hexdigest()
        if file_sha1 == txt_sha1:
            return True
        else:
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
        sha1 = hashlib.new(mode)
        with open(file_path, 'r') as file:
            block = file.read(512)
            while block:
                sha1.update(block.encode('utf8'))
                block = file.read(512)
        return sha1.hexdigest()

    @staticmethod
    def diff(left_file, right_file):
        opened_left_file = open(left_file).readlines()
        opened_right_file = open(right_file).readlines()
        for line in difflib.unified_diff(opened_left_file, opened_right_file):
            if re.search("^@@.*@@$", line):
                is_metadata = True
                Message.report(line, label='')
            elif re.search("^\\+", line) :
                is_plus_line = True
                Message.sucess(line, label='')
            elif re.search("^\\-", line):
                is_minus_line = True
                Message.failure(line, label='')
