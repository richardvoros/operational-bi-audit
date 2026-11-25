# Adatminőség-ellenőrzési módszertan

[English version](validation.en.md)

| Ellenőrzés | Elvárt működés |
|---|---|
| Munkablokkok összesítése | Az összesítő idő egyszer szerepeljen, a részletekkel ne duplikálódjon |
| Hiányzó időtartam | Csak érvényes kezdési és befejezési időből számítható |
| Hiányzó bizonyíték | Nyitott eltérésként jelölendő, nem helyettesíthető nullával |
| Azonosítók integritása | Ellentmondó hozzárendelések jelzése, eredeti adatok megőrzése |
| Tény és terv | A tervezett események kizárása a tény-KPI-ból |

A mesterséges példa a munkablokkok, a hiányzó időtartamok és a tény/terv elkülönítésének szabályait szemlélteti. Az azonosítók integritása külön auditvizsgálat tárgya.

[CSV-minta](../sample-data/worklog.csv): 40 perc összesítő blokk, két részletsor, 20 perc számítható önálló esemény, egy ismeretlen időtartam és egy tervezett esemény. Elvárt összeg: 60 perc; egy tisztázatlan időtartam. Ez nem tényleges üzemi teljesítményadat.
