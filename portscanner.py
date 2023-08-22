import asyncio

async def scan_port(target, port):
    try:
        reader, writer = await asyncio.open_connection(target, port)
        print(f"Port {port} is open")
        writer.close()
    except:
        pass

async def main():
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    tasks = []
    for port in range(start_port, end_port + 1):
        task = asyncio.create_task(scan_port(target, port))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
