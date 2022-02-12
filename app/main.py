from fastapi import FastAPI, Depends
from .schemas import RequestParams, DataOut
from .util import gcContent, reverseComplement
import httpx


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/api/sequence", response_model=DataOut)
async def getData(params: RequestParams = Depends()):
    # NOTE: When using GET request use '&' as delimiter instead of ';'
    # TODO: Implement recognition of '&' as ';'
    url = f"https://api.genome.ucsc.edu/getData/sequence?genome={params.genome};chrom={params.chrom};start={params.start};end={params.end}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()

    dna = data.get('dna')

    # Perform calculations using util functions
    data["gc_content"] = gcContent(dna)
    data["reverse"] = reverseComplement(dna)

    # print(data)

    return data
