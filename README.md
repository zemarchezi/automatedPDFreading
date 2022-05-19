# Basic documentation for automatedPDFreading


## Requirements

Python 3.8+

1. Clone or download the automatePDFreading
2. From the automatePDFreading directory: 

```python
   pip install -r requirements.txt
```

***
## config.json

If some change in downloding directories is needed, it can be done in this file.

```automatedPDFreading/config.json```

This file sets the directory where the individual reports are stored (default: ./data/); and also the directore fot the LaTex compilation and figures.

You can change the area responsible if needed as well.

The parameters in the file are:

```json
   {
    "dataPath": "directory where the individual reports are stored (default: ./data/)"
    "latexPath": "directory are the LaTex files (default: ./latexText)",
    "outputimagePath": "directory are the LaTex figures (default: ./latexText/figures/)",
    "dictResponsible": {"01Sun": "Name",
                        "02Sun": "Name",
                        "03MeioInterp": "Name",
                        "04RadBelt": "Name",
                        "05ULF": "Name",
                        "06EMIC": "Name",
                        "07Geomag": "Name",
                        "08Ionosfera": "Name",
                        "09Scintilation": "Name",
                        "10Imager": "Name",
                        "11ROTI": "Name"},
    "generateLatex": true (Set false if you don't want the program generate the LaTex file),
    "compileLatex": true (Set false if you don't want the program compile the LaTex),
    "deleteTempFile": false (Set true if you don't want to delete the ./data/ and ./latexText/figures/ content)
}
   
```

***
# Usage

1st Edit the "config.json" and set all folders and responsible names.

2nd Run

```python
   python main.py --dirConfig "config.json" --year "YYYY" --month "MM" --day "DD"
```
```bash
   --dirConfig DIRCONFIG O diretório do arquivo .json de configuração.
  --year YEAR           Ano no qual o Briefing ocorreu.
  --month MONTH         Mes no qual o Briefing ocorreu.
  --day DAY             Dia no qual o Briefing ocorreu.
```
