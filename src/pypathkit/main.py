import os


def file_put(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)


def file_get(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def file_delete(filename):
    if os.path.exists(filename):
        os.remove(filename)


def file_exists(filename):
    return os.path.exists(filename)
