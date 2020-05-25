import jieba
jieba.enable_paddle()
jieba.enable_parallel(4)
import jieba.posseg as pseg
pdf_file = '/Users/vanxv/Downloads/500Libary/chaoyuezhishang.pdf'
import pdftotext
from collections import Counter
from wordcloud import WordCloud




def analysis(text):
    cnt = Counter()
    for word in text:
        cnt[word] += 1
    cnt.most_common()
    print(cnt)

def deal_text(text):
    flag_array = ("n","t",'PER','ORG','ORG','TIME') # https://github.com/fxsjy/jieba
    text = text.replace("\n", " ")
    text = text.replace(" ", "")
    seg_list = pseg.cut(text,use_paddle=True)
    new_text = []
    for word, flag in seg_list:
        # print('%s %s' % (word, flag))
        if(flag.endswith(flag_array)):
            new_text.append(word)

    analysis(new_text)


def read_pdf():
    text = ''
    with open(pdf_file, "rb") as f:
        pdf = pdftotext.PDF(f)
        for page in pdf:
            text +=page
    deal_text(text)

read_pdf()
