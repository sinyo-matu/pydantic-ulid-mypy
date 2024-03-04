## disciption

`pydantic-extra-types.ulid.ULID` forces user codebase to use `pydantic-extra-types.ulid.ULID` instead of `ulid.ULID` when using mypy.

## 1. install dependencies

```bash
make install
```

## 2. run mypy

```bash
make mypy
```

expected output:

```bash
tests/test_application.py:10: error: Argument 1 to "code_use_something_id" has incompatible type "pydantic_extra_types.ulid.ULID"; expected "ulid.ULID"  [arg-type]
```
