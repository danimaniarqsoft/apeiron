#! /usr/bin/env python
# -*- coding: utf-8 -*-
import click
import os
from pathlib import Path
from apeiron.commons.message_type import MessageType
from apeiron.commons.message import Message
from apeiron.commons.file_version_manager import FileVersionManager
import glob

class Apeiron:

    '''
    FILE EXIST AND IS THE SAME -> not write and skipt, print warning
    FILE EXIST AND IS DIFFERENT -> make a diff and not save it
    FILE NOT EXIST -> just save it and print where is save it, return path
    '''
    
    @staticmethod
    def isapeiron():
        if glob.glob('.apeiron'):
            return True
        else:
            return False
    
    @staticmethod
    def init():
        Path('.apeiron').mkdir(parents=True, exist_ok=True)
