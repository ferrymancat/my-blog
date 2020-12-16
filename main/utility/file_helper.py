#!/usr/bin/env python
#  -*- coding: utf-8 -*
"""
文件帮助类
"""
from os.path import abspath, dirname, join
import hashlib


def build_abs_path_by_file(related_file, relative_file_path):
    """
    根据传入的文件及文件所在的相对路径来构建绝对路径
    :param related_file: 传入的文件
    :param relative_file_path: 传入文件的相对路径
    :return: 传入文件的绝对路径
    """
    cur_path = dirname(abspath(related_file))
    return join(cur_path, relative_file_path)


def checksum_by_bytes(file_blob: bytes) -> str:
    """
    获取bytes的MD5值，用于监测文件是否同一个
    :param file_blob:
    :return:
    """
    md5_obj = hashlib.md5()
    md5_obj.update(file_blob)
    hash_code = md5_obj.hexdigest()
    return str(hash_code).lower()
