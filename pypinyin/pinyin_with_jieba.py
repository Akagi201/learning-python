# coding: utf-8
from pypinyin import lazy_pinyin, load_phrases_dict, TONE2
hans = u'桔子'
print(lazy_pinyin(hans, style=TONE2))
