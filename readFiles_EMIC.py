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
#%%

def saveFigs(pages, page, outputpath, figname):
    with BytesIO() as image_byte_array:
        pages[page].save(image_byte_array, format='PNG')
        image_to_extract = image_byte_array.getvalue()
        img = cv2.imdecode(np.frombuffer(image_to_extract, np.uint8),3)
    cv2.imwrite(f'{outputpath}/{figname}.png',img)
    return f'{outputpath}/{figname}.png'

#%%
def extractFiguresTextULF(docPath, filename, outputimage):
    textPt = ''
    textEn = ''
    

    pages = convert_from_path(docPath + filename, 500)

    includeFigure = """\\begin{figure}[H]\n    
                        \\centering\n   
                             \\includegraphics[width=14cm]{./%s}\n
                        \\end{figure}\n
                     """
    textpt = '\section{Ondas EMIC} \n \subsection{Responsável: Claudia Medeiros} \n \n'
    texten = '\section{EMIC Waves} \n \subsection{Responsible: Claudia Medeiros} \n \n' 
    for i in range(1,len(pages)):
        outfigpath = saveFigs(pages, i, 
                             f"{outputimage}", f'figureEMIC_{i}')
        
        textpt += includeFigure % ('/'.join(outfigpath.split('/')[2:]))
        texten += includeFigure % ('/'.join(outfigpath.split('/')[2:]))

    textPt += textpt
    textEn += textpt

    return textPt, textEn

#%%

PATH = '/home/jose/python_projects/automatedPdfReading/data/'

filename = 'briefing_ULF_EMIC_02_05_2022.pdf'

#%%
texten, textpt = extractFiguresTextULF(PATH, filename, outputimage='./latexText/figures/')
generateLaTexFile(textpt, EnPt=True, outputPath='./latexText', date='2022/04/25')

# img = cv2.imdecode(np.frombuffer(img_page, np.uint8),3) 
# imgCropped = img[crop[0]:crop[1],crop[2]:crop[3]]


# cv2.imwrite(f'{outputpath}/{figname}.png',imgCropped)
# %%
