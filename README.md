# Backend Full Stack Technical Exam - Take Home

Coding assessment for Full Stack Engineer position at Novozymes.

## Project Description

See attached _full_stack_take_home_technical_examp.pdf_ file in repository for in-depth description of the project.

## Dependencies, Frameworks, & Libraries

- python3
- FastAPI
- Uvicorn
- httpx
- pip

These are the tools that I chose to use because they are the one that I am most comfortable and most proficient in. Python has been my language of choice due to the years of experience I have built upon it, which is also a factor in some of the frameworks that I used on this project as well. FastAPI/Uvicorn is my api framework of choice because this the technology that I am currently teaching myself through YouTube alongside its compatability with `pip` and Python. It also has my favorite aspect of an integrated [Swagger UI](https://swagger.io/tools/swagger-ui/) and [ReDoc](https://redoc.ly/redoc/) for an easy interative API documentation page.

One additional library that I used for this exam was `httpx`. This Python library allowed me to redirect my `GET` request endpoint to the specific [endpoint](http://api.genome.ucsc.edu/getData/sequence) noted in the guidelines, without following the redirection.

## Install and Run Project

1. Install [python3](https://www.python.org) (version 3.9 or higher)

2. Open a terminal window and install pip dependency

   - **Linux:** `python -m ensurepip --upgrade`
   - **MacOS:** `python -m ensurepip --upgrade`
   - **Windows:** `py -m ensurepip --upgrade`

3. Go to project directory

   ```
   cd novozymes_exam
   ```

4. Within the directory write the command below to enter the virtual environment to run/test the program

   ```
   source venv/bin/activate
   ```

5. Next we will download and install the FastAPI/Uvicorn dependencies

   ```
   pip install "fastapi[all]"
   ```

6. Now to run the program we can type the following

   ```
   uvicorn app.main:app
   ```

   This will run the current state of the program. Any changes mad to the program must be refreshed by exiting the program by pressing `CTRL + C` and entering the same command as above. If you want to make multiple edits to the program and have it refresh instantly upon saving enter the flag `--reload` after the command above,

   ```
   uvicorn app.main:app --reload
   ```

7. On a brower (Safari, Chrome, Firefox, etc) enter the url provided by the terminal window starting with **http**.

   ```
   INFO:   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

8. After copying the url onto your browser search bar, at the end of the url you can add the endpoint `/api/sequence` and query parameters to refine your genome search.

   ```
   http://127.0.0.1:8000/api/sequence?genome=hg38&chrom=chrM&start=3&end=25
   ```

   **NOTE:** The `genome` query parameter is optional and defaulted to `hg38`. The other three parameters are required (without defaults) per the instructions of the exam.

## Example Test Cases

1. Input:

   ```
   http://127.0.0.1:8000/api/sequence?chrom=chrM&start=0&end=20
   ```

   Output:

   ```
   {"GC Content":0.5,"DNA Sequence":"GATCACAGGTCTATCACCCT","Reverse Complement":"AGGGTGATAGACCTGTGATC"}
   ```

2. Input:

   ```
   http://127.0.0.1:8000/api/sequence?genome=mm10&chrom=chrM&start=4321&end=5678
   ```

   Output:

   ```
   {"GC Content":0.3537214443625645,"DNA Sequence":"GCTCCCCTATCAATTTTAATTCAAATTTACCCGCTACTCAACTCTACTATCATTTTAATACTAGCAATTACTTCTATTTTCATAGGGGCATGAGGAGGACTTAACCAAACACAAATACGAAAAATTATAGCCTATTCATCAATTGCCCACATAGGATGAATATTAGCAATTCTTCCTTACAACCCATCCCTCACTCTACTCAACCTCATAATCTATATTATTCTTACAGCCCCTATATTCATAGCACTTATACTAAATAACTCTATAACCATCAACTCAATCTCACTTCTATGAAATAAAACTCCAGCAATACTAACTATAATCTCACTGATATTACTATCCCTAGGAGGCCTTCCACCACTAACAGGATTCTTACCAAAATGAATTATCATCACAGAACTTATAAAAAACAACTGTCTAATTATAGCAACACTCATAGCAATAATAGCTCTACTAAACCTATTCTTTTATACTCGCCTAATTTATTCCACTTCACTAACAATATTTCCAACCAACAATAACTCAAAAATAATAACTCACCAAACAAAAACTAAACCCAACCTAATATTTTCCACCCTAGCTATCATAAGCACAATAACCCTACCCCTAGCCCCCCAACTAATTACCTAGAAGTTTAGGATATACTAGTCCGCGAGCCTTCAAAGCCCTAAGAAAACACACAAGTTTAACTTCTGATAAGGACTGTAAGACTTCATCCTACATCTATTGAATGCAAATCAATTGCTTTAATTAAGCTAAGACCTCAACTAGATTGGCAGGAATTAAACCTACGAAAATTTAGTTAACAGCTAAATACCCTATTACTGGCTTCAATCTACTTCTACCGCCGAAAAAAAAAAATGGCGGTAGAAGTCTTAGTAGAGATTTCTCTACACCTTCGAATTTGCAATTCGACATGAATATCACCTTAAGACCTCTGGTAAAAAGAGGATTTAAACCTCTGTGTTTAGATTTACAGTCTAATGCTTACTCAGCCATTTTACCTATGTTCATTAATCGTTGATTATTCTCAACCAATCACAAAGATATCGGAACCCTCTATCTACTATTCGGAGCCTGAGCGGGAATAGTGGGTACTGCACTAAGTATTTTAATTCGAGCAGAATTAGGTCAACCAGGTGCACTTTTAGGAGATGACCAAATTTACAATGTTATCGTAACTGCCCATGCTTTTGTTATAATTTTCTTCATAGTAATACCAATAATAATTGGAGGCTTTGGAAACTGACTTGTCCCACTAATAATCGGAGCCCCAGATATAGCATTCCCACGAATAAATAATATAAGTTTTTGACTCCTACCACCATCATTTCTCCTTCTCCTAGCATCATCAATA","Reverse Complement":"TATTGATGATGCTAGGAGAAGGAGAAATGATGGTGGTAGGAGTCAAAAACTTATATTATTTATTCGTGGGAATGCTATATCTGGGGCTCCGATTATTAGTGGGACAAGTCAGTTTCCAAAGCCTCCAATTATTATTGGTATTACTATGAAGAAAATTATAACAAAAGCATGGGCAGTTACGATAACATTGTAAATTTGGTCATCTCCTAAAAGTGCACCTGGTTGACCTAATTCTGCTCGAATTAAAATACTTAGTGCAGTACCCACTATTCCCGCTCAGGCTCCGAATAGTAGATAGAGGGTTCCGATATCTTTGTGATTGGTTGAGAATAATCAACGATTAATGAACATAGGTAAAATGGCTGAGTAAGCATTAGACTGTAAATCTAAACACAGAGGTTTAAATCCTCTTTTTACCAGAGGTCTTAAGGTGATATTCATGTCGAATTGCAAATTCGAAGGTGTAGAGAAATCTCTACTAAGACTTCTACCGCCATTTTTTTTTTTCGGCGGTAGAAGTAGATTGAAGCCAGTAATAGGGTATTTAGCTGTTAACTAAATTTTCGTAGGTTTAATTCCTGCCAATCTAGTTGAGGTCTTAGCTTAATTAAAGCAATTGATTTGCATTCAATAGATGTAGGATGAAGTCTTACAGTCCTTATCAGAAGTTAAACTTGTGTGTTTTCTTAGGGCTTTGAAGGCTCGCGGACTAGTATATCCTAAACTTCTAGGTAATTAGTTGGGGGGCTAGGGGTAGGGTTATTGTGCTTATGATAGCTAGGGTGGAAAATATTAGGTTGGGTTTAGTTTTTGTTTGGTGAGTTATTATTTTTGAGTTATTGTTGGTTGGAAATATTGTTAGTGAAGTGGAATAAATTAGGCGAGTATAAAAGAATAGGTTTAGTAGAGCTATTATTGCTATGAGTGTTGCTATAATTAGACAGTTGTTTTTTATAAGTTCTGTGATGATAATTCATTTTGGTAAGAATCCTGTTAGTGGTGGAAGGCCTCCTAGGGATAGTAATATCAGTGAGATTATAGTTAGTATTGCTGGAGTTTTATTTCATAGAAGTGAGATTGAGTTGATGGTTATAGAGTTATTTAGTATAAGTGCTATGAATATAGGGGCTGTAAGAATAATATAGATTATGAGGTTGAGTAGAGTGAGGGATGGGTTGTAAGGAAGAATTGCTAATATTCATCCTATGTGGGCAATTGATGAATAGGCTATAATTTTTCGTATTTGTGTTTGGTTAAGTCCTCCTCATGCCCCTATGAAAATAGAAGTAATTGCTAGTATTAAAATGATAGTAGAGTTGAGTAGCGGGTAAATTTGAATTAAAATTGATAGGGGAGC"}
   ```

3. Input:

   ```
   http://127.0.0.1:8000/api/sequence?chrom=chrM&start=0
   ```

   Output:

   ```
   {"detail":[{"loc":["query","end"],"msg":"field required","type":"value_error.missing"}]}
   ```

## Compromise

One compromise that I have made to this assessment is by using the default query parameter delimiter '&' instead of the semicolon, ';', used in this external api.

## Further Consideration

The description on ambiguous bases was confusing to me. Thus I interpreted the statement as to ignore any nucleotides not ['A', 'C', 'G', 'T'], i.e.

```
sequence = "AGTCNG"
len(sequence) = 5
```

I also want to note that I have limited experience with AWS services and products therefore my answer to the question is limited to what I already know and what I can gather through research on AWS. However I am a quick learner who is independent and proacitve in learning new tools and technologies.
