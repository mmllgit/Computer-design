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
from pyecharts.globals import ThemeType,SymbolType
import pytorch
import tensorflow as tf
import sklearn
import seaborn


my_wordcloud = []
times = 0
for k,v in dfRes.items():
    my_wordcloud.append(((k),(v*7)))
    times += 1

def wordcloud_base() -> WordCloud:
    c = (
    WordCloud(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add("", my_wordcloud, word_size_range=[20, 100], shape=SymbolType.ROUND_RECT)
        .set_global_opts(title_opts=opts.TitleOpts(""))
)
    return c

wordcloud_base().render('云图.html')