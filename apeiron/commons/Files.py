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
        if not file_path_to_save.exist():
            with open(file_path_to_save, "w+") as file:
                file.write(text)

            return file_path_to_save
        else:
            return None


