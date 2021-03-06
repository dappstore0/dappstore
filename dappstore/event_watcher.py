from web3 import Web3, HTTPProvider, WebsocketProvider
import json
import dappstore.settings as settings
#import os
import time
#os.environ["DJANGO_SETTINGS_MODULE"] = "dappstore.settings"
#import django
#django.setup()
from app.models import State, Dapp


class DappStore:
    @staticmethod
    def sign(app, name, category, homepage, icon, blockchain):
        print(app)
        Dapp(
            address=app,
            name=name,
            category=category,
            homepage=homepage,
            icon=icon,
            status="protoype",
            blockchain=blockchain
        ).save()

    @staticmethod
    def update(app, name, stage):
        dp = Dapp.objects.filter(name__exact=name)[0]

        if dp and dp.address == app:
            dp.status=stage
            dp.save()


match = {
    settings.CONTRACT_WSS.events.Sign: DappStore.sign,
    settings.CONTRACT_WSS.events.StageUpdate: DappStore.update,
}


def loop_items(block, min_block, max_block, first_loop):
    for event, func in match.items():
        # Get all events starting from last block
        data = event.createFilter(fromBlock=block, toBlock=max_block)
        for entry in data.get_all_entries():
            # Call corresponding function
            func(**entry["args"])

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
    db_block = State.objects.get(key="block")

    block = db_block.value
    firstTime = True

    while True:
        first_loop = True
        # Max block is to make every loop go in sync
        max_block = None
        min_block = -2147483647

        # Loop over every event
        min_block, max_block, first_loop = loop_items(block, min_block, max_block, first_loop)

        # commit transaction queries
        # Update database min_block
        if min_block != -2147483647:
            # Search from the block +=1
            block = db_block.value = min_block+1
            db_block.value = block
            db_block.save()
            #db_block.value = min_block+1

        if firstTime:
            print("Loop working")
            firstTime = False
        time.sleep(4)