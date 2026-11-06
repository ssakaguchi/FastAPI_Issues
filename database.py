from collections.abc import Iterator
from datetime import time
from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from model import NonstandardWorkType, ProcessType, RoutineWork


engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)


def seed_mock_data() -> None:
    with Session(engine) as session, session.begin():
        session.add_all([
            NonstandardWorkType(group_id="M22", nonstandard_work_type_code=code)
            for code in ("NW001", "NW002", "NW003")
        ])
        session.add_all([
            RoutineWork(
                group_id="M22",
                nonstandard_work_code=code,
                is_night_shift=is_night_shift,
                is_next_day=is_next_day,
                start_time=start_time,
                working_time=Decimal(working_time),
            )
            for code, is_night_shift, is_next_day, start_time, working_time in (
                ("RW001", 0, 0, time(8), 480),
                ("RW002", 1, 1, time(22), 480),
                ("RW003", 0, 0, time(13), 240),
            )
        ])
        session.add_all([
            ProcessType(group_id="M22", r_number=number)
            for number in ("R001", "R002", "R003")
        ])


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
