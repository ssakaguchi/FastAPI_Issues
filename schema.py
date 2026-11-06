from datetime import time

from pydantic import BaseModel, ConfigDict, field_serializer
from pydantic.alias_generators import to_camel


class ResponseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel, populate_by_name=True, from_attributes=True
    )


class NonstandardWorkTypeItem(ResponseModel):
    nonstandard_work_type_code: str


class RoutineWorkItem(ResponseModel):
    nonstandard_work_code: str
    is_night_shift: bool
    is_next_day: bool
    start_time: time
    working_time: int

    @field_serializer("start_time", when_used="json")
    def serialize_start_time(self, value: time) -> str:
        return value.isoformat(timespec="minutes")


class ProcessTypeItem(ResponseModel):
    r_number: str


class NonstandardWorkResponse(ResponseModel):
    nonstandard_work_types: list[NonstandardWorkTypeItem]
    routine_works: list[RoutineWorkItem]
    process_types: list[ProcessTypeItem]
