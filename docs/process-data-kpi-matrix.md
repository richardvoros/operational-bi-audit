# Folyamat–adat–KPI kapcsolati mátrix

A korábbi portfóliócsomag fogalmi mátrixának rövidített változata. A mutatók részben javasoltak; a táblázat nem igazolja megvalósításukat.

| Alrendszer és folyamat | Bemenő adat | Ellenőrzési szabály | Javasolt KPI | Döntés |
|---|---|---|---|---|
| Termelés – tervezés | Cél, időszak, állomány | Terv/tény elkülönítése | Cél–tény eltérés | Prioritások |
| Termelés – tavaszi fejlesztés | Család, állapot, dátum | Érvényes azonosító | Erősségmegoszlás | Fejlesztési feladatok |
| Termelés – mézeltetés, pergetés | Termelési esemény, tömeg | Mértékegység, pozitív tömeg | Termés/család | Termelés értékelése |
| Egészségügy – védekezés | Kezelés, dózis, dátum | Egység, duplikáció, tény/terv | Kezelési lefedettség | Célzott ellenőrzés |
| Egészségügy – megfigyelés | Mért érték, időablak | Mérés és becslés külön | Mért trend | Kockázatkezelés |
| Logisztika – kaptár és telephely | Kaptár-, család-, telephelyazonosító | Egyediség, hozzárendelés | Nyilvántartási eltérések | Egyeztetés |
| Logisztika – munka, utazás | Munkaidő, helyszín, típus | Hiányzó és átfedő idők | Munkaidő/telephely | Kapacitástervezés |
| Logisztika – készlet | Anyag, készletmozgás | Negatív készlet, egység | Készleteltérés | Beszerzés |
| Értékesítés – kiszerelés | Tétel, darabszám, tömeg | Tételkövetés, átváltás | Kiszerelési teljesítmény | Kapacitás |
| Értékesítés – eladás | Mennyiség, ár, csatorna | Visszáru elkülönítése | Értékesített kg | Árképzés |
| BI – riport | Törzsadat, napló, cél | Teljesség, konzisztencia | KPI-egyezőség | Döntés-előkészítés |
| BI – audit | Teszteset, eltérés | Bizonyíték, verzió | Nyitott eltérések | Javítási prioritások |

A KPI-khoz rögzítendő: számláló, nevező, időablak, szűrők és hiányzó értékek kezelése. A ténylegesen ellenőrzött eredmények külön dokumentumban szerepelnek: [Audit eredményei](audit-results.md).
