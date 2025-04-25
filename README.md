


INSTALLATION :

1 - PULL image from Git

2 - Navigate to app_streamlit

3 - Build docker image [ docker build -t <NAME_IMAGE> . ]

4 - Prepare run with CREDENTIALS for AZURE (-e LANGUAGE_ENDPOINT="..." -e LANGUAGE_KEY="...")

5 - Prepare run  MAP a VOLUME for File Persistence (-v <path_on_host>:<path_in_container>)

6 - Prepare run with PORT mapping for accessibility (-p <host_port>:<container_port>)

7 - Start container [ docker run -d -e <> -e <> -p<> -v <> <NAME_IMAGE>]



to instanciate docker : 

docker run -d -e LANGUAGE_KEY="<key_azure_language ressource>" -e LANGUAGE_ENDPOINT="<endpoint>" -p 8501:8501 -v "<local_volume>":<volume_in_container>