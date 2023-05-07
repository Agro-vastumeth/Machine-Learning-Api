from enum import Enum
from pydantic import BaseModel, Field

# class which describes elementalAnalysis value
class chno(BaseModel):
    C: float
    H: float
    N: float
    O: float
    Ash: float


class MainModel(BaseModel):
    """
    This is the description of the main model
    """

    CHNO: chno = Field(...)
    

    class Config:
        title = 'Main'

# print(MainModel.schema_json(indent=2))