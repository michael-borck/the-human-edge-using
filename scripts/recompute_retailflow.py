#!/usr/bin/env python3
"""Recompute every RetailFlow figure quoted in Chapter 6 from the CSV.

Run from the book root: python3 scripts/recompute_retailflow.py
Exits nonzero if any quoted figure disagrees with the data.
"""
import collections
import csv
import pathlib
import statistics
import sys

CSV = pathlib.Path(__file__).resolve().parent.parent / "resources" / "retailflow-customer-service-data.csv"
rows = list(csv.DictReader(CSV.open()))


def mean(values):
    return statistics.mean(values)


def by(key, value):
    groups = collections.defaultdict(list)
    for r in rows:
        groups[r[key]].append(float(r[value]))
    return {k: mean(v) for k, v in groups.items()}


checks = []


def check(label, got, want, tol=0.05):
    ok = abs(got - want) <= tol
    checks.append(ok)
    print(f"{'OK ' if ok else 'FAIL'} {label}: got {got:.2f}, book says {want}")


resp = [float(r["response_time_hours"]) for r in rows]
check("tickets", len(rows), 260, tol=0)
check("agents", len({r['agent'] for r in rows}), 8, tol=0)
check("overall response hours", mean(resp), 9.2, tol=0.05)
chan = by("channel", "response_time_hours")
for name, want in [("Live Chat", 4.0), ("Phone", 6.1), ("Social Media", 9.4), ("Email", 13.2)]:
    check(f"response {name}", chan[name], want)
day = by("day_of_week", "response_time_hours")
check("response Sunday (slowest)", day["Sunday"], 13.7)
check("response Thursday (fastest)", day["Thursday"], 7.4)
month = by("month", "response_time_hours")
check("response December", month["December"], 13.6)
check("response November", month["November"], 7.2)
fast = [float(r["satisfaction_score"]) for r in rows if float(r["response_time_hours"]) <= 4]
slow = [float(r["satisfaction_score"]) for r in rows if float(r["response_time_hours"]) > 12]
check("satisfaction within 4h", mean(fast), 4.09, tol=0.01)
check("satisfaction over 12h", mean(slow), 1.64, tol=0.01)
check("Email/Live Chat ratio", chan["Email"] / chan["Live Chat"], 3.3)

print(f"date range {min(r['date'] for r in rows)} to {max(r['date'] for r in rows)} (book: 3 July to 29 December 2024)")
sys.exit(0 if all(checks) else 1)
