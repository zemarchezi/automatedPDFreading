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

def saveFigs(pages, page, outputpath, figname, crop):
    with BytesIO() as image_byte_array:
        pages[page].save(image_byte_array, format='PNG')
        image_to_extract = image_byte_array.getvalue()
        img = cv2.imdecode(np.frombuffer(image_to_extract, np.uint8),3)
        imgCropped = img[crop[0]:crop[1],crop[2]:crop[3]]
    cv2.imwrite(f'{outputpath}/{figname}.png',imgCropped)
    return f'{outputpath}/{figname}.png'

#%%
def extractFiguresTextULF(docPath, filename, outputimage):
    ttextEn = ''
    ttextPt = ''
    with fitz.open(docPath + filename) as doc:
        for page in range(-2,0):
            text = doc[page].get_text()
            detector = Detector(text)
            if detector.language.code == 'pt':
                ttextPt += text
            if detector.language.code == 'en':
                ttextEn += text

    ttextEn += ' '.join(ttextEn.split('\n')[:-3])
    ttextPt += ' '.join(ttextPt.split('\n')[:-3])
    


    pages = convert_from_path(docPath + filename, 500)


    imagesDict = {"FigISLL": {'page': 1,
                              'leg_pt': """a) sinal do campo magnético total 
                              medido na Estação ISLL da rede CARISMA em cinza, 
                              junto com a flutuação na faixa de Pc5 em preto. b) 
                              Espectro de potência wavelet do sinal filtrado. c) 
                              Média da potência espectral nas faixas de 2 a 10 minutos 
                              (ondas ULF).""",
                              'leg_en': """a) signal of the total magnetic 
                              field measured in the ISLL Station of the CARISMA 
                              network in gray, together with the fluctuation in the 
                              range of Pc5 in black. b) Wavelet power spectrum of the 
                              filtered signal. c) Average spectral power in the ranges 
                              from 2 to 10 minutes (ULF waves).""", 
                              'crop': [260,1650,200,2900]},
                  "FigEmbrace": {'page': 2,
                              'leg_pt': """a) sinal do campo magnético total medido 
                              na Estação SMS da rede EMBRACE em cinza, junto com a 
                              flutuação na faixa de Pc5 em preto. b) Espectro de potência 
                              wavelet do sinal filtrado. c) Média da potência espectral nas 
                              faixas de 2 a 10 minutos (ondas ULF).""",
                              'leg_en': """a) signal of the total magnetic field 
                              measured in the EMBRACE network in gray, together with
                               the fluctuation in the range of Pc5 in black. b)
                                Wavelet power spectrum of the filtered signal. c) 
                                Average spectral power in the ranges from 2 to 10
                                 minutes (ULF waves).""", 
                              'crop': [260,1650,200,2900]},
                  "FigGOES": {'page': -3,
                              'leg_pt': """a) sinal do campo magnético total medido pelo 
                              satélite GOES 16, junto com a flutuação na faixa de Pc5 
                              em preto. b) Espectro de potência wavelet do sinal 
                              filtrado. c) Média da potência espectral nas faixas 
                              de 2 a 10 minutos (ondas ULF).""",
                              'leg_en': """a) signal of the total magnetic field 
                              measured by the GOES 16 satellite, together with the 
                              fluctuation in the range of Pc5 in black. b) Wavelet 
                              power spectrum of the filtered signal. c) Average 
                              spectral power in the ranges from 2 to 10 minutes 
                              (ULF waves).""", 
                              'crop': [260,1650,200,2900]},
                  }
    includeFigure = """\\begin{figure}[H]\n    
                        \\centering\n   
                             \\includegraphics[width=14cm]{./%s}\n
                             \\caption{%s}
                        \\end{figure}\n
                     """
    keys = list(imagesDict.keys())
    textpt = '\section{Ondas ULF} \n \subsection{Responsável: José Paulo Marchezi} \n \n'
    texten = '\section{ULF Waves} \n \subsection{Responsible: José Paulo Marchezi} \n \n' 

    for i in range(len(keys)):
        crops = imagesDict[keys[i]]['crop']
        outfigpath = saveFigs(pages, imagesDict[keys[i]]['page'], 
                             f"{outputimage}", f'figureULF_{i}', 
                             crops)
        
        textpt += includeFigure % ('/'.join(outfigpath.split('/')[2:]), imagesDict[keys[i]]['leg_pt'])
        texten += includeFigure % ('/'.join(outfigpath.split('/')[2:]), imagesDict[keys[i]]['leg_en'])

    textpt += ttextPt
    texten += ttextEn

    return textpt, texten

#%%

PATH = '/home/jose/python_projects/automatedPdfReading/data/'

filename = 'EmbracePresentation_ULF_20220502.pdf'

#%%
texten, textpt = extractFiguresTextULF(PATH, filename, outputimage='./latexText/figures/')
generateLaTexFile(textpt, EnPt=True, outputPath='./latexText', date='2022/04/25')

# img = cv2.imdecode(np.frombuffer(img_page, np.uint8),3) 
# imgCropped = img[crop[0]:crop[1],crop[2]:crop[3]]


# cv2.imwrite(f'{outputpath}/{figname}.png',imgCropped)
# %%
