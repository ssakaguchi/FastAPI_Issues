from datetime import time
from decimal import Decimal

from sqlalchemy import DECIMAL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    group_id: Mapped[str] = mapped_column("groupId", primary_key=True)


class NonstandardWorkType(Base):
    __tablename__ = "nonstandardWorkTypes"

    nonstandard_work_type_code: Mapped[str] = mapped_column(
        "nonstandardWorkTypeCode", primary_key=True
    )


class RoutineWork(Base):
    __tablename__ = "routineWorks"

    nonstandard_work_code: Mapped[str] = mapped_column(
        "nonstandardWorkCode", primary_key=True
    )
    is_night_shift: Mapped[int] = mapped_column("isNightShift")
    is_next_day: Mapped[int] = mapped_column("isNextDay")
    start_time: Mapped[time] = mapped_column("startTime")
    working_time: Mapped[Decimal] = mapped_column("workingTime", DECIMAL(4, 0))


class ProcessType(Base):
    __tablename__ = "processTypes"

    r_number: Mapped[str] = mapped_column("rNumber", primary_key=True)
