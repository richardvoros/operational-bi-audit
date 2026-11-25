import csv
from pathlib import Path
from datetime import datetime

path = Path(__file__).resolve().parents[1] / 'sample-data' / 'worklog.csv'
with path.open(newline='', encoding='utf-8') as f:
    rows = [r for r in csv.DictReader(f) if r['status'] == 'actual']
summary_blocks = {r['block'] for r in rows if r['kind'] == 'summary'}
total = 0
exceptions = []
for r in rows:
    if r['kind'] == 'detail' and r['block'] in summary_blocks:
        continue
    try:
        if r['minutes']:
            minutes = int(r['minutes'])
        else:
            start, end = (datetime.strptime(r[k], '%H:%M') for k in ('start', 'end'))
            minutes = int((end - start).total_seconds() / 60)
        if minutes < 0:
            raise ValueError('negative duration')
    except ValueError:
        exceptions.append(r['id'])
        continue
    total += minutes
assert total == 60, total
assert exceptions == ['5'], exceptions
print(f'PASS: {total} minutes; unresolved records: {exceptions}')
