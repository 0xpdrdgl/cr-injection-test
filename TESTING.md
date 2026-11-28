# Testing and runtime validation

The repository does not use a heavyweight test runner in review sandboxes.

For a minimal interpreter sanity check, mirror CI module resolution exactly:

```bash
PYTHONPATH=. python -c "import sys; print(sys.version.split()[0])"
```

The full local suite, when needed outside the review sandbox, is:

```bash
python -m unittest discover -s tests -v
```
