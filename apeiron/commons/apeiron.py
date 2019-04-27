#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
import json
from pathlib import Path
from apeiron.commons.message_type import MessageType
from apeiron.commons.message import Message
from apeiron.commons.file_version_manager import FileVersionManager
import glob
from datetime import datetime


class Apeiron:

    @staticmethod
    def init():
        Path(Apeiron.apeirondir()).mkdir(parents=True, exist_ok=True)
        data = {'author':'apeiron','gendate':datetime.today().strftime('%Y%m%d')}  
        with open(Apeiron.apeironconfig(), 'w+') as outfile:  
            json.dump(data, outfile, indent=4)
            Path(Apeiron.apeironconfig()).touch()

    @staticmethod
    def isapeiron():
        if glob.glob(Apeiron.apeirondir()):
            return True
        else:
            return False
    
    @staticmethod
    def apeirondir():
        return '.apeiron'

    @staticmethod
    def apeironconfig():
        return Apeiron.apeirondir() + '/' + 'config.json' 

    @staticmethod
    def savestate(key, value):
        with open(Path('.apeiron/config.json'), 'r+') as f:
            data = json.load(f)
            data[key] = value # <--- add `id` value.
            f.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, f, indent=4)
            f.truncate()     # remove remaining part
