from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Read marks from CSV into a dictionary
marks_dict = {}
with open("marks.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 2:
            name, mark = row[0].strip(), int(row[1].strip())
            marks_dict[name] = mark

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    return {"marks": [marks_dict.get(n, None) for n in name]}
