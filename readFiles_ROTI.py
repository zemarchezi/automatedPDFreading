#%%
from PIL import Image
import numpy as np
from io import BytesIO
import fitz
from matplotlib import image
from generateLatexFile import *
from pdf2image import convert_from_path
from polyglot.detect import Detector
import cv2
import matplotlib.pyplot as plt
import re
#%%

def extractItemize_Scint(text):
    texs = """\\begin{itemize} \n """
    for i in text.split('•'):
        if len(i) > 1:
            texs += '\\item ' + ' '.join(i.split('\n')) +'\n'
            if i.startswith('TEC'):
                texs += '\\subsectoin{%s}' %(i) +'\n'
    
    texs += """\\end{itemize} \n """

    return texs


def saveFigs(pages, page, outputpath, figname, crop):
    with BytesIO() as image_byte_array:
        pages[page].save(image_byte_array, format='PNG')
        image_to_extract = image_byte_array.getvalue()
        img = cv2.imdecode(np.frombuffer(image_to_extract, np.uint8),3)
        imgCropped = img[crop[0]:crop[1],crop[2]:crop[3]]
    cv2.imwrite(f'{outputpath}/{figname}.png',imgCropped)
    return f'{outputpath}/{figname}.png'

#%%
def extractFiguresTextScint(docPath, filename, outputimage):

    pages = convert_from_path(docPath + filename, 500)


    textDict = {"Tabela": {'page': 0, 
                              'crop': [1500,4000,250,3800]},
                  "imager": {'page': 1,
                              'regex_en': r"(?<=Remarks.)(.|\n)*",
                              'regex_pt': r"(?<=Observacoes.)(.|\n)*(?=Remarks)"},
                  "tec": {'page': 2,
                              'regex_en': r"(?<=Remarks.)(.|\n)*",
                              'regex_pt': r"(?<=Observacoes.)(.|\n)*(?=Remarks)"}
                  }
    includeFigure = """\\begin{figure}[H]\n    
                        \\centering\n   
                             \\includegraphics[width=14cm]{./%s}\n
                        \\end{figure}\n
                     """
    keys = list(textDict.keys())
    ttextEn = ''
    ttextPt = ''
    # ttextPt = '\section{Imageador All-Sky} \n \subsection{Responsável: LUME} \n \n'
    # ttextEn = '\section{All-Sky Imager} \n \subsection{Responsible: LUME} \n \n' 

    
    for i in range(len(keys)):
        if 'regex_en' not in list(textDict[keys[i]].keys()):
            crops = textDict[keys[i]]['crop']
            outfigpath = saveFigs(pages, textDict[keys[i]]['page'], 
                                f"{outputimage}", f'figureScint_{i}', 
                                crops)
            # includeFigure % ('/'.join(outfigpath.split('/')[2:]))
        else:
            if keys[i] == 'tec':
                ttextPt += 'TEC \n'
                ttextEn += 'TEC \n'
            doc = fitz.open(docPath + filename)
            text = doc[textDict[keys[i]]['page']].get_text()
            text = re.sub('[\¸\˜\´\❘❙❚]+', '', text)
            matches = re.search(textDict[keys[i]]['regex_en'], text, re.MULTILINE)
            
            if matches:
                ttextEn += extractItemize_Scint(matches.group())
            matches = re.search(textDict[keys[i]]['regex_pt'], text, re.MULTILINE)
            if matches:
                ttextPt += extractItemize_Scint(matches.group())

    return ttextEn, ttextPt

#%%

PATH = './data/'

filename = 'EMBRACE_BRIEFING_REPORT_24.04-30.04_Prosper.pdf'

#%%
texten, textpt = extractFiguresTextScint(PATH, filename, outputimage='./latexText/figures/')
generateLaTexFile(textpt, EnPt=True, outputPath='./latexText', date='2022/04/25')

#%%
