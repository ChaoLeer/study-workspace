#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'动态图'

__author__ = '作者'

from PIL import Image,ImageSequence
gif_name = 'gif'
gif = Image.open('%s.gif'%gif_name)
for i, frame in enumerate(ImageSequence.Iterator(gif), 1):
	# print(frame)
    frame.convert('RGB').save("./tmp/%s%d.jpg" % (gif_name, i))

import imageio
import os
frames = []
for x in os.listdir('./tmp'):
	if os.path.isfile(x) and os.path.splitext(x)[1] == '.jpg':
		print(x)
# print(os.listdir('./tmp'))
# x for x in os.listdir('./tmp') if os.path.isfile(x) and os.path.splitext(x)[1] == '.jpg' and os.path.splitext(x)[0].index(gif_name) > -1
# print(os.path.splitext('gif16.jpg')[0].index(gif_name))
# for x in [x for x in os.listdir('./tmp') if os.path.isfile(x) and ((os.path.splitext(x)[0].index(gif_name) > -1) and os.path.splitext(x)[1] == '.jpg')]:
# 	frames.append(imageio.imread('./tmp/%s'%x))
# imageio.mimsave('gif/as_t.gif', frames, 'GIF', duration=0.5)
