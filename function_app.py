import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="incoming/{name}",
                  connection="AzureWebJobsStorage")
@app.blob_output(arg_name="outputblob", path="processed/{name}-summary.txt",
                 connection="AzureWebJobsStorage")
def blob_trigger(myblob: func.InputStream, outputblob: func.Out[str]):
    logging.info(f"Python blob trigger function processed blob "
                 f"Name: {myblob.name} "
                 f"Blob Size: {myblob.length} bytes")
    outputblob.set(f"Processed {myblob.name}, size {myblob.length} bytes")


# This example uses SDK types to directly access the underlying BlobClient object provided by the Blob storage trigger.
# To use, uncomment the section below and add azurefunctions-extensions-bindings-blob to your requirements.txt file
# Ref: aka.ms/functions-sdk-blob-python
#
# import azurefunctions.extensions.bindings.blob as blob
# @app.blob_trigger(arg_name="client", path="mycontainer",
#                   connection="AzureWebJobsStorage")
# def blob_trigger(client: blob.BlobClient):
#     logging.info(
#         f"Python blob trigger function processed blob \n"
#         f"Properties: {client.get_blob_properties()}\n"
#         f"Blob content head: {client.download_blob().read(size=1)}"
#    
