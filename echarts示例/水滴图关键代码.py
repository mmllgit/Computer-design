import pysenti
import pandas as pd
import re
import jieba
import jieba.posseg
import jieba.analyse
import collections
import numpy
from PIL import Image               
import wordcloud     
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import ThemeType
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode
import pytorch
import tensorflow as tf
import sklearn
import seaborn






l1 = (
    Liquid()
    .add("正面情绪",
         [positive/mysum], 
         center=["60%", "50%"],
         color=['#5dbe8a'], 
         is_outline_show=False,
        label_opts=opts.LabelOpts(
        font_size=30,
        formatter=JsCode(
            """function (param) {
                    return ( Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
    ),
        )
    
)

l2 = Liquid().add(
    "负面情绪",
    [1-positive/mysum],
    color=['#ee3f4d'],
    center=["25%", "50%"],
    label_opts=opts.LabelOpts(
        font_size=30,
        formatter=JsCode(
            """function (param) {
                    return (  Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
    ),
    is_outline_show=False
).set_global_opts(title_opts=opts.TitleOpts(title="情感分析",pos_top='15%',pos_left='37%')
)

grid = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts())
grid.render("multiple_liquid.html")
