# 📘 Content Management System (CMS)

A professional **Content Management System (CMS)** built using **Python, Flask, SQLite, Bootstrap, and REST APIs**.  
This project supports **role-based access control (Admin, Editor, Viewer)** and allows managing content via **UI and Postman APIs**.

---

## 🚀 Features

### 🔐 Authentication & Roles
- Secure login system
- Password hashing
- Role-based access control:
  - **Admin**: Add, Edit, Delete
  - **Editor**: Add, Edit
  - **Viewer**: View only

### 📝 Content Management
- Add content via UI
- Edit content
- Delete content (Admin only)
- View all content in dashboard
- Search content by title

### 🎨 Professional UI
- Modern dashboard with stats cards
- Card-based content layout
- Clean login page
- Responsive design using Bootstrap

### 🔌 REST API (Postman)
- Create content via API
- Fetch all posts
- Fetch single post
- Update post
- Delete post
- API-created content author is automatically set to **Postman**

---

## 🛠️ Technology Stack

| Layer | Technology |
|------|-----------|
| Backend | Python, Flask |
| Frontend | HTML, Bootstrap |
| Database | SQLite |
| ORM | SQLAlchemy |
| Auth | Flask-Login |
| API Testing | Postman |
| Version Control | Git, GitHub |

---

## How to Run the Project

Clone the repository, install dependencies, create the database, create users, and start the server using the following commands:

pip install -r requirements.txt  
python create_db.py  
python create_user.py  
python create_viewer.py  
python run.py  

Open the application in a browser at:

http://127.0.0.1:5000/login

---

## Default User Credentials

Admin  
Username: admin  
Password: admin123  

Viewer  
Username: viewer  
Password: viewer123  

---

## REST API Endpoints

GET    /api/posts          → Fetch all posts  
GET    /api/posts/{id}     → Fetch single post  
POST   /api/posts          → Create post  
PUT    /api/posts/{id}     → Update post  
DELETE /api/posts/{id}     → Delete post  

Note: All posts created via API automatically have the author set to **Postman**.

---

## Security

- Passwords are hashed before storage
- Routes are protected using login sessions
- Role-based authorization is enforced
- Database and virtual environment are excluded from Git using .gitignore

---

## Academic and Portfolio Use

This project is suitable for:
- College mini and major projects
- Viva examinations
- Backend / full-stack portfolios
- GitHub project showcase

---

## Conclusion

This CMS demonstrates real-world backend development using Flask, including authentication, authorization, REST APIs, professional UI design, and version control. It is designed to be simple, scalable, and easy to understand while following industry practices.

---

<img width="1919" height="947" alt="Screenshot 2026-01-28 191033" src="https://github.com/user-attachments/assets/a46e5ad1-8d84-4635-ad87-cfd7f560fdab" />
<img width="1919" height="938" alt="Screenshot 2026-01-28 191127" src="https://github.com/user-attachments/assets/b488236e-683c-4560-8a64-70edb9a310a4" />
<img width="1917" height="945" alt="Screenshot 2026-01-28 191156" src="https://github.com/user-attachments/assets/b7808eb0-18ca-410a-bb2e-83ef641c3abc" />
<img width="1919" height="934" alt="Screenshot 2026-01-28 191221" src="https://github.com/user-attachments/assets/3904f129-f031-491e-9441-bbbf283cda38" />
<img width="1919" height="929" alt="Screenshot 2026-01-28 191417" src="https://github.com/user-attachments/assets/2ce5e6cc-d658-45f0-b108-539fe88690b4" />



