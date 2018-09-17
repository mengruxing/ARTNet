#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def get_project_path(*paths):
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), *paths)


def check_sys_path(path):
    if path is None or path == '':
        path = '.'
    if path not in sys.path:
        sys.path.insert(0, path)


PROJECT_PATH = get_project_path()
