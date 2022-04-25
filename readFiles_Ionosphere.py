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
from polyglot.detect import Detector
from generateLatexFile import *


# %%
def saveFigs(zipf, zipimgpath, outputpath, figname):
    image1 = zipf.open(zipimgpath).read()
    f = open(f'{outputpath}/{figname}.png','wb')
    f.write(image1)
    return f'{outputpath}/{figname}.png'

def get_bold_list(para):
    bold_list = []
    for run in para.runs:
        bold_list.append(run.bold)
    return bold_list
def extractFiguresTextIonosphere(docPath, filename):

    z = zipfile.ZipFile(docPath+filename)
    all_files = z.namelist()
    images = [x for x in all_files if x.startswith('word/media/')]

    document = Document(docPath+filename)
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
    bold_list = []
    for run in para.runs:
        bold_list.append(run.bold)

    dictsposition = {}
    for nnb, bol in enumerate(bolds):
        dictsposition[bol] = {}
        dictsposition[bol]['img'] = images[nnb] 
        for nn, te in enumerate(texst):
            if te.startswith(bol):
                detector = Detector(texst[nn+1])
                if detector.language.code == 'pt':
                    dictsposition[bol]['pt'] = nn
                if detector.language.code == 'en':
                    dictsposition[bol]['en'] = nn

    return dictsposition, texst, z


def constructLatexFileIonosphere(docPath, filename, outputFigure):
    dictsposition, texst, zipf = extractFiguresTextIonosphere(docPath, filename)
    keys = list(dictsposition.keys())
    textpt = '\section{Ionosfera} \n \subsection{Responsável: Laysa Resende} \n \n'
    texten = '\section{Ionosphere} \n \subsection{Responsible: Laysa Resende} \n \n'
    for i in range(len(keys)):
        figname = keys[i].replace(' ', '').replace(':','')
        outfigpath = saveFigs(zipf, dictsposition[keys[i]]['img'], f"{outputFigure}", figname)
        textpt += '\\textbf{%s}\n\n \\begin{itemize}\n' % (keys[i])
        texten += '\\textbf{%s}\n\n \\begin{itemize}\n' % (keys[i])
        if i+1 < len(keys):
            textitempt = ''
            for ti in texst[dictsposition[keys[i]]['pt']+1:dictsposition[keys[i+1]]['pt']]:
                textitempt += '\\item ' + ti + '\n'
            textitemen = ''
            for ti in texst[dictsposition[keys[i]]['en']+1:dictsposition[keys[i+1]]['en']]:
                textitemen += '\\item ' + ti + '\n'
        else:
            textitempt = ''
            for ti in texst[dictsposition[keys[i]]['pt']+1:dictsposition[keys[0]]['en']]:
                textitempt += '\\item ' + ti + '\n'
            textitemen = ''
            for ti in texst[dictsposition[keys[i]]['en']+1:]:
                textitemen += '\\item ' + ti + '\n'

        includeFigure = "\\begin{figure}[H]\n    \\centering\n    \\includegraphics[width=14cm]{./%s}\n\\end{figure}\n" % '/'.join(outfigpath.split('/')[2:]) 

        textpt += f'{textitempt}'+ '\\end{itemize}\n'
        textpt += f"{includeFigure}\n"
        texten += f'{textitemen}' + '\\end{itemize}\n'
        texten += f"{includeFigure}\n"

    return textpt, texten



#%%


PATH = '/home/jose/python_projects/automatedPDFreading/data/'

filename = 'Sumário(06:12-13:12)_Laysa.docx'

textpt, texten = constructLatexFileIonosphere(PATH, filename, outputFigure='./latexText/figures')

generateLaTexFile(textpt, EnPt=False, outputPath='./latexText', date='25/04/2022')
# %%
