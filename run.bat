pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser edge

rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser edge
rem pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser edge