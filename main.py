#%%
import argparse
import glob
import json
from automatedBriefingReport.extractAllFiles import *

#%%

parser = argparse.ArgumentParser(description='Program to compile the report for the EMBRACE Briefing.')

parser.add_argument('--dirConfig', action='store', dest='dirConfig',
                           default='config.json', required=False,
                           help='O diretório do arquivo .json de configuração.')


arguments = parser.parse_args()


with open(f'{arguments.dirConfig}', 'r') as f:
    configFile = json.load(f)

PATH = configFile['dataPath']

files = glob.glob(f"{PATH}*")

#%%

dictPaths = separatePathsAreas(files)
dictPaths = dict(sorted(dictPaths.items()))

outputimage = configFile["outputimagePath"]

dictResponsible = configFile["dictResponsible"]

#%%
eF = extractFiles(dictPaths=dictPaths, dictResponsible=dictResponsible, 
                  outputimage=outputimage)
#%%

eF.extractData()


if configFile['generateLatex']:
    eF.constructLatex(outputPath="./latexText", year="2022", month="05", day="09")

if configFile['compileLatex']:
    eF.compileLatexFile()
if configFile['deleteTempFile']:
    eF.deleteTempFiles(filesReports=files)



