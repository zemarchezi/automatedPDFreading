def generateLaTexFile(texto, EnPt, outputPath, date):
    
    if EnPt:
        title = 'Briefing Space Weather'
        outFile = 'reportSpaceWeather_En'
    else:
        title = 'Briefing Clima Espacial'
        outFile = 'reportSpaceWeather_Pt'

    textTemplate = '''\\documentclass[a4paper, 10pt]{article}
\\usepackage[a4paper,margin=1in,bottom=2.5cm,top=2.5cm, headheight=26pt]{geometry}
\\geometry{a4paper}
\\usepackage{graphicx}
\\usepackage{amssymb}
\\usepackage[utf8]{inputenc}
\\usepackage[brazil]{babel}
\\usepackage{color}
\\usepackage{float}
\\usepackage{hyperref}
\\usepackage{fancyhdr}
\\usepackage{indentfirst}

\\pagestyle{fancy}

\\lhead{\\includegraphics[width=10cm]{embracetopimage.png}}

\\title{\\Large{\\textbf{%s}}}
\\date{%s}

\\begin{document}
\\maketitle \n\n  \\thispagestyle{fancy} ''' %(title, date)

    outtext = f"{textTemplate}{texto}\n\n" + "\\end{document}"

    with open(f'{outputPath}/{outFile}.tex', 'w')  as fls:
        fls.write(outtext)

    return f'{outputPath}/{outFile}.tex'