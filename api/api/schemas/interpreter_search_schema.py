from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

from api.schemas.interpreter_schema import InterpreterBase
from api.schemas.location_schema import CourtDistanceSchema, LocationSchema, LocationShortSchema



class DatesSchema(BaseModel):
    arrivalTime: Optional[str]
    date: Optional[datetime]
    period: Optional[str]


class CrcDateRangeSchema(BaseModel):
    endDate: Optional[str]
    startDate: Optional[str]

class BaseInterpreterSearchSchema(BaseModel):    
    languageId:  Optional[int]
    level: Optional[List[str]]
    city: Optional[str]
    dates: Optional[List[DatesSchema]]
    name: Optional[str]
    keywords: Optional[str]
    active: Optional[bool]
    criminalRecordCheck: Optional[CrcDateRangeSchema]
    courtAddr: Optional[str]
    distanceLimit: Optional[bool]
    location: Optional[LocationSchema]

class InterpreterSearchRequestSchema(BaseInterpreterSearchSchema):    
    limit: Optional[int]
    page: Optional[int]
    # sort: Optional[str]


class BookingDateSearchSlimSchema(BaseModel):
    date: Optional[datetime]
    start_time: Optional[str] = Field(alias="startTime")
    finish_time: Optional[str] = Field(alias="finishTime")
    method_of_appearance: Optional[str] = Field(alias="methodOfAppearance")
    status: Optional[str]

    class Config():
        orm_mode = True
        allow_population_by_field_name = True


class BookingSearchSlimSchema(BaseModel):
    location_id: Optional[int] = Field(alias="locationId")
    location: Optional[LocationShortSchema]
    dates: Optional[List[BookingDateSearchSlimSchema]] = []

    class Config():
        orm_mode = True
        allow_population_by_field_name = True



class InterpreterSearchResponseSchema(InterpreterBase):    
    id: int     
    events: Optional[List] = []
    booking: Optional[List[BookingSearchSlimSchema]] = []
    created_at: Optional[datetime]
    court: Optional[CourtDistanceSchema]
    court_distance: Optional[int] = Field(alias="courtDistance")    


class InterpreterDataInExcelRequestSchema(BaseInterpreterSearchSchema):
    pass

