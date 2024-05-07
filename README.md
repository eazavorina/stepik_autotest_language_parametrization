# The task: an automated test that can be run using different languages and browsers
https://stepik.org/lesson/237240/step/10?unit=209628

## Run with different languages
```bash
pytest --language=es test_items.py
pytest --language=fr test_items.py
```


## Run for different browsers
```bash
pytest --browser_name=chrome --language=es test_items.py
pytest --browser_name=firefox --language=es test_items.py
```
