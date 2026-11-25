# Validation approach

| Check | Expected behaviour |
|---|---|
| Work-block aggregation | Count the summary once, not summary plus detail |
| Missing duration | Derive only if valid start and end times exist |
| Missing evidence | Flag as unresolved; do not silently impute zero |
| Entity integrity | Flag inconsistent assignments; preserve source evidence |
| Actual vs planned | Exclude planned events from actual KPI |

The synthetic example illustrates the first three rules and planned-event exclusion. Entity integrity is documented as an audit concern. Synthetic sample: 40 minutes summary + two component rows, 20 minutes derived from recorded times, one unknown-duration event and one planned event. Expected total: 60 minutes; one unresolved duration. No claim is made about production performance based on this example.
