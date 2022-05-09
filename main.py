#%%
import glob
from automatedBriefingReport.functions import separatePathsAreas
from automatedBriefingReport.readFiles import *
from automatedBriefingReport.generateLatexFile import *
# from generateLatexFile import *

#%%

PATH = './data/'

files = glob.glob(f"{PATH}*")

#%%

dictPaths = separatePathsAreas(files)

#%%
latexTextEn = ''
latexTextPt = ''
outputimage='./latexText/figures/'
for area in dictPaths.keys():
    filename = dictPaths[area].split('/')[-1]
    dirpath = '/'.join(dictPaths[area].split('/')[0:-1]+'/')
    if area == 'Sun0':
        texten, textpt = extractFiguresTextSun_0(docPath=dirpath, 
                                                 filename=filename, 
                                                 outputimage=outputimage, 
                                                 responsible='José Cecatto')
    
        
#%%
texten, textpt = extractFiguresTextSun_1(PATH, filename, outputimage='./latexText/figures/', responible="José Cecatto")
generateLaTexFile(texten, EnPt=True, outputPath='./latexText', date='2022/04/25')

#%%

doc = fitz.open(files[0])
# %%
