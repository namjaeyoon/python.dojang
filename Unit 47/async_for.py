import asyncio

class AsyncCounter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.stop:
            await asyncio.sleep(1.0)
            r = self.current
            self.current += 1
            return r
        else:
            raise StopAsyncIteration

async def main():
    async for i in AsyncCounter(3):    # for 앞에 async를 붙임
        print(i, end=' ')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
