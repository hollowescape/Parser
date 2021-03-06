# Parser
## The project consists of two stages :

### Stage 1: Parsing the raw_html and storing it in the CSV file.
### Stage 2: In this Stage, we are cleaning the parsed data stored in the CSV file that we got in stage1.

## Stage1 : 
  1. ### Parsing :
            Step1: It consists the reading the data of the raw JSON file using pandas.
            Step2: Iterating over each row that we got in step1.
            Step3: Then we are using the beautiful soup library with Html parser to parse the raw_Html data and then appending it into the list.
            Step4: The raw_html which does not have the body tag was generating the error so to handle this exception I used the try-catch.
            Step5: Using the CSV library we are storing the parsed data that we got in step3 into a CSV file.

## Stage2 : 
  2. ### Cleaning :
            Step 1: In this step, I am importing the parsed CSV files that were generated in the  stage1
            Step 2: Iterating over each row that we got in step1.
            Step 3: I am using the CSV reader to read the data present in the CSV file row-wise, then we are cleaning the data for which I have created a separate                        function.
            Step 4: In the function, I am removing the linespaces, Unicodes that are present in the data.
            Step 5: After that, I am using the CSV writer to write the cleaned data in the new CSV file.

## Input Format 
![Screenshot from 2021-09-05 16-56-16](https://user-images.githubusercontent.com/46193104/132127630-066942e4-1d85-4d95-a211-604cb5fb4cc4.png)
    
    In the above input format, we have to call the parse.py followed by the name of the file on which the parser should work. Then after execution of the parser.py,     it will make a call on the clean.py file and the parsed data will be sent to the clean.py file.

## Output Format 
![Screenshot from 2021-09-05 16-57-50](https://user-images.githubusercontent.com/46193104/132127889-24632906-f4b2-47ab-aa02-841cabd54348.png)

  
    In the output, we can see the all mails got parsed successfully for this input file.
## File Name Convention 
    The Parsed CSV file will be named filename_parseddata.csv	
    The cleaned CSV file will be named filename_cleandata.csv 


