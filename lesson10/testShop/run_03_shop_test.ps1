Write-Host "Start test...":
python -m pytest --alluredir allure-results

Write-Host "Generating a report...":
allure serve allure-results