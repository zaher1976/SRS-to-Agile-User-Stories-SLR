#!/usr/bin/env python3
"""Recheck only bibliographic arithmetic and public-file provenance (stdlib)."""
import csv
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
def rows(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

counts=rows('identification_counts.csv')
ledger=rows('bibliographic_candidates_181.csv')
status=rows('scopus_abstract_provenance_93.csv')
linked=rows('source_linked_scopus_76.csv')
assert len(ledger)==181
assert len({r['Index'] for r in ledger})==181
assert Counter(r['Source group'] for r in ledger)=={'Scopus':93,'IEEE Xplore':7,'ScienceDirect citation list':81}
assert len(status)==93
assert len(linked)==76
source_status=Counter(r['Recovery status'] for r in status)
assert source_status=={
  'Full abstract from user-provided export':26,
  'Verified-source précis (not verbatim abstract)':50,
  'Not an individual research article':9,
  'Abstract not verified':8
}, source_status
lookup={r['Stage']:int(r['Count']) for r in counts}
assert lookup['Imported records total']==207
assert lookup['Matched cross-source duplicates']==26
assert lookup['Distinct bibliographic candidates']==181
assert 207-26==181
assert {r['SCOP ID'] for r in linked} <= {r['SCOP ID'] for r in status}
print('PASS: 181 distinct candidate records, 207 entries, 26 duplicates, 93 source-status records, 76 source-linked records.')
print('Source provenance:',dict(source_status))
print('This check does not certify study eligibility, independent reviewer decisions or publisher text rights.')
