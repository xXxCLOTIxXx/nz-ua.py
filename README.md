nz-ua
==========

![PyPI](https://img.shields.io/pypi/v/nz-ua?style=for-the-badge)

Library for working with the nz.ua service

Requirements
----------

* Python 3.10+
* [Aiohttp](https://github.com/aio-libs/aiohttp) for making requests to nz.ua api.
* [Pydantic](https://github.com/pydantic/pydantic) for data validation.

Installing
----------

```console
pip install nz-ua
```
Or use the version from github:
```console
pip install git+https://github.com/GoldMasterPro/nz-ua
```

Quick usage
----------

```python
import nz
import asyncio

USER_NAME = "your username"
PASSWORD = "your password"


async def main():
    async with nz.Client() as client:
        await client.login(USER_NAME, PASSWORD)
        schedule = await client.get_schedule()
        print(schedule.dict())


if __name__ == "__main__":
    asyncio.run(main())

```

Links
------

- [Documentation](https://GoldMasterPro.github.io/nz-ua)
- [Pypi](https://test.pypi.org/project/nz-ua/)