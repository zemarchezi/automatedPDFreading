#%%
import re
import fitz
from matplotlib import image
from generateLatexFile import *
from pdf2image import convert_from_path
#%%

#%%
def extractFiguresTextScint(docPath, filename, outputimage):
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

        ttextEn = re.split('\n\s+',doc[pageEn].get_text())[-2]
        ttextPt = re.split('\n\s+', doc[pagePt].get_text())[-2]
    
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

    textpt = '\section{Cintilação} \n \subsection{Responsável: Siomel Savio Odriozola}\n\n' +ttextPt + '\n'
    texten = '\section{SCintilation} \n \subsection{Responsible: Siomel Savio Odriozola}\n\n' +ttextEn +'\n'

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

PATH = './data/'

filename = 'Resumo(06_12-12_2021)_S4_Siomel.pdf'

#%%
texten, textpt = extractFiguresTextScint(PATH, filename, outputimage='./latexText/figures/')
generateLaTexFile(textpt, EnPt=True, outputPath='./latexText', date='2022/04/25')

#%%
