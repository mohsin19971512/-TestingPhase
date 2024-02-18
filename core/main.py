import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from core.routers import include_routers

app = FastAPI()

include_routers(app)

register_tortoise(
    app,
    db_url='sqlite://db/db.sqlite3',
    modules={'models': ['models.user', 'models.post']},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
