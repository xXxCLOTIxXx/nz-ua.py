import nz
import asyncio
client = nz.Client()

async def main():
	info = await client.login('user_name', 'password')
	print(info.json)


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(loop.create_task(main()))