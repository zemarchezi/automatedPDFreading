#%%
import glob
from automatedBriefingReport.functions import separatePathsAreas
from automatedBriefingReport.readFiles import *
from automatedBriefingReport.generateLatexFile import *
from latexText.compileDocument import *
# from generateLatexFile import *

#%%

PATH = './data/'

files = glob.glob(f"{PATH}*")

#%%

dictPaths = separatePathsAreas(files)
dictPaths = dict(sorted(dictPaths.items()))
#%%
latexTextEn = ''
latexTextPt = ''
outputimage='./latexText/figures/'

# keys = list(dictPaths.keys())
# #%%
# area = keys[0]
# filename = dictPaths[area]['path'].split('/')[-1]
# dirpath = '/'.join(dictPaths[area]['path'].split('/')[0:-1])+'/'
# # #%%
# # # #%%

# texten, textpt = extractFiguresTextSun_0(docPath=dirpath, 
#                                                  filename=filename, 
#                                                  outputFigure=outputimage, 
#                                                  responsible='Douglas Silva')

#%%
for area in dictPaths.keys():
    if len(dictPaths[area].keys()) < 2:
        filename = dictPaths[area]['path'].split('/')[-1]
        dirpath = '/'.join(dictPaths[area]['path'].split('/')[0:-1])+'/'
    if area == '01Sun':
        print(area)
        print(filename)
        try:
            texten, textpt = extractFiguresTextSun_0(docPath=dirpath, 
                                                    filename=filename, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
        except (Exception) as e:
            print(e)
            textpt = ''
            texten = ''
            print(f"{area} {filenamept} --- Error")
    if area == '02Sun':
        print(area)
        print(filename)
        texten, textpt = extractFiguresTextSun_1(docPath=dirpath, 
                                                 filename=filename, 
                                                 outputFigure=outputimage, 
                                                 responsible='Nome')
    
    if area == '03MeioInterp':
        print(area)
        print(filename)
        try:
            texten, textpt = constructLatexFileInterpMedium(docPath=dirpath, 
                                                    filename=filename, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
        except (Exception) as e:
            print(e)
            textpt = ''
            texten = ''
            print(f"{area} {filenamept} --- Error")
    if area == '04RadBelt':
        print(area)
        try:
            filenamept = dictPaths[area]['pathPt'].split('/')[-1]
            dirpathpt = '/'.join(dictPaths[area]['pathPt'].split('/')[0:-1])+'/'
            filenameen = dictPaths[area]['pathEn'].split('/')[-1]
            dirpathen = '/'.join(dictPaths[area]['pathEn'].split('/')[0:-1])+'/'
            textpt = constructLatexFileRadBelts(docPath=dirpathpt, 
                                                    filename=filenamept, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
            texten = constructLatexFileRadBelts(docPath=dirpathpt, 
                                                    filename=filenameen, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
        except (Exception) as e:
            print(e)
            textpt = ''
            texten = ''
            print(f"{area} {filenamept} --- Error")
    if area == '05ULF':
        print(area)
        print(filename)
        try:
            texten, textpt = extractFiguresTextULF(docPath=dirpath, 
                                                    filename=filename, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
        except (Exception) as e:
            print(e)
            textpt = ''
            texten = ''
            print(f"{area} {filenamept} --- Error")
    if area == '06EMIC':
        print(area)
        print(filename)
        try:
            texten, textpt = extractFiguresTextEMIC(docPath=dirpath, 
                                                    filename=filename, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
        except (Exception) as e:
            print(e)
            textpt = ''
            texten = ''
            print(f"{area} {filenamept} --- Error")
    if area == '07Geomag':
        print(area)
        print(filename)
        try:
            texten, textpt = constructLatexFileGeomag(docPath=dirpath, 
                                                    filename=filename, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
        except (Exception) as e:
            print(e)
            textpt = ''
            texten = ''
            print(f"{area} {filenamept} --- Error")
    if area == '08Ionosfera':
        print(area)
        print(filename)
        try:
            texten, textpt = constructLatexFileIonosphere(docPath=dirpath, 
                                                    filename=filename, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
        except (Exception) as e:
            print(e)
            textpt = ''
            texten = ''
            print(f"{area} {filenamept} --- Error")
    if area == '09Scintilation':
        print(area)
        print(filename)
        try:
            texten, textpt = extractFiguresTextScint(docPath=dirpath, 
                                                    filename=filename, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
        except (Exception) as e:
            print(e)
            textpt = ''
            texten = ''
            print(f"{area} {filenamept} --- Error")
    if area == '10Imager':
        print(area)
        print(filename)
        try:
            texten, textpt = extractFiguresTextImager(docPath=dirpath, 
                                                    filename=filename, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
        except (Exception) as e:
            print(e)
            textpt = ''
            texten = ''
            print(f"{area} {filenamept} --- Error")
    if area == '11ROTI':
        print(area)
        print(filename)
        try:
            texten, textpt = constructLatexFileRoti(docPath=dirpath, 
                                                    filename=filename, 
                                                    outputFigure=outputimage, 
                                                    responsible='Nome')
        except (Exception) as e:
            print(e)
            textpt = ''
            texten = ''
            print(f"{area} {filenamept} --- Error")
    latexTextEn += texten
    latexTextPt += textpt
#%%
outhpathlatex_En = generateLaTexFile(latexTextEn, EnPt=True, outputPath='./latexText', date='2022/05/09')
outhpathlatex_Pt = generateLaTexFile(latexTextPt, EnPt=False, outputPath='./latexText', date='09/05/2022')
#%%
compileLatex(outhpathlatex_Pt, openFile=False)
compileLatex(outhpathlatex_En, openFile=False)

#%%
files_fig = glob.glob(f"{'/'.join(outhpathlatex_Pt.split('/')[:-1])}/figures/*", recursive=True)

for f in files_fig:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))

# for f in files:
#     try:
#         os.remove(f)
#     except OSError as e:
#         print("Error: %s : %s" % (f, e.strerror))
# # os.system(outhpathlatex)
# %%
