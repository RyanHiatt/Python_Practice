import asyncio

async def find_divisibles(inrange, div_by):
    print("Finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 5000000 == 0:
            await asyncio.sleep(0.00001)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located

async def main():
    divs1 = loop.create_task(find_divisibles(508000, 34113))
    divs2 = loop.create_task(find_divisibles(100052, 9876))
    divs3 = loop.create_task(find_divisibles(5000, 333))
    await asyncio.wait([divs1, divs2, divs3])
    return divs1, divs2, divs3

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(1)
        d1, d2, d3 = loop.run_until_complete(main())
        for row in d1.result(), d2.result(), d3.result():
            print(row)
    except Exception as e:
        pass
    finally:
        loop.close()