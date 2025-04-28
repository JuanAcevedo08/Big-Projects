import asyncio
import random
import time

async def process_transaction(name: str, amount: int):
    print("Processing purchase...")
    time.sleep(1)
    print(f"Accessing account of {name} ...")
    time.sleep(2)
    print(f"Amount to pay {amount}")
    await asyncio.sleep(random.randint(1, 3))
    print("Transaction completed successfully")

