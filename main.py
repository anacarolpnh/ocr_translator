from fastapi import FastAPI
from Routes.routes_tranlation import router as translation_router
import uvicorn

app = FastAPI()

app.include_router(translation_router)

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
