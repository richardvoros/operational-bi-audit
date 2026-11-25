# Lezárt BI-audit – eredmények és korlátok

**Vizsgálat:** 2026. november 15.  
**Forrás:** a végső V3 auditjegyzőkönyv, a V34 Excel és a V64.1 HTML ellenőrzése.  
**Minősítés:** az audit lezárva, a rendszer feltételesen és korlátozottan validált.

## Ellenőrzött eredmények

| Vizsgálat | Dokumentált eredmény |
|---|---|
| Excel-fájl épsége | Sikeres |
| Munkalapok megőrzése | 9/9 |
| Képletek integritása | 35 eredeti képlet karakterazonosan megmaradt |
| Napló vizsgálati hatóköre | 653 sor, ebből 644 elvégzettként jelölve |
| Kaptár–család megfeleltetés | A nyilvántartáson belül egyezett; a tényleges létszám nem igazolt |
| Munkaidő és állomány KPI | A vizsgált alapmutatók egyeztek a független számítással |
| JavaScript-szintaxis | Sikeres |
| Dashboard DOM- és KPI-próba | Sikeres, teszthelyettesítőkkel |
| Évszűrő és keresés | Sikeres, korlátozott környezetben |
| Rendszerterv fájlépsége | Sikeres, 20 beágyazott ábra jelenléte |

A vizsgálat belső üzemi adatokat is érintett. A portfólió a szakmai ellenőrzési eredményeket közli, az állománylétszámot, telephelyeket és tényleges munkaidőösszeget nem teszi közzé.

## Nyitott eltérések

| Azonosító | Terület | Következő lépés |
|---|---|---|
| A-01 | Nyilvántartási és helyszíni állományeltérés | Igazolt forrásadatok egyeztetése |
| A-02 | Hiányos munkaidőadatok | Az önálló és részletező események elkülönítése |
| A-03 | Lehetséges időátfedések | Tételes értelmezés, automatikus törlés nélkül |
| A-04 | Hiányzó kezdési idő | Csak hiteles forrásból történő pótlás |
| A-05 | Teljes Excel-betöltés és diagramrajzolás | Valódi végponttól végpontig elfogadási teszt |
| A-06 | Becsült és részleges adatokból képzett mutatók | Módszertani és értelmezési korlátok kezelése |

## Következtetés

Az audit lezárása nem egyenlő a rendszer teljes üzemi megfelelőségével. A teszt során a külső SheetJS és Chart.js könyvtárak helyett teszthelyettesítők futottak. A teljes Excel-betöltés és a diagramok tényleges rajzolása még nem igazolt. A hiányzó forrásadatokat nem pótoltuk feltételezésekkel.

A portfólióban bemutatott auditálási kompetencia: forrásintegritás, független KPI-rekalkuláció, hibajegyek dokumentálása, ellenőrizhető javítások és korlátozások egyértelmű közlése.
