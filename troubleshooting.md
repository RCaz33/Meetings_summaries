Create free Azure accoutn

Accept Microsoft term of use

Put personnal bank coordinated


Possible trial assay from .txt files
==> https://language.cognitive.azure.com/home (https://language.cognitive.azure.com/tryout/summarization)

Tutoriel to follow her 
==> https://learn.microsoft.com/fr-fr/azure/ai-services/language-service/summarization/overview?tabs=text-summarization

==> save environ variable (export ...) 
LANGUAGE_KEY=your-key
LANGUAGE_ENDPOINT=your-endpoint

INstall azure librairy
pip install azure-ai-language-conversations==1.1.0

complete sdk librairy here:
https://learn.microsoft.com/en-us/python/api/azure-ai-textanalytics/azure.ai.textanalytics?view=azure-python&viewFallbackFrom=azure-python-preview&preserve-view=true




déployer la solution locale dasn un contenaur docker
https://learn.microsoft.com/fr-fr/azure/ai-services/language-service/summarization/how-to/use-containers

La licence des conteneurs Azure AI Services ne vous permet pas de les exécuter sans les connecter au point de terminaison du compteur ou de la facturation. Vous devez configurer les conteneurs de manière à ce qu’ils communiquent les informations de facturation au point de terminaison de facturation à tout moment. Les conteneurs Azure AI Services n’envoient pas de données client, telles que l’image ou le texte analysé, à Microsoft.