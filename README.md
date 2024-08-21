to istall dependencies:

$: pip install -r requirements.txt

to run tests without allure reports

$: pytest -v -s

to run tests with allure reports

$: pytest -v -s --alluredir results

to see the generated reports:
NEED TO INSTALL ALLURE LOCALLY https://allurereport.org/docs/install/

after install you could run via the command line 
$: allure serve results
