from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload_logs")
async def upload_logs(file: UploadFile = File(...)):
    content = await file.read()

    # dummy analysis response
    return {
        "message": f"File {file.filename} received",
        "events": [
            {
                "time": "10:01",
                "title": "Suspicious Login",
                "desc": "Multiple failed login attempts",
                "status": "fail"
            }
        ],
        "root_cause": "Weak password policy",
        "impact": "Unauthorized access",
        "prevention": ["Enable MFA", "Strong passwords"]
    }
