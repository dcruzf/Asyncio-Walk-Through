import asyncio, time
import pdb


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


# You need a loop instance before you can run any coroutines
loop = asyncio.get_event_loop()

# We say that create_task() schedules your coroutine to be run on the loop
task = loop.create_task(main())

# This call will block the current thread, which will usually be the main thread.
# Note that run_until_complete() will keep the loop running only until the given
# coro completes—but all other tasks scheduled on the loop will also run while the
# loop is running. Internally, asyncio.run() calls run_until_complete() for you
# and therefore blocks the main thread in the same way.
loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
