#%%
import re
import fitz
from matplotlib import image
from generateLatexFile import *
from pdf2image import convert_from_path
#%%

def extractItemize(text):
    dictTex = {}
    for nn, i in enumerate(text.split('\n')[1:]):
        i = re.sub('[\¸\˜\´]+', '', i)

        if i.startswith("WSA") or i.startswith("EMC") or i.startswith("CME"):
            dictTex[i] = []
            ns = i
        else:
            dictTex[ns].append(i) 
    dics = {}
    for kk in dictTex.keys():
        tts = dictTex[kk]
        tts = ' '.join(tts).split('●')
        tts = [i for i in tts if len(i)>0]
        dics[kk] = tts

    texs = """\\begin{itemize} \n """

    for i in dics.keys():
        texs += '\\item ' + i +'\n'
        if len(dics[i]) > 0:
            for j in dics[i]:
                texs += """\\begin{itemize} \n """ + '\\item' + j + '\n'
        
            texs += """\\end{itemize} \n """
    
    texs += """\\end{itemize} \n """

    return texs

def extractFiguresTextSun_0(docPath, filename, outputimage):

    
    with fitz.open(docPath + filename) as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    regexPt = r"(?<=Summary)(.|\n)*(?=Resumo)"
    regexEn = r"(?<=Resumo)(.|\n)*(?=END)"

    matches = re.search(regexPt, text, re.MULTILINE)
    if matches:
        ttextPt = matches.group()
    else:
        ttextPt = ''
    matches = re.search(regexEn, text, re.MULTILINE)
    if matches:
        ttextEn = matches.group()
    else:
        ttextEn = ''

    ttextEn = ttextEn.strip().replace('%', '\%').replace('\n', "\\\ ")
    ttextEn = ttextEn.replace('<', '$<$').replace('>', '$>$').replace('~', '$\sim$')
    ttextPt = ttextPt.strip().replace('%', '\%').replace('\n', "\\\ ")
    ttextPt = ttextPt.replace('<', '$<$').replace('>', '$>$').replace('~', '$\sim$')
    textpt = '\section{Sol} \n \subsection{Responsável: José Cecatto}\n\n' +ttextPt
    texten = '\section{Sun} \n \subsection{Responsible: José Cecatto}\n\n' +ttextEn


    return texten, textpt

#%%
def extractFiguresTextSun_1(docPath, filename, outputimage):
    regexPt = r"(?i)resumo"
    regexEn = r"(?i)summary"
    
    with fitz.open(docPath + filename) as doc:
        for page in range(len(doc)):
            text = doc[page].get_text()
            textsplit = text.split("\n")
            matchespt = re.search(regexPt, text, re.MULTILINE)
            matchesen = re.search(regexEn, text, re.MULTILINE)
            if matchespt:
                pagePt = page
            elif matchesen:
                pageEn = page

        ttextEn = doc[pageEn].get_text()
        ttextPt = doc[pagePt].get_text()
    
        imagesPages = {'en':list(range(pagePt+1,pageEn)), 'pt':list(range(pageEn+1,len(doc)))}

    pages = convert_from_path(docPath + filename, 500)
    pathEn = []
    pathPt = []
    for im in imagesPages.keys():
        langPage = imagesPages[im]
        for p in range(len(langPage)):
            outimagePath = f"{outputimage}{im}_outfile_{p}.jpg"
            if im == 'en':
                pathEn.append(outimagePath)
            else:
                pathPt.append(outimagePath)
            pages[langPage[p]].save(outimagePath, 'JPEG')
            # pageim = doc.loadPage(langPage[p])  # number of page
            # pix = pageim.get_pixmap()
            # output = f"{im}_outfile_{p}.png"
            # pix.save(output)

    textpt = '\section{Sol} \n \subsection{Responsável: Douglas Silva}\n\n' +extractItemize(ttextPt) + '\n'
    texten = '\section{Sun} \n \subsection{Responsible: Douglas Silva}\n\n' +extractItemize(ttextEn) +'\n'

    print(pathEn)
    
    figures = """
    \\begin{figure}[H]
        \\centering
        \\includegraphics[width=14cm]{./%s}
    \\end{figure} \n \n
    """
    for s in range(len(pathEn)):
        ouIm = '/'.join(pathEn[s].split('/')[2:])
        texten += figures % (ouIm)

    for s in range(len(pathPt)):
        ouIm = '/'.join(pathPt[s].split('/')[2:])
        textpt += figures % (ouIm)

    return texten, textpt

#%%

PATH = '/home/jose/python_projects/automatedPdfReading/data/'

filename = 'briefing_25_april_02_may_Douglas.pdf'

#%%
texten, textpt = extractFiguresTextSun_1(PATH, filename, outputimage='./latexText/figures/')
generateLaTexFile(texten, EnPt=True, outputPath='./latexText', date='2022/04/25')

#%%
