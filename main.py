from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from exceptions import AppException
from schemas import ErrorResponse
import traceback

app = FastAPI()
