# Operational BI & Data Quality Audit

**Vörös Richárd | Business Process Analysis · Data Quality · BI · Process Improvement**

[Magyar összefoglaló](docs/hu.md) · [System design](docs/system-design.md) · [Validation approach](docs/validation.md)

## Business challenge
An operational beekeeping system uses an Excel workbook and a browser-based BI dashboard to support planning and daily decisions. Reliable reporting requires consistent master data, traceable operational events and correct aggregation of work time. The audit examines these relationships rather than treating visual presentation as proof of data quality.

## Approach
- Map operational processes, data inputs and decision outputs.
- Separate current master-data status from historical events.
- Reconcile identifiers, missing durations and overlapping work blocks.
- Validate KPI inclusion rules and document unresolved exceptions.

## Findings and corrective actions
The internal audit log documents missing work durations, duplicate time accounting across detail and summary rows, and inconsistent entity assignments. Corrections include deriving duration only from recorded start/end times, counting a parent work block once, and preserving historical records when the correct assignment is uncertain.

This is a scoped portfolio summary, not an assertion that every component of the production system is error-free. Final audit totals are withheld pending verification against the final report.

## Reproducible illustration
The included Python example uses entirely synthetic data and demonstrates work-block reconciliation and exception reporting. It is a separate demonstration, not the original production code.

```bash
python tests/validate.py
```

## Technology
Excel, browser-based HTML/JavaScript reporting, data reconciliation and business rule validation. Python is used for the standalone illustrative test.

## Publication scope
No production workbook, private operational records, exact locations or employer data are included. Internal documents and production dashboard source remain private.
