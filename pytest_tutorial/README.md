# How to install pytest
pip install pytest==2.9.1

# How to run

## Run all the filenames
```
py.test
```

## Run all the filenames
```
py.test
```

## Run tests only from a specific file, we can use py.test <filename>

```
py.test test_sample1.py
```

## Run a subset of entire test

### Run tests by substring matching
```
py.test -k method1 -v
-k <expression> is used to represent the substring to match
-v increases the verbosity
```

### Run tests by markers
```
py.test -m <name>
-m <name> mentions the marker name
```

## Running tests in parallel

Install `pytest-xdist` first
```
pip install pytest-xdist
```
You can run tests now by

```
py.test -n 4
```

-n <num> runs the tests by using multiple workers. In the above command, there will be 4 workers to run the test.

