import csv, sys

HEADER = ["eia_id","hifld_name","utility_name","hifld_state","rto","ownership_type",
"res_habit","res_habit_src","res_dispatch","res_dispatch_src","ci_habit","ci_habit_src",
"ci_dispatch","ci_dispatch_src","notes","last_verified","confidence"]

PATH = "/sessions/wizardly-vibrant-davinci/mnt/utility-map/data/raw/presence_scan/scan_E.csv"

def init_file():
    with open(PATH, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)

def append_rows(rows):
    with open(PATH, "a", newline="") as f:
        w = csv.writer(f)
        for r in rows:
            assert len(r) == 17, f"Row has {len(r)} fields, expected 17: {r}"
            w.writerow(r)

if __name__ == "__main__":
    init_file()
    print("initialized with header")
