from datetime import time
from decimal import Decimal

from sqlalchemy import DECIMAL
from sqlmodel import Field, SQLModel


class Base(SQLModel):
    group_id: str = Field(primary_key=True, sa_column_kwargs={"name": "groupId"})


class NonstandardWorkType(Base, table=True):
    __tablename__ = "nonstandardWorkTypes"

    nonstandard_work_type_code: str = Field(
        primary_key=True, sa_column_kwargs={"name": "nonstandardWorkTypeCode"}
    )


class RoutineWork(Base, table=True):
    __tablename__ = "routineWorks"

    nonstandard_work_code: str = Field(
        primary_key=True, sa_column_kwargs={"name": "nonstandardWorkCode"}
    )
    is_night_shift: int = Field(sa_column_kwargs={"name": "isNightShift"})
    is_next_day: int = Field(sa_column_kwargs={"name": "isNextDay"})
    start_time: time = Field(sa_column_kwargs={"name": "startTime"})
    working_time: Decimal = Field(
        sa_type=DECIMAL(4, 0), sa_column_kwargs={"name": "workingTime"}
    )


class ProcessType(Base, table=True):
    __tablename__ = "processTypes"

    r_number: str = Field(primary_key=True, sa_column_kwargs={"name": "rNumber"})
