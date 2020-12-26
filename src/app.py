from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.api import router as api_router
from src.booking_service import BookingServiceError

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")


@app.exception_handler(BookingServiceError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        jsonable_encoder({"info": "booking service error", "error": exc}),
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
    )
