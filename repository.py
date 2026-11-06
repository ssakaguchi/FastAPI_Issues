from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from model import NonstandardWorkType, ProcessType, RoutineWork


class NonstandardWorkRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def list_nonstandard_work_types(self, group_id: str) -> Sequence[NonstandardWorkType]:
        return self.session.scalars(
            select(NonstandardWorkType)
            .where(NonstandardWorkType.group_id == group_id)
            .order_by(NonstandardWorkType.nonstandard_work_type_code)
        ).all()

    def list_routine_works(self, group_id: str) -> Sequence[RoutineWork]:
        return self.session.scalars(
            select(RoutineWork)
            .where(RoutineWork.group_id == group_id)
            .order_by(RoutineWork.nonstandard_work_code)
        ).all()

    def list_process_types(self, group_id: str) -> Sequence[ProcessType]:
        return self.session.scalars(
            select(ProcessType)
            .where(ProcessType.group_id == group_id)
            .order_by(ProcessType.r_number)
        ).all()
