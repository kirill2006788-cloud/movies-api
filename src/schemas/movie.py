from pydantic import BaseModel, ConfigDict, Field


class MovieCreate(BaseModel):
    title: str = Field(min_length=1)
    genre: str = Field(min_length=1)
    rating: float = Field(ge=0, le=10)
    year: int = Field(ge=1888)


class MovieRead(MovieCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
