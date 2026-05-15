from fastapi import BackgroundTasks, FastAPI

from core.cmd import process

app = FastAPI()


@app.get("/scan")
async def scan(domain: str, email: str, bgt: BackgroundTasks):
    bgt.add_task(process, domain, email)

    return {"msg": f"scan run in {domain}"}
