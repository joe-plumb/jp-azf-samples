import logging

import azure.functions as func


def main(hourdocin: func.DocumentList, hourdocout: func.Out[func.Document]) -> str:
    # Set DocumentList to update second collection with
    returnDocs = func.DocumentList() 
    
    # Loop around documents in incoming DocumentList, and update a value
    for doc in hourdocin:
        logging.info(f"Document: {doc.to_json()}")
        newDoc = func.Document.from_json(doc.to_json())
        newDoc["value"] = newDoc["value"] + 10
        logging.info("newDoc: %s", newDoc.to_json())
        returnDocs.append(newDoc)

    hourdocout.set(returnDocs)