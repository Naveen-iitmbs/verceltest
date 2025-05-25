from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks from marks.json into a dictionary
with open("marks.json") as f:
    data = json.load(f)
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    return {"marks": [marks_dict.get(n, None) for n in name]}
