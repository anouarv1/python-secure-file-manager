Secure File Manager Project
This is a secure file manager project using Python and Azure. The project allows users to upload, download, and delete files from a storage account in Azure Blob Storage. The app is built using the Flask web framework and uses the Azure Storage Python SDK to interact with the storage account.

Features
The secure file manager project includes the following features:

User authentication using Microsoft Azure Active Directory
User authorization using role-based access control (RBAC)
Secure file uploads and downloads using SAS tokens
Encrypted storage using client-side encryption
File management operations, including create, read, update, and delete (CRUD)
Responsive design using Bootstrap
Setup
To set up the secure file manager project, follow these steps:

Clone the repository from GitHub: git clone https://github.com/anouarv1/python-secure-file-manager.git

Install the required dependencies: pip install -r requirements.txt

Configure your Azure storage account settings in the app.py file. This includes setting the connection string and access keys for your storage account, as well as the container name and SAS token expiry time.

Set up user authentication and authorization in Azure Active Directory. This includes creating a new Azure AD app and assigning roles to users or groups.

Run the app using flask run. The app should be accessible at http://localhost:5000.

Usage
To use the secure file manager project, follow these steps:

Log in to the app using your Azure AD credentials. Depending on your role, you may be able to upload, download, and delete files.

Navigate to the file manager page to view and manage files in your storage account.

To upload a file, click the "Upload" button and select the file you want to upload. You can also specify a custom file name and set encryption options.

To download a file, click the file name in the file list. The file will be downloaded using a SAS token with a limited expiry time.

To delete a file, click the "Delete" button next to the file name. You will be prompted to confirm the deletion.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contributions
Contributions to the project are welcome! Please open a pull request on GitHub to submit changes or bug fixes.
