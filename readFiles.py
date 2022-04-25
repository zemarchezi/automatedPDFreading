#%%
import pandas as pd
import numpy as np
import os
import pytesseract
from pdfminer.high_level import extract_text
import fitz
import io
from PIL import Image
from docx import Document
import zipfile
import enchant
# %%
dictionaryEng = enchant.Dict("en_US")
dictionaryBrl = enchant.Dict("pt_BR")
#%%

PATH = '/home/jose/python_projects/automatedPdfReading/data/'

filename = 'Sumário(06:12-13:12)_Laysa.docx'


# %%

z = zipfile.ZipFile(PATH+filename)
all_files = z.namelist()
images = [x for x in all_files if x.startswith('word/media/')]


def get_bold_list(para):
    bold_list = []
    for run in para.runs:
        bold_list.append(run.bold)
    return bold_list

document = Document(PATH+filename)
texst = list()
bolds = []
for para in document.paragraphs:
    bold_list = get_bold_list(para)
    if True in bold_list:
        if len(para.text) > 0:
            bolds.append(para.text)
    bolds = list(dict.fromkeys(bolds))
    if len(para.text) > 0:
        texst.append(para.text)


#%%

bold_list = []
for run in para.runs:
    bold_list.append(run.bold)
#%%
ssa = ''
dictsposition = {}
for nnb, bol in enumerate(bolds):
    dictsposition[bol] = {}
    dictsposition[bol]['img'] = images[nnb] 
    for nn, te in enumerate(texst):
        if te.startswith(bol):
            if dictionaryBrl.check(texst[nn+1].split(' ')[0]):
                dictsposition[bol]['pt'] = nn
            if dictionaryEng.check(texst[nn+1].split(' ')[0]):
                dictsposition[bol]['en'] = nn

# %%
image1 = z.open('word/media/image1.png').read()
f = open('figures/image1.jpeg','wb')
f.write(image1)

#%%

# %%
