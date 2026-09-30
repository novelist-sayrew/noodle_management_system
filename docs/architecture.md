# Internal Design Documentation<br>
<br>

## 1. Overview<br>
&nbsp; This page summarizes detailed information about the internal design and processing logic of the noodle_management_system.<br>
&nbsp; While the README provides a simplified overview, this document explains each component in greater depth.<br>
<br>

## 2. Directory Structure
```
noodle_management_system
│
├── images                                   # Application demo images
├── README.md                                # Application overview (this file)
├── README_日本語版.md 
├── docs
│    ├─── architecture.md                    # Internal architecture documentation
│    └─── architecture_日本語版.md
│
├── app                                      # Application modules
│    ├── forms.py
│    ├── models.py
│    ├── scheduler.py                        # APScheduler jobs
│    ├── utils.py                            # Password reset email utilities
│    ├── __init__.py                         # create_app() initialization
│    │
│    ├── auth                                # User authentication module
│    │    ├── routes.py
│    │    ├── __init__.py
│    │    │
│    │    └─ templates
│    │  　     └─ auth
│    │  　         ├── forgot_password.html
│    │  　         ├── login.html
│    │  　         ├── register.html
│    │  　         └── reset_password.html
│    │
│    └─── noodle                             # Product management module
│         ├── routes.py
│         ├── __init__.py
│         │
│         └─ templates
│       　     └─ noodle
│       　         ├── base.html
│       　         ├── form.html
│       　         ├── list.html
│       　         └── warning.html          # Items nearing expiration
│
├── Procfile
├── requirements.txt
├── config.py                                # Configuration file
├── run.py
├── .env
└── .gitignore
```
## 3. Role of create_app()<br>
&nbsp; This application adopts the application factory pattern to simplify switching between development and production environments, and to safely initialize extensions such as SQLAlchemy, Flask‑Login, and APScheduler.<br>
<br>

### Initialization Order<br>
The following steps are executed inside create_app():<br>
<br>

#### 1. Create the Flask instance via create_app()<br>
#### 2. Load configuration from the Config class in config.py<br>
#### 3. Load environment variables and register settings such as DATABASE_URI<br>
#### 4. Initialize extensions such as LoginManager and SQLAlchemy<br>
##### Reasons:<br>
・Extensions like SQLAlchemy cannot be initialized until configuration values (e.g., DATABASE_URI) are loaded; otherwise a RuntimeError occurs.<br>
・Blueprint registration requires extensions such as LoginManager to be initialized beforehand.<br>
・Since DB models reference the db instance, importing models before initializing db causes circular imports.<br>
<br>

#### 5. Import DB models such as User<br>
##### Reasons:<br>
&nbsp; This ensures SQLAlchemy registers the models and prevents ImportError or circular import issues.<br>
<br>

#### 6. Create the application context<br>
##### Reasons:<br>
・Blueprint registration requires current_app, and DB table creation requires current_config.<br>
・To use these features, the application context must be established.<br>
<br>

#### 7. Register Blueprints<br>
##### Reasons:<br>
Routing is separated by responsibility:<br>
・auth — user registration, authentication, password reset<br>
・noodle — product editing, deletion, expiration calculation<br>
<br>

#### 8. Create DB tables<br>
##### Reasons:<br>
&nbsp; Registering Blueprints first clarifies routing and application structure, ensuring correct table creation.<br>
<br>

#### 9. Define the top‑level route<br>
<br>

## 4. Blueprint Structure<br>
### auth (Authentication Features)<br>
・User registration and login authentication<br>
・Logout processing<br>
・Token generation and password reset email sending<br>
・Password reset handling, invalid token detection, and error processing<br>
<br>

### noodle (Product Management Features)<br>
・Base “/” page<br>
・Automatic expiration date calculation<br>
・Sorting products by expiration date<br>
・Page showing only products expiring within 5 days<br>
・Product editing, addition, and deletion<br>
<br>

## 5. Simplified Password Reset Flow<br>
1. User clicks “Forgot your password?”<br>
2. User enters their email address<br>
3. A token is generated and stored in the DB<br>
4. Flask sends an email containing a URL with the token<br>
5. User accesses the URL<br>
6. Flask validates the token and displays the password reset page<br>
7. User submits a new password<br>
8. Flask updates the password in the DB and invalidates the token<br>
9. Flask redirects the user to the login page<br>
<br>

## 6. DB Model Design Intent<br>
#### User Model<br>
・id<br>
・username<br>
・email<br>
・password_hash<br>
<br>

#### Noodle Model<br>
・id<br>
・name<br>
・year, month, day<br>
・No relations (data is shared among all users)<br>
<br>

## 7. APScheduler Job Design<br>
### Job Purpose and Security Considerations<br>
&nbsp; To prevent replay attacks and token reuse attacks, and to avoid unnecessary DB growth, tokens expire after 30 minutes, and an interval job runs every 1 hour to delete expired or used tokens.<br>
<br>

### Execution Timing<br>
&nbsp; WSGI servers spawn multiple worker processes.
If cron scheduling is used, every worker may execute the job simultaneously, causing duplicate execution.<br>
&nbsp; To avoid this, scheduler.start() is called inside create_app(), and interval scheduling is used so jobs run relative to application startup.<br>
<br>

### Preventing Duplicate Execution<br>
&nbsp; Because WSGI workers are forked, placing scheduler.start() in the global scope causes both parent and child processes to start the scheduler.<br>
&nbsp; To avoid this, scheduler initialization is separated into scheduler.py, and the scheduler is started only inside create_app().<br>
<br>

## 8. Application‑Wide Security Design<br>
#### SECRET_KEY Configuration<br>
・Prevents cookie tampering → protects against session hijacking<br>
・Enables CSRF protection<br>
<br>

#### Environment Variables (.env)<br>
・Prevents hard‑coding sensitive information<br>
・Protects passwords and email credentials<br>
<br>

#### Password Hashing<br>
・Password + hashing + salt reduces leakage risk<br>
・Protects against brute‑force attacks<br>
<br>

#### APScheduler Token Deletion<br>
・Prevents replay attacks<br>
・Prevents token reuse attacks<br>
・Reduces DB load → lowers DoS risk<br>

#### HTTPS Encryption<br>
・TLS encrypts communication (login info, tokens), preventing man‑in‑the‑middle attacks.<br>
<br>

## 9. Future Improvements<br>
・Data consistency issues caused by simultaneous editing<br>
・Barcode scanning for improved usability<br>
・Edit history and deletion history features<br>