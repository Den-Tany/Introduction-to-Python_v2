Write-Host "Start test...":
python -m pytest --alluredir allure-result

Write-Host "Generating a report...":
allure serve allure-result