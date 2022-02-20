import asyncpg

CONNECTION = "postgres://postgres:postgres@localhost:5432/postgres"


async def main():
    timescale_pool = CONNECTION
    connection_pool = await asyncpg.create_pool(dsn=timescale_pool)
    print("Created connection pool")
    try:
        async with connection_pool.acquire() as connection:
            result = await connection.execute(
                "SELECT MAX(period) FROM replication_data WHERE systemid = '2M200107XS' AND target = 'PCLPRM1';")
            print(result)
            print("Test query worked I suppose")
    except Exception as ex:
        raise Exception("Failed to fetch dear query")


if __name__ == '__main__':
    await main()
