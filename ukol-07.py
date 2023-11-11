"""Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:
- platná data:

2.2.2022
13. 8. 1999
4/5/2001"""

"""
\d?\.\d?\.\d{4}
\d\d\.\s\d\.\s\d{4}
\d\S\d\S\d{4}
"""

import re
regularni_vyraz = re.compile(r"\d?\.\d?\.\d{4}", "\d\d\.\s\d\.\s\d{4}", "\d\S\d\S\d{4}")

"""- neplatná data:

5.123.458.91
21.4
8./9"""

"""Zkopíruj si obsah souboru posta.txt do regex101 jako testovací řetězec.
Vymysli regulární výraz, který označí všechny "poslední řádky adresy" v textu.
Poslední řádka adresy zpravidla obsahuje PSČ a název obce, například 190 16 PRAHA 916 nebo 742 45 FULNEK. Celkem by jich mělo být 18."""

"""\d{3}\s\d{2}\s\d?.(?:[A-Z]+\s\d+|[A-Z\sÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+)$"""

import re
regularni_vyraz = re.compile(r"\d{3}\s\d{2}\s\d?.(?:[A-Z]+\s\d+|[A-Z\sÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ]+)$")