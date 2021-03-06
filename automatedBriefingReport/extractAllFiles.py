#%%
from automatedBriefingReport.functions import *
from automatedBriefingReport.readFiles import *
from automatedBriefingReport.generateLatexFile import *
from automatedBriefingReport.generateMarkdownFile import *
from latexText.compileDocument import *
from logger import *

#%%

class extractFiles():
    def __init__(self, dictPaths, dictResponsible, outputimage, latex):
        self.dictPaths = dictPaths
        self.dictResponsible = dictResponsible
        self.outputimage = outputimage
        self.latexFile = latex

    def extractData(self):
        logger.warning("Extracting Data...")
        self.latexTextEn = ''
        self.latexTextPt = ''
        for area in self.dictPaths.keys():
            if len(self.dictPaths[area].keys()) < 2:
                try:
                    filename = self.dictPaths[area]['path'].split('/')[-1]
                    dirpath = '/'.join(self.dictPaths[area]['path'].split('/')[0:-1])+'/'
                    logger.info(filename)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"--- Error, there is no files in data.")
            if area == '01Sun':
                logger.info(area)
                try:
                    texten, textpt = extractFiguresTextSun_0(docPath=dirpath, 
                                                            filename=filename, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} --- Error")
            if area == '02Sun':
                logger.info(area)
                try:
                    texten, textpt = extractFiguresTextSun_1(docPath=dirpath, 
                                                            filename=filename, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} --- Error")
            if area == '03MeioInterp':
                logger.info(area)
                try:
                    texten, textpt = constructLatexFileInterpMedium(docPath=dirpath, 
                                                            filename=filename, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} --- Error")
            if area == '04RadBelt':
                logger.info(area)
                try:
                    filenamept = self.dictPaths[area]['pathPt'].split('/')[-1]
                    dirpathpt = '/'.join(self.dictPaths[area]['pathPt'].split('/')[0:-1])+'/'
                    filenameen = self.dictPaths[area]['pathEn'].split('/')[-1]
                    dirpathen = '/'.join(self.dictPaths[area]['pathEn'].split('/')[0:-1])+'/'
                    textpt = constructLatexFileRadBelts(docPath=dirpathpt, 
                                                            filename=filenamept, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area])
                    texten = constructLatexFileRadBelts(docPath=dirpathen, 
                                                            filename=filenameen, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} --- Error")
            if area == '05ULF':
                logger.info(area)
                try:
                    texten, textpt = extractFiguresTextULF(docPath=dirpath, 
                                                            filename=filename, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} -- Error")
            if area == '06EMIC':
                logger.info(area)
                try:
                    texten, textpt = extractFiguresTextEMIC(docPath=dirpath, 
                                                            filename=filename, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} --- Error")
            if area == '07Geomag':
                logger.info(area)
                try:
                    texten, textpt = constructLatexFileGeomag(docPath=dirpath, 
                                                            filename=filename, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} --- Error")
            if area == '08Ionosfera':
                logger.info(area)
                try:
                    texten, textpt = constructLatexFileIonosphere(docPath=dirpath, 
                                                            filename=filename, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} --- Error")
            if area == '09Scintilation':
                logger.info(area)
                try:
                    texten, textpt = extractFiguresTextScint(docPath=dirpath, 
                                                            filename=filename, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} --- Error")
            if area == '10Imager':
                logger.info(area)
                try:
                    texten, textpt = extractFiguresTextImager(docPath=dirpath, 
                                                            filename=filename, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} --- Error")
            if area == '11ROTI':
                logger.info(area)
                try:
                    texten, textpt = constructLatexFileRoti(docPath=dirpath, 
                                                            filename=filename, 
                                                            outputFigure=self.outputimage, 
                                                            responsible=self.dictResponsible[area],
                                                            latex=self.latexFile)
                except (Exception) as e:
                    logger.error(e)
                    textpt = ''
                    texten = ''
                    logger.error(f"{area} --- Error")
            self.latexTextEn += texten
            self.latexTextPt += textpt
        logger.warning("Done extractin!")

    def constructLatex(self, outputPath, year, month, day):
        logger.warning("Constructing LaTex File")
        self.outhpathlatex_En = generateLaTexFile(self.latexTextEn, 
                                                  EnPt=True, 
                                                  outputPath=outputPath, 
                                                  date=f"{year}/{month}/{day}")
        self.outhpathlatex_Pt = generateLaTexFile(self.latexTextPt, 
                                                  EnPt=False, 
                                                  outputPath=outputPath, 
                                                  date=f"{day}/{month}/{year}")
        logger.warning("Done Latex!")

    def constructMarkdown(self, outputPath, year, month, day):
        logger.warning("Constructing LaTex File")
        self.outhpathlatex_En = generateMarkdownFile(self.latexTextEn, 
                                                  EnPt=True, 
                                                  outputPath=outputPath, 
                                                  date=f"{year}/{month}/{day}")
        self.outhpathlatex_Pt = generateMarkdownFile(self.latexTextPt, 
                                                  EnPt=False, 
                                                  outputPath=outputPath, 
                                                  date=f"{day}/{month}/{year}")
        logger.warning("Done Latex!")


    def compileMarkdownFile(self):
        logger.warning('Compiling markdown')
        compileMarkdown(self.outhpathlatex_Pt, openFile=False)
        compileMarkdown(self.outhpathlatex_En, openFile=False)
        logger.warning("Pdf File is ready!")

    def compileLatexFile(self):
        logger.warning('Compiling Latex')
        compileLatex(self.outhpathlatex_Pt, openFile=False)
        compileLatex(self.outhpathlatex_En, openFile=False)
        logger.warning("Pdf File is ready!")

    def deleteTempFiles(self, filesReports):
        logger.warning("Deleting Files")
        files_fig = glob.glob(f"{'/'.join(self.outhpathlatex_Pt.split('/')[:-1])}/figures/*", recursive=True)

        for f in files_fig:
            try:
                os.remove(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))

        if filesReports:
            for f in filesReports:
                try:
                    os.remove(f)
                except OSError as e:
                    print("Error: %s : %s" % (f, e.strerror))