import MeCab

mecab = MeCab.Tagger('-Ochasen')
sent ="今日は電通大へ行きそばを食べました。"
print(mecab.parse(sent))