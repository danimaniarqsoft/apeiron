#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
from pathlib import Path
from apeiron.commons.message_type import MessageType
from apeiron.commons.message import Message
from apeiron.commons.file_version_manager import FileVersionManager

class Files:

    '''
    FILE EXIST AND IS THE SAME -> not write and skipt, print warning
    FILE EXIST AND IS DIFFERENT -> make a diff and not save it
    FILE NOT EXIST -> just save it and print where is save it, return path
    '''
    @staticmethod
    def save(text, dir_path_to_save, file_name, force_override=False):
        file_path_to_save = dir_path_to_save / file_name
        if not file_path_to_save.exists() or force_override:
            return Files.write_to_file(file_path_to_save, text, force_override)
        elif FileVersionManager.eq_txt(file_path_to_save, text):
            Message.warning('skipt - This are the same :: ' + file_path_to_save.as_posix())
            return True
        else:
            Message.error('file conflicts!  ' + file_path_to_save.as_posix())
            return False

    @staticmethod
    def write_to_file(file_path_to_save, text, force_override=False):
        with open(file_path_to_save, mode="w+", encoding="utf-8") as file:
            file.write(text)
            if force_override:
                Message.warning('Overriding file at:', file_path_to_save.as_posix())
            else:
                Message.info('Adding file to:', file_path_to_save.as_posix())
            return True
