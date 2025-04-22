from fastapi import APIRouter
from fastapi.responses import FileResponse
import os, json, zipfile

router = APIRouter()

def generate_export():
    export_dir = "project_exports"
    os.makedirs(export_dir, exist_ok=True)
    with open(f"{export_dir}/agents.json", "w") as f:
        json.dump([], f)
    with open(f"{export_dir}/feedback.json", "w") as f:
        json.dump([], f)
    zip_path = "export.zip"
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for filename in os.listdir(export_dir):
            zipf.write(os.path.join(export_dir, filename), arcname=filename)
    return zip_path

@router.get("/download")
def export():
    return FileResponse(generate_export(), filename="export.zip")
