<h1 align="center">nz-ua</h1>
<p align="center">Library for working with the nz.ua service</p>

## Requirements
Python 3.10+
* [Aiohttp](https://github.com/aio-libs/aiohttp) for making requests to nz.ua api.
* [Pydantic](https://github.com/pydantic/pydantic) for data validation.
## Installation
```console
pip install nz-ua
```
Or use the version from github:
```console
pip install git+https://github.com/GoldMasterPro/nz-ua
```
## Quick usage
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
See the [documentation](https://GoldMasterPro.github.io/nz-ua) for more examples.