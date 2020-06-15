import logging
import json

import azure.functions as func


def main(event: func.EventHubEvent, fromeventhub: func.Out[func.Document]) -> str:
    try:
        logging.info('Function triggered to process a message: %s', event.get_body(), 
        '\n  EnqueuedTimeUtc =', event.enqueued_time,
        '\n  SequenceNumber =', event.sequence_number,
        '\n  Offset =', event.offset)
    except Exception as e:
        print(e)
        pass

    event_body = event.get_body()

    fromeventhub.set(func.Document.from_json(event_body))


