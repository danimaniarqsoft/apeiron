#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
from pathlib import Path
from apeiron.commons.message_type import MessageType
from apeiron.commons.message import Message
from apeiron.commons.file_version_manager import FileVersionManager

class Files:

    @staticmethod
    def save(text, file_name, dir_path_to_save=Path(os.getcwd())):
        file_path_to_save = dir_path_to_save / file_name
        if not file_path_to_save.exists():
            with open(file_path_to_save, mode="w+", encoding="utf-8") as file:
                file.write(text)
            Message.info('Saving file to: ' + file_path_to_save.as_posix())
            return True
        elif FileVersionManager.eq_txt(file_path_to_save, text):
            Message.info('Same Hash, hence are the same ' + file_path_to_save.as_posix())
            return False
        else:
            Message.info('The files are differents!!!')
            return False


