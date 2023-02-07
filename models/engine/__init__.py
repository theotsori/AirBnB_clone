#!/usr/bin/python3

from models.engine.file_storage import FileStorage

storage = None

def create_storage():
    global storage
    if storage is None:
        storage = FileStorage()
        storage.reload()

create_storage()