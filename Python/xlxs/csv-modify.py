#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'read csv'

__author__ = 'ChaoLee'

import csv

with open('match.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['昵称'], row['编号'])