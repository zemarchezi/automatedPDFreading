#%%
from PIL import Image
from io import StringIO
import matplotlib.pyplot as plt
from docx import Document
import zipfile
from polyglot.detect import Detector
from generateLatexFile import *
import cv2
import numpy as np

# %%
def saveFigs(zipf, zipimgpath, outputpath, figname, crop):
    image1 = zipf.open(zipimgpath).read()
    img = cv2.imdecode(np.frombuffer(image1, np.uint8),3)
    if crop:
        imgCropped = img[crop[0]:crop[1],crop[2]:crop[3]]
    else:
        imgCropped = img
    cv2.imwrite(f'{outputpath}/{figname}.png',imgCropped)
    return f'{outputpath}/{figname}.png'

def get_bold_list(para):
    bold_list = []
    for run in para.runs:
        bold_list.append(run.bold)
    return bold_list

def extractFiguresTextRadBelts(docPath, filename):

    z = zipfile.ZipFile(docPath+filename)
    all_files = z.namelist()
    images = [x for x in all_files if x.startswith('word/media/')]

    document = Document(docPath+filename)
    texs= []
    for para in document.paragraphs:
        texs.append(para.text)

    dictsposition = {}
    fig = 0
    for n, i in enumerate(texs):
        if i.startswith('Fig'):
            fig += 1
            dictsposition[f"Figure_{fig}"] = {'leg': i,
                                              'fig': images[fig-1]}
        if i.startswith('Summary') or i.startswith('Resumo'):
            dictsposition[f"locSummary"] = n

    return dictsposition, texs, z


def constructLatexFileRadBelts(docPath, filename, outputFigure):
    dictsposition, texst, zipf = extractFiguresTextRadBelts(docPath, filename)
    keys = list(dictsposition.keys())
    detector = Detector(dictsposition[keys[1]]['leg'])
    if detector.language.code == 'pt':
        text = '\section{ROTI} \n \subsection{Responsável: Carolina de Sousa do Carmo} \n \n'
    if detector.language.code == 'en':
        text = '\section{ROTI} \n \subsection{Responsible: Carolina de Sousa do Carmo} \n \n'
    keys = list(dictsposition.keys())
    
    includeFigure = """\\begin{figure}[H]\n    
                        \\centering\n   
                             \\includegraphics[width=14cm]{./%s}\n
                             \\caption{%s}
                        \\end{figure}\n
                     """

    
    for i in range(len(keys)):
        if keys[i].startswith("Fig"):

            if keys[i].endswith("1"):
                crops = False
            if keys[i].endswith("2"):
                crops = False
            outfigpath = saveFigs(zipf, dictsposition[keys[i]]['fig'], f"{outputFigure}", f'figureRadBelts_{i}', crops)

            text += includeFigure % ('/'.join(outfigpath.split('/')[2:]), dictsposition[keys[i]]['leg'])

    
    textSum = '\n\n'.join(texst[dictsposition['locSummary']+1:])
    text += textSum


    return text



PATH = './data/'

filename = 'Resumo_semana2207_Carolina.docx'

#%%
# ssa = extractFiguresTextRadBelts(PATH, filename)
ssa = constructLatexFileRadBelts(PATH, filename, outputFigure='./latexText/figures')

generateLaTexFile(ssa, EnPt=False, outputPath='./latexText', date='25/04/2022')
# %%

# %%
