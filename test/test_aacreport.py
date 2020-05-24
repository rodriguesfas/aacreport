#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from aacreport.analysis import Analysis

dataset = '/home/fasr/Developer/aacreport/data/dataset/corpora/childes/Eng-UK-MOR/Barbara'

report = Analysis(dataset).FormatJSON()
print(report)
print(type(report))