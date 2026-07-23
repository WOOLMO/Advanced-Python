import asyncio

# First Of All Lets Introduce Tasks, Await and Async. lets start coding! 


# If You Are Familiar With Asyncio, The exercise is to orchestrate multiple coroutines to run concurrently using asyncio, the answer is below. if you are not familiar with asyncio, then please read the below explanation.


# Here Is A Classic Example ! 

async def fetching(): # this function is a coroutine function which is defined by async keyword. and its a simulation of fetching data from a database or an api.
    print("Start fetching...")
    await asyncio.sleep(2)
    print("Done fetching!")
    return {'data': 1}

# this is a counter function. its a coroutine object too 
async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)
        
        
        
async def main():
    task1 = asyncio.create_task(fetching())
    task2 = asyncio.create_task(print_numbers())
    value = await task1
    print(value)
    await task2
    
    
def main1():
    asyncio.run(main())
main1()
    