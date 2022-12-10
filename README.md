# Nexus-Upload-Application

#This application was made to simplify the upload process to the Nexus REST API.

Clone this project and run the executable to start. You can also use the NxUp.py script to do the same thing.

This app uploads files to a Nexus directory within a repo programmatically

by running this curl command with the inputs submitted in this form:

 

'curl -v -k -X POST "{}"

               -H "accept: application/json"

               -H "Content-Type: multipart/form-data"

               -H "Authorization: Basic {}"

               -F "raw.directory={}"

               -F raw.asset1=@{}

               -F "raw.asset1.filename={}"

 

In order to get your authorization key, login to Nexus

 

1. Click your username in the top right corner.

2. Click User Token. Click "Access user token".

3. Copy the bottom "user:password" token.

#It is a WIP and definitely needs tuning.
