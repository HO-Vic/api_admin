import csv
from pathlib import Path

# 현재 파일의 부모: pipeline 디렉터리 - a
# a의 부모: csmetic_admin - b
ROOT = Path(__file__).resolve().parent.parent

# data 디렉터리는 a의 부모에서 타고 가야한다
DATA_DIR = ROOT / "data"

def read_csv(path):
    """csv를 읽어서 필드(컬럼)과 내용을 반환"""
    with open(path, encoding='utf-8', newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


# 해당 디렉터리의 *.csv 확장자를 읽는다
for path in sorted(DATA_DIR.glob("*.csv")):
    colums, rows = read_csv(path)
    
    print(f"\n{path.name} : {len(rows)} rows, {len(colums)} columns")

