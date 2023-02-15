from azure.storage.blob import BlobServiceClient, BlobClient, ContainerSasPermissions, generate_container_sas, BlobSasPermissions, generate_blob_sas
import datetime
import os
from flask import Flask, request, redirect, url_for, render_template, send_file

# Construct the connection string and credentials
connection_string = "DefaultEndpointsProtocol=https;AccountName=sfmsotrageofppt;AccountKey=L1N+WcC896sxUeaxIoQcVIJ1Wyi/VyUkkxIU9NyjwnyguzxAeGg7N8iMbRnOGlza2B4yGnBKtl4P+AStAJ0XMA==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Define the Flask app
app = Flask(SFM)

# Define the route for the home page
@app.route("/")
def home():
    # Get a list of all the files in the container
    container_name = "sfmcontainer"
    container_client = blob_service_client.get_container_client(container_name)
    files = [blob.name for blob in container_client.list_blobs()]

    # Render the home page template and pass in the list of files
    return render_template("home.html", files=files)

# Define the route for uploading a file
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Save the uploaded file to the container
        container_name = "sfmcontainer"
        container_client = blob_service_client.get_container_client(container_name)
        file = request.files["file"]
        blob_client = container_client.get_blob_client(file.filename)
        blob_client.upload_blob(file)

        # Redirect to the home page
        return redirect(url_for("home"))

    # Render the upload page template
    return render_template("upload.html")

# Define the route for downloading a file
@app.route("/download/<filename>")
def download(filename):
    # Generate a SAS token for the file
    container_name = "sfmcontainer"
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(filename)
    blob_sas_permissions = BlobSasPermissions(read=True)
    sas_token = generate_blob_sas(
        account_name="sfmstorageofppt",
        container_name=container_name,
        blob_name=filename,
        account_key="L1N+WcC896sxUeaxIoQcVIJ1Wyi/VyUkkxIU9NyjwnyguzxAeGg7N8iMbRnOGlza2B4yGnBKtl4P+AStAJ0XMA==",
        permission=blob_sas_permissions,
        expiry=datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    )

    # Set the response headers to force the file to download
    headers = {"Content-Disposition": f"attachment; filename={filename}"}

    # Generate the URL for the file and send it as a response
    blob_url = f"https://sfmstorageofppt.blob.core.windows.net/{container_name}/{filename}?{sas_token}"
    return redirect(blob_url)

# Define the route for deleting a file
@app.route("/delete/<filename>")
def delete(filename):
    # Delete the file from the container
    container_name = "sfmcontainer"
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(filename)
    blob_client.delete_blob()

    # Redirect to the home page
    return redirect(url_for("home"))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)