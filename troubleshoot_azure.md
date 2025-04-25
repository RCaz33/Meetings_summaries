

docker build -t cw_summary_meetings .   

docker run -d --env-file ../.env -p 8501:8501 cw_summary_meetings  

docker run -e LANGUAGE_KEY="<lauguage_ressource_key>" -e LANGUAGE_ENDPOINT="https://<lauguage_ressource_name>.cognitiveservices.azure.com/" -e KEY_VAULT_NAME="summary-transcript-kv" -e SECRET_NAME="get-your-summary" -p 8501:8501 -d cw_summary_meetings  

az login --use-device-code
az acr login --name app4production   

docker tag cw_summary_meetings app4production.azurecr.io/cw_summary:v1
docker push app4production.azurecr.io/cw_summary:v1 

az container create --resource-group CW-Ressource-Group --name cw-summary-meetings --image app4production.azurecr.io/cw_summary:v1 --assign-identity --environment-variables LANGUAGE_KEY="<lauguage_ressource_key>" LANGUAGE_ENDPOINT="https://<lauguage_ressource_name>.cognitiveservices.azure.com/" KEY_VAULT_NAME="summary-transcript-kv" SECRET_NAME="get-your-summary"   

az container update --resource-group CW-Ressource-Group --name cw-summary-meetings --image app4production.azurecr.io/cw_summary:v1 --assign-identity --environment-variables LANGUAGE_KEY="<lauguage_ressource_key>" LANGUAGE_ENDPOINT="https://<lauguage_ressource_name>.cognitiveservices.azure.com/" KEY_VAULT_NAME="summary-transcript-kv" SECRET_NAME="get-your-summary" --ports 80 --ip-adress public  


use AIM to give the container access to the keyvault that the app is calling

# check container
az container logs --resource-group CW-Ressource-Group --name cw-summary-meetings  
az container show --resource-group CW-Ressource-Group --name cw-summary-meetings --query "identity.principalId" -o tsv           
az container show --resource-group CW-Ressource-Group --name cw-summary-meetings --query "ipAddress" --output json         
az container show --resource-group CW-Ressource-Group --name cw-summary-meetings --query "ipAddress.ip"         
az container show --resource-group CW-Ressource-Group --name cw-summary-meetings --query "containers[0].ports" --output json       

az container stop --resource-group CW-Ressource-Group --name cw-summary-meetings        
