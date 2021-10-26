# -*- coding: utf-8 -*-
import sys, os, time, random

from functools import partial
from collections import namedtuple
from itertools import product

import pandas as pd

#def cost_thick(in_thick,out_thick,in_thick_up,in_thick_down):




usecol = {'材料号':'No','入口厚度':'in_thick','入厚上跳':'in_thick_up', '入厚下跳':'in_thick_down', '入口宽度':'in_width',\
           '宽反值3(a3)':'in_width_up', '宽跳上限(a4)':'in_width_down','退火温度':'temp', '温度上跳':'temp_up','温度下跳':'temp_down'}
df_ori = pd.read_excel('./oridata.xlsx',usecols = list(usecol.keys()))
df_ori = df_ori.rename(columns=usecol)
df_ori.in_width_up = df_ori.in_width + df_ori.in_width_up
df_ori.in_width_down = df_ori.in_width + df_ori.in_width_down
