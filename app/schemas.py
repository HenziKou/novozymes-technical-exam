from typing import Optional
from pydantic import BaseModel, Field


# genome - The genome to query against. Optional, should default to human(hg38)
# chrom - The chromosome of interest
# start - The location on the chromosome where the returned sequence should start
# end - The location of the chromosome wheret the returned sequence should end

class RequestParams(BaseModel):
    genome: Optional[str] = "hg38"
    chrom: str
    start: int
    end: int


class DataOut(BaseModel):
    gc_content: float = Field(alias="GC Content")
    dna: str = Field(alias="DNA Sequence")
    reverse: str = Field(alias="Reverse Complement")

    class Config:
        allow_population_by_field_name = True
