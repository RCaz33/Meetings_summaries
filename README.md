# 📊 Azure ML Conversation Summarizer for Microsoft Teams

This project uses **Azure Machine Learning** and the **Conversation Summarization** capability to extract key insights from **Microsoft Teams meeting transcripts**. It automates the summarization of long meeting transcripts, helping teams quickly understand the discussion highlights, decisions made, and follow-up actions.

---

## 🚀 Features

- ✅ Automatically processes Teams meeting transcripts
- 🧠 Uses Azure ML's Conversation Summarization to extract:
  - Topics discussed [tool ChapterTitle]
  - Key decisions [tool narrative]
- 📁 Handles `.vtt` transcript formats
- ☁️ Integrates seamlessly with Azure resources
- 🔒 Securely processes data with Azure Identity and role-based access [AzureKeyCredential]

---

## 🛠️ Technologies

- **Python 3.10+**
- **Azure Machine Learning**
- **Azure OpenAI / Cognitive Services**
- **Azure Identity (for authentication)**
- **Jupyter / Streamlit** (Development, frontend)

---

## 📄 Folder Structure

```
Meetings_summary/
├── app_streamlit/          # Jupyter notebooks for development and testing
    ├── pages               # Front-end with Streamlit
    ├── utils               # Helper scripts
    ├── Acceuil.oy          # Front-end
    ├── Dockerfile          # ready file to contenairize app
    ├── requirements.txt    
├── .environ                # Need to set-up AZURE ressources credentials
├── HuggingFace_resume.ipynb# Assay with different framework
├── resume_equipe.ipynb     # Used for development               
├── summaries_from_txt.ipynb# Used for development
├── troubleshoot_azure.md   # To resolve common issues regarding azure
├── troubleshooting.md      # Guidelines to deploy on azure container instance
└── README.md
```

---

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/conversation-summarizer.git
   cd conversation-summarizer
   ```

2. **Set-up AZURE credential in a .env file**
   ```bash
   configure KeyVault access
   configure Language ressource usage
   ```

3. **Build and run Docker container**
   - Ensure you have map a volume to store the resume locally
   ```bash
   docker run -d -e LANGUAGE_KEY="<key_azure_language ressource>" -e LANGUAGE_ENDPOINT="" -p 8501:8501 -v "<local_volume>":<volume_in_container>
   ```

---

## ▶️ Usage

1. Loggin with Keyvault access
2. Upload your Teams transcript file into the app.
3. Run the summarization script or notebook:
4. Review the generated summary in the output folder.
5. Export as Doc file

---

## 📊 Output Example

```docx
Chapter title 1 : ..
Narrative 1 : ..
Chapter title 2 : ..
Narrative 2 : ..
.
.
.
```

---

## 📌 Notes

- Currently optimized for English-language transcripts
- Requires a supported Azure region with access to Conversation Intelligence
- Can only accept 2 identification name

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or have an idea for improvement, feel free to open an issue.

---

## 📄 License

This project is licensed under the MIT License.

---
