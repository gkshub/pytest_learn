# pytest_learn


1. Create the Environment
> ```bash
> python3.14 -m venv my_env
> ```

2. Activate the Environment
> ```bash
> source my_env/bin/activate
> ```

3. Use and Deactivate
> ```bash
> python main.py
> pip install packages
> deactivate
> ```


###

pytest 
    -v => verbose => detailed output
    -m => marker experssion

```
 pytest -v -m smoke
 pytest -v -m "not sanity"
 pytest -v -m "sanity or stringtest"
 pytest -v -m "sanity and stringtest"

```
    -k => keyword
    --tb=no  => trace back = NO 

```
pytest -v -k "module" --tb=no 
pytest -v -k "06 or 05" --tb=no
```
