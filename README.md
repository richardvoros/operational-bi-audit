# Operatív BI-rendszer és adatminőségi audit

**Folyamatelemzés · Rendszerszervezés · Adatminőség · BI · Folyamatfejlesztés**

[English version](README.en.md) · [Rendszerterv](docs/system-design.md) · [Magyar dokumentáció](docs/hu.md)

## Üzleti probléma
Egy Excel-alapú méhészeti nyilvántartás és böngészőben futó BI-rendszer megbízhatóságának vizsgálata. A cél, hogy az operatív eseményekből ellenőrizhető mutatók és döntési információk készüljenek.

## Rendszertervi ábrák

![A méztermelési rendszer fő folyamatai és alrendszerei](meheszeti-rendszer-abrai.webp)

**Bal oldalon:** éves működési ciklus és támogató folyamatok.

**Jobb oldalon:** funkcionális alrendszerek, kapcsolataik és a BI szerepe.

## A rendszer működése
```mermaid
flowchart TD
 A[Operatív események és törzsadatok] --> B[Excel nyilvántartás]
 B --> C[Adatelőkészítés és ellenőrzés]
 C --> D[BI és KPI riportok]
 C --> E[Eltérésjegyzék]
 E --> B
 D --> F[Vezetői döntések]
```

A fogalmi ábra az információ útját mutatja, nem a tényleges dashboard képernyőképe.

## Audit és megállapítások
- Hiányzó időtartamok: csak igazolható kezdés és befejezés alapján történő pótlás.
- Kettős időelszámolás: összesítő munkablokkok és részletek elkülönítése.
- Ellentmondó azonosítók: forrásadatok megőrzése, bizonytalanság jelölése.
- Tényadatok és tervek elkülönítése, KPI-számítási szabályok ellenőrzése.

A vizsgálat nem igazolja a teljes rendszer hibamentességét. A végleges auditszámok ellenőrzése még szükséges.

## Mintaadatok és validáció

[CSV mintaadatok](sample-data/worklog.csv)

| Sor | Blokk | Típus | Státusz | Kezdés | Befejezés | Perc |
|---|---|---|---|---|---|---:|
| 1 | A | Összesítő | Tény | 08:00 | 08:40 | 40 |
| 2 | A | Részlet | Tény | 08:00 | 08:15 | 15 |
| 3 | A | Részlet | Tény | 08:15 | 08:40 | 25 |
| 4 | B | Önálló | Tény | 09:00 | 09:20 | — |
| 5 | C | Önálló | Tény | — | — | — |
| 6 | D | Önálló | Terv | 10:00 | 10:30 | 30 |

Elvárt eredmény: 60 perc tényleges munkaidő és egy tisztázatlan időtartam. A részletek nem számítanak kétszer, a tervezett esemény kimarad. A példa mesterséges adatokat használ.

A példa az Excel-alapú ellenőrzési logikát szemlélteti, nem önálló alkalmazás.

## Szakmai kompetenciák
Folyamatfeltárás, rendszermodellezés, üzleti szabályok, adatminőség, BI-validáció, döntéstámogatás. Technológia: Excel, HTML/JavaScript.

A csomag nem tartalmaz eredeti üzemi adatállományt vagy munkáltatói adatokat.

## English summary
A portfolio case study of operational BI and data quality auditing, covering process mapping, business rules, work-time reconciliation and exception handling. [Full English version](README.en.md).
