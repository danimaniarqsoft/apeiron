#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
from .message_type import MessageType
from pathlib import Path

class Files:

    @staticmethod
    def save(file, text):
        file_path_to_save = Path(os.getcwd()) / file
        with open(file_path_to_save, "w+") as file:
            file.write(text)
        return file_path_to_save
