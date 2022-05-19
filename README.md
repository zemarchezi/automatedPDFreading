# Basic documentation for automatedPDFreading


## Requirements


Python 3.8+

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
    "dataPath": "./data/", # 
    "latexPath": "./latexText",
    "outputimagePath": "./latexText/figures/",
    "dictResponsible": {"01Sun": "José Cecatto",
                        "02Sun": "Douglas Silva",
                        "03MeioInterp": "Paulo Jauer",
                        "04RadBelt": "Ligia Alves da Silva",
                        "05ULF": "José Paulo Marchezi",
                        "06EMIC": "Claudia Medeiros",
                        "07Geomag": "Livia Riveiro Alves",
                        "08Ionosfera": "Laysa Resende",
                        "09Scintilation": "Siomel Savio Odriozola",
                        "10Imager": "LUME",
                        "11ROTI": "Name"},
    "generateLatex": true,
    "compileLatex": true,
    "deleteTempFile": false
}
   
```

***

```python
import json
from pysatdata.loaders.load import *

trange=['2021-05-26', '2021-05-30']

varss_rept = load_sat(trange=trange, satellite='rbsp',
                     probe=['a'], level='2', rel='rel03',
                     instrument='rept',datatype='sectors',
                     config_file='./pysatdata/resources/config_file.json', downloadonly=False,
                     usePandas=False, usePyTplot=True)
```
