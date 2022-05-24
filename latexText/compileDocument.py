#%%
import os
import platform
import subprocess
import glob
from markdown import markdown
import pdfkit


#%%

def compileLatex(outhpathlatex, openFile):
    filename, ext = os.path.splitext(outhpathlatex)
    pdf_filename = filename + '.pdf'
    subprocess.run(['pdflatex', '-interaction=nonstopmode', 
                    '-aux-directory=./latexText/aux',
                    '-output-directory=./latexText/', 
                    outhpathlatex])

    if openFile:
        if not os.path.exists(pdf_filename):
            raise RuntimeError('PDF output not found')

        # open PDF with platform-specific command
        if platform.system().lower() == 'darwin':
            subprocess.run(['open', pdf_filename])
        elif platform.system().lower() == 'windows':
            os.startfile(pdf_filename)
        elif platform.system().lower() == 'linux':
            subprocess.run(['xdg-open', pdf_filename])
        else:
            raise RuntimeError('Unknown operating system "{}"'.format(platform.system()))
        

def compileMarkdown(outhpathlatex, openFile):
    filename, ext = os.path.splitext(outhpathlatex)
    pdf_filename = filename + '.pdf'
    with open(filename, 'r') as f:
        html_text = markdown(f.read(), output_format='html4')
    
    pdfkit.from_string(html_text, pdf_filename)

    if openFile:
        if not os.path.exists(pdf_filename):
            raise RuntimeError('PDF output not found')

        # open PDF with platform-specific command
        if platform.system().lower() == 'darwin':
            subprocess.run(['open', pdf_filename])
        elif platform.system().lower() == 'windows':
            os.startfile(pdf_filename)
        elif platform.system().lower() == 'linux':
            subprocess.run(['xdg-open', pdf_filename])
        else:
            raise RuntimeError('Unknown operating system "{}"'.format(platform.system()))
        
