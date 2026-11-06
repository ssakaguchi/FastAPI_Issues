from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session

from database import engine, get_session, seed_mock_data
from model import Base
from repository import NonstandardWorkRepository
from schema import NonstandardWorkResponse
from service import load_nonstandard_work


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    try:
        Base.metadata.create_all(engine)
        seed_mock_data()
        yield
    finally:
        engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get("/api/nonstandard-work", response_model=NonstandardWorkResponse)
def get_nonstandard_work(
    group_id: Annotated[str, Query(alias="groupId", min_length=1)],
    session: Annotated[Session, Depends(get_session)],
) -> NonstandardWorkResponse:
    return load_nonstandard_work(group_id, NonstandardWorkRepository(session))
