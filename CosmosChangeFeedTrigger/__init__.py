import logging

import azure.functions as func


def main(documentsin: func.DocumentList, documentsout: func.Out[func.Document]) -> str:
    # Set DocumentList to update second collection with
    returnDocs = func.DocumentList() 
    
    # Loop around documents in incoming DocumentList
    for doc in documentsin:
        logging.info(f"Document: {doc.to_json()}")
        newDoc = func.Document.from_json(doc.to_json())
        logging.info("newDoc: %s", newDoc)
        returnDocs.append(newDoc)

    documentsout.set(returnDocs)