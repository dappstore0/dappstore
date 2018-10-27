import dappstore.settings as settings

match = {
    settings.CONTRACT_WSS.events.Sign: Restaurant.new,
    settings.CONTRACT_WSS.events.StageUpdate: Restaurant.update,
}


def loop_items(conn, block, min_block, max_block, first_loop):
    for event, func in match.items():
        # Get all events starting from last block
        data = event.createFilter(fromBlock=block, toBlock=max_block)
        for entry in data.get_all_entries():
            # Call corresponding function
            func(conn, entry["blockNumber"], **entry["args"])

            print("Event: {}".format(event))

            # If first time looping through dict
            if first_loop:
                # The first entry defines the max block, so all events go in sync
                if max_block is None:
                    max_block = entry["blockNumber"]
                elif entry["blockNumber"] > max_block:
                    max_block = entry["blockNumber"]

            # Define the latest block that gets found, this will be the fromBlock next loop
            if entry["blockNumber"] > min_block:
                min_block = entry["blockNumber"]

        first_loop = False

    return min_block, max_block, first_loop


def loop():
    # get block from database
    conn = database.Conn()
    db_block = conn.session.query(database.BlockState).first()
    block = db_block.value
    firstTime = True

    while True:
        first_loop = True
        # Max block is to make every loop go in sync
        max_block = None
        min_block = -2147483647

        # Loop over every event
        min_block, max_block, first_loop = loop_items(conn, block, min_block, max_block, first_loop)

        # commit transaction queries
        # Update database min_block
        if min_block != -2147483647:
            # Search from the block +=1
            block = db_block.value = min_block+1
            #db_block.value = min_block+1

        conn.commit()
        if firstTime:
            print("Loop working")
            firstTime = False
        time.sleep(4)