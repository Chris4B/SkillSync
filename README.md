# **SkillSync** 🚀

## **📌 Présentation du Projet**
SkillSync est une **plateforme intelligente** permettant aux développeurs de **gérer et optimiser leur candidature** grâce à l'automatisation. Elle intègre un **CV dynamique, la gestion des projets via Trello, la synchronisation avec GitHub et la publication sur les réseaux sociaux**.

---

## **🎯 Objectifs du Projet**
🔹 **Générer un CV dynamique** évoluant en fonction des compétences acquises  
🔹 **Créer des projets techniques personnalisés** pour combler les lacunes  
🔹 **Gérer les tâches en mode Kanban (Trello)** et synchroniser avec GitHub  
🔹 **Publier automatiquement les réalisations** sur LinkedIn, Twitter, Dev.to  
🔹 **Suivre les interactions des recruteurs** et générer des statistiques

---

## **🛠️ Technologies Utilisées**
| **Module** | **Technologie** |
|-------------------|----------------|
| **Backend API** | FastAPI |
| **Base de Données** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Gestion de Projet** | Trello API |
| **Automatisation GitHub-Trello** | GitHub Actions |
| **Éditeur de Code** | Monaco Editor (VS Code), CodeMirror |
| **Exécution du Code** | Docker, Firecracker |
| **Suivi des Interactions** | Matplotlib, Pandas |
| **Publication R. Sociaux** | LinkedIn API, Twitter API, Dev.to API |
| **Envoi d'Emails** | SendGrid |
| **Notifications SMS/WhatsApp** | Twilio |

---
<!--
## **📂 Architecture du Projet**
```
backend-cv-trello/
│── 📂 app
│   │── 📂 api          # Routes API REST (utilisateurs, CV, projets)
│   │── 📂 models       # Modèles SQLAlchemy (BDD PostgreSQL)
│   │── 📂 database     # Connexion et gestion PostgreSQL
│   │── 📂 services     # Logique métier (PDF, Trello, GitHub)
│   │── 📂 security     # Authentification JWT et gestion des accès
│   │── 📂 utils        # Fonctions auxiliaires (logs, validation)
│── main.py             # Point d’entrée de l’API FastAPI
│── .env                # Variables d’environnement
│── requirements.txt    # Dépendances Python
│── docker-compose.yml  # Conteneurisation avec PostgreSQL
│── README.md           # Documentation du projet
```

---

## **🚀 Installation & Configuration**

### **1️⃣ Cloner le projet**
```bash
git clone https://github.com/tonutilisateur/backend-cv-trello.git
cd backend-cv-trello
```

### **2️⃣ Créer un environnement virtuel et installer les dépendances**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### **3️⃣ Configurer la base de données PostgreSQL**
Assurez-vous que PostgreSQL est installé et créez une base de données :
```sql
CREATE DATABASE skillsync_db;
CREATE USER skillsync_user WITH PASSWORD 'securepassword';
GRANT ALL PRIVILEGES ON DATABASE skillsync_db TO skillsync_user;
```

Ajoutez les informations de la base de données dans `.env` :
```bash
DATABASE_URL=postgresql://skillsync_user:securepassword@localhost/skillsync_db
```
-->
### **4️⃣ Lancer l’API FastAPI**
```bash
uvicorn main:app --reload
```

✅ **Accédez à l’API :** [http://127.0.0.1:8000](http://127.0.0.1:8000)  
✅ **Documentation interactive :** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## **🔑 Authentification & Sécurité**
✅ Gestion des utilisateurs avec **FastAPI + SQLAlchemy**  
✅ Authentification avec **JWT (JSON Web Tokens)**  
✅ Sécurisation des accès aux routes API  



---

## **📌 Gestion du CV**
✅ Stockage du CV en **format JSON**  
✅ Génération automatique d’un **CV en PDF**  
✅ Mise à jour avec **les compétences acquises** via les projets  
✅ Téléchargement et envoi du CV aux recruteurs  

📌 **Exemple d’API pour enregistrer un CV (`POST /cv/`)** :
```json
{
  "user_id": 1,
  "experiences": ["Développeur Python"],
  "skills": ["FastAPI", "PostgreSQL"],
  "education": ["Master Informatique"]
}
```

---

## **📌 Gestion des Projets et Trello**
✅ Intégration avec **Trello API** pour la gestion des tâches  
✅ Synchronisation automatique avec **GitHub Actions**  
✅ Suivi de l’avancement et mise à jour en **Kanban**  

📌 **Exemple d’API pour créer un projet (`POST /projects/`)** :
```json
{
  "name": "API FastAPI",
  "description": "Développement d'une API REST",
  "user_id": 1
}
```

---

## **📌 Suivi des Interactions et Notifications**
✅ Tracking des recruteurs qui consultent le CV  
✅ Suivi des téléchargements du CV et des clics GitHub  
✅ Notifications **Email (SendGrid) et SMS (Twilio)**  

---

## **📌 Déploiement & CI/CD**
🚀 **Déploiement Backend :** Render / Railway / AWS  
🚀 **Déploiement Frontend :** Vercel / Netlify  
🚀 **Intégration CI/CD :** GitHub Actions  

---
<!--
## **📌 Roadmap** 📅
🔜 **1. Finaliser l’authentification et la gestion des utilisateurs**  
🔜 **2. Améliorer le tracking des recruteurs et le reporting**  
🔜 **3. Ajouter une interface utilisateur (Frontend React/Vue)**  
🔜 **4. Automatiser encore plus la publication des réalisations**  

📌 **Tu veux contribuer ?** Forke le repo et propose une PR ! 🔥



## **💡 Contact & Support**
📩 **Email :** support@skillsync.com  
🌐 **Site Web :** [www.skillsync.com](http://www.skillsync.com)  
🐙 **GitHub :** [github.com/skillsync](http://github.com/skillsync)  

-->

💙 **Si ce projet t'intéresse, laisse une ⭐ sur GitHub !** 🚀

