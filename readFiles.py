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
#%%
def saveFigs(zipimgpath, outputpath, figname):
    image1 = z.open(zipimgpath).read()
    f = open(f'{outputpath}/{figname}.png','wb')
    f.write(image1)
    return f'{outputpath}/{figname}.png'
#%%
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


#%%
keys = list(dictsposition.keys())
textpt = ''
texten = ''
for i in range(len(keys)):
    figname = keys[i].replace(' ', '').replace(':','')
    outfigpath = saveFigs(dictsposition[keys[i]]['img'], f"./figures", figname)
    textpt += f'{keys[i]}\n'
    texten += f'{keys[i]}\n'
    if i+1 < len(keys):
        texTemppt = '\n'.join(texst[dictsposition[keys[i]]['pt']+1:dictsposition[keys[i+1]]['pt']])
        texTempen = '\n'.join(texst[dictsposition[keys[i]]['en']+1:dictsposition[keys[i+1]]['en']])
    else:
        texTemppt = '\n'.join(texst[dictsposition[keys[i]]['pt']+1:dictsposition[keys[0]]['en']])
        texTempen = '\n'.join(texst[dictsposition[keys[i]]['en']+1:])

    textpt += f'{texTemppt}\n'
    textpt += f"{outfigpath}\n"
    texten += f'{texTempen}\n'
    texten += f"{outfigpath}\n"

# %%
image1 = z.open('word/media/image1.png').read()
f = open('figures/image1.jpeg','wb')
f.write(image1)

#%%

# %%
