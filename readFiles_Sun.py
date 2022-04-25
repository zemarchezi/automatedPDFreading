#%%
import re
import fitz
from generateLatexFile import *

#%%

def extractFiguresTextSun_0(docPath, filename):
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
    ttextPt = ttextPt.strip().replace('%', '\%').replace('\n', "\\\ ")
    textpt = '\section{Sol} \n \subsection{Responsável: José Cecatto}\n\n' +ttextPt
    texten = '\section{Sun} \n \subsection{Responsible: José Cecatto}\n\n' +ttextEn

    # textpt = '\section{Sol} \n \subsection{Responsável: José Cecatto}\n\n\\begin{itemize}\n'
    # texten = '\section{Sun} \n \subsection{Responsible: José Cecatto}\n\n\\begin{itemize}\n'
    # for i in ttextPt.split('\n'):
    #     if len(i) > 2:
    #         textpt += "\\item "
    #         textpt += i + '\n'
    # textpt += '\\end{itemize}\n'
    # for i in ttextEn.split('\n'):
    #     if len(i) > 2:
    #         texten += "\\item "
    #         texten += i + '\n'
    # texten += '\\end{itemize}\n'

    return texten, textpt


#%%

PATH = '/home/jose/python_projects/automatedPDFreading/data/'

filename = 'Brief06Dez21_Summ_Cecatto.pdf'


#%%
texten, textpt = extractFiguresTextSun_0(PATH, filename)
generateLaTexFile(texten, EnPt=True, outputPath='./latexText', date='2022/04/25')

#%%