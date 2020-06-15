import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
import json

# Load and set credentials
with open('../local.settings.json') as json_file:
    credentials = json.load(json_file)["Values"]

conn_str=credentials['AzureEventHubsWriteConnectionString']
eventhub_name=credentials['AzureEventHubsName']

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
 	    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str=conn_str, eventhub_name=eventhub_name)
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData(json.dumps({"First event":"an event", "value":10})))
        event_data_batch.add(EventData(json.dumps({"Second Event":"another event", "value": 20})))
        event_data_batch.add(EventData(json.dumps({"Third Event": 100, "value": 30})))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())