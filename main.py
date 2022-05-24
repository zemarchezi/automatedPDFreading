#%%
import argparse
import glob
import json
from pathlib import Path
from automatedBriefingReport.extractAllFiles import *

#%%

parser = argparse.ArgumentParser(description='Program to compile the report for the EMBRACE Briefing.')

parser.add_argument('--dirConfig', action='store', dest='dirConfig',
                           default='config.json', required=False,
                           help='O diretório do arquivo .json de configuração.')
parser.add_argument('--year', action='store', dest='year',
                           default='', required=True,
                           help='Ano no qual o Briefing ocorreu.')

parser.add_argument('--month', action='store', dest='month',
                           default='', required=True,
                           help='Mes no qual o Briefing ocorreu.')

parser.add_argument('--day', action='store', dest='day',
                           default='', required=True,
                           help='Dia no qual o Briefing ocorreu.')


arguments = parser.parse_args()


with open(f'{arguments.dirConfig}', 'r') as f:
    configFile = json.load(f)

#%%

PATH = configFile['dataPath']

files = glob.glob(f"{PATH}*")

#%%

dictPaths = separatePathsAreas(files)
dictPaths = dict(sorted(dictPaths.items()))

latexFilesPath = configFile["latexPath"]


outputimage = configFile["outputimagePath"]

Path(outputimage).mkdir(parents=True, exist_ok=True)

dictResponsible = configFile["dictResponsible"]

#%%
eF = extractFiles(dictPaths=dictPaths, dictResponsible=dictResponsible, 
                  outputimage=outputimage, latex=True)
#%%

eF.extractData()


#%%
if configFile['generateLatex']:
    eF.constructLatex(outputPath=latexFilesPath, 
                      year=f"{arguments.year}", 
                      month=f"{arguments.month}", 
                      day=f"{arguments.day}")

if configFile['compileLatex']:
    eF.compileLatexFile()
if configFile['deleteTempFile']:
    eF.deleteTempFiles(filesReports=files)

