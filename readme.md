# Scraping Register of Disqualification Gov UK

Scraping script for scraping Register of Disqualification data from A-Z on www.gov.uk including Name, Date of Birth, and Post Town data.

This project created using Scrapy Python Web Scraping frameworks.

### How to Run

* Install the requirements
    ```^terminal
    pip install -r requirements.txt
    ```

* Run
    ```^terminal
    scrapy crawl govuk -o output.json
    ```

    Addtional command such as `-o` for outputing the resutlts while [output.json](output.json) is the output filename for the results. You also can use .CSV extension to output a csv file beside of json file.