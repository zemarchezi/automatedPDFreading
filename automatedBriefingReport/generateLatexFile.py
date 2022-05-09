def generateLaTexFile(texto, EnPt, outputPath, date):
    
    if EnPt:
        title = 'Briefing Space Weather'
    else:
        title = 'Briefing Clima Espacial'

    textTemplate = '''\\documentclass[11pt, oneside]{article}
\\usepackage[bottom=2.5cm,top=2.5cm]{geometry}
\\geometry{a4paper}
\\usepackage{graphicx}
\\usepackage{amssymb}
\\usepackage[utf8]{inputenc}
\\usepackage[brazil]{babel}
\\usepackage{color}
\\usepackage{float}
\\usepackage{hyperref}
\\bibliographystyle{apalike}
\\usepackage{indentfirst}

\\title{%s}
\\date{%s}

\\begin{document}
\\maketitle \n\n ''' %(title, date)

    outtext = f"{textTemplate}{texto}\n\n" + "\end{document}"

    with open(f'{outputPath}/reportSpaceWeather.tex', 'w')  as fls:
        fls.write(outtext)