from repository import NonstandardWorkRepository
from schema import (
    NonstandardWorkResponse,
    NonstandardWorkTypeItem,
    ProcessTypeItem,
    RoutineWorkItem,
)


def load_nonstandard_work(
    group_id: str, repository: NonstandardWorkRepository
) -> NonstandardWorkResponse:
    return NonstandardWorkResponse(
        nonstandard_work_types=[
            NonstandardWorkTypeItem.model_validate(row)
            for row in repository.list_nonstandard_work_types(group_id)
        ],
        routine_works=[
            RoutineWorkItem.model_validate(row)
            for row in repository.list_routine_works(group_id)
        ],
        process_types=[
            ProcessTypeItem.model_validate(row)
            for row in repository.list_process_types(group_id)
        ],
    )
