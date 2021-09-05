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
    
