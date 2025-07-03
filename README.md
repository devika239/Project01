Bank Management System
Project Overview
This project is a robust, Python-based application designed to simulate core banking operations within a secure environment. It serves as a practical demonstration of fundamental software engineering principles, including database management, secure user authentication, role-based access control, and transaction processing. The system currently operates as a Command-Line Interface (CLI) application, making it a foundational backend system capable of managing user accounts and financial transactions.
Key Features
Secure User Authentication: Implements a robust registration and login system with password hashing, supporting both standard user accounts and administrative roles.
User Account Management: Allows users to create multiple bank accounts (e.g., savings, checking) and view their account details, including balances.
Financial Transaction Processing: Supports fundamental banking operations such as:
Deposits: Adding funds to a specified account.
Withdrawals: Removing funds from an account, with balance checks to prevent overdrafts.
Transfers: Facilitating secure money transfers between different bank accounts within the system.
Comprehensive Transaction History: Provides detailed logs for all account activities, including transaction type, amount, description, and timestamp.
Real-time Balance Updates: Ensures account balances are accurately and immediately reflected after each transaction.
Admin-Level Monitoring & Control: A dedicated administrator panel provides privileged functionalities:
Viewing a list of all registered users.
Toggling user account activation status (enabling/disabling user access).
Monitoring all bank accounts and their current balances across the system.
Accessing a complete audit log of all financial transactions within the bank.
Technologies Used
Core Language: Python 3.x
Database: SQLite (for development and local persistence, easily adaptable to PostgreSQL for production)
Object-Relational Mapper (ORM): SQLAlchemy
Chosen for its abstraction layer over raw SQL, allowing interaction with the database using Python objects, enhancing code readability, and providing database independence.
Password Hashing: bcrypt
Used for securely hashing user passwords, including automatic salting, to prevent plaintext storage and protect against common attacks like rainbow table lookups.
System Interaction: os and sys modules for command-line operations (e.g., clearing screen, exiting application).
Data Handling: Standard Python data structures and datetime for timestamps.
Architectural Highlights & Design Choices
Modular Architecture: The application is logically separated into distinct Python modules (database.py, auth.py, bank_operations.py, admin_operations.py, cli_app.py). This promotes code organization, reusability, and makes the system easier to debug and extend.
Layered Design:
Data Layer: SQLAlchemy models define the database schema and handle persistence.
Business Logic Layer: Functions for banking operations and authentication rules reside here.
Presentation Layer: The CLI handles user input and output.
Secure Password Management: A critical design choice was to never store plaintext passwords. bcrypt generates strong, unique hashes for each password, which are then stored in the database. Password verification involves hashing the entered password and comparing it to the stored hash.
Error Handling: Robust try-except blocks are implemented around database operations and user input to gracefully manage exceptions (e.g., SQLAlchemyError, ValueError) and provide informative feedback to the user.
Role-Based Access Control (RBAC): Differentiating between 'user' and 'admin' roles at the application level ensures that only authorized individuals can perform sensitive administrative tasks, enhancing system security.
Challenges and Solutions
Challenge: Managing Database Sessions: Ensuring proper session handling with SQLAlchemy (opening, committing/rolling back, and closing sessions for each operation) was crucial to prevent resource leaks and maintain data integrity, especially given Python's threading model.
Solution: Implemented a session factory (Session = sessionmaker(bind=engine)) and consistently managed sessions within try...finally blocks in each database interaction function, ensuring sessions are closed regardless of success or failure.
Challenge: Password Security: Storing and verifying passwords securely is paramount.
Solution: Integrated bcrypt for one-way password hashing with salting, a cryptographic best practice that protects against brute-force attacks and rainbow table attacks.

Future Enhancements
Graphical User Interface (GUI): Transitioning from CLI to a more user-friendly GUI (e.g., using Tkinter, PyQt, or a web framework like Flask/Django with a frontend) would enhance user experience.
External Database: Migrating from SQLite to a robust external database like PostgreSQL or MySQL for better scalability and concurrent access in a production environment.
Enhanced Security: Implementing features like two-factor authentication (2FA), rate limiting for login attempts, and detailed audit logging of administrative actions.
Advanced Features: Adding more complex banking features such as loan management, interest calculation, account statements, and notifications.
Transaction Limits & Fees: Incorporating business logic for transaction limits and various service fees.
Comprehensive Testing: Developing a suite of unit tests, integration tests, and end-to-end tests to ensure reliability and correctness.






















E-commerce Backend Engine

Project Overview
This project is designed as a foundational RESTful API backend for a modern e-commerce platform. Built with Python, it focuses on providing core functionalities necessary for an online shopping experience, including user management, product catalog, shopping cart logic, order processing, and an administrative control panel. The system is architected to be scalable and maintainable, offering a clear separation of concerns suitable for integration with various frontend applications.
Key Features
Secure User Management:
User Registration & Authentication: Implements robust user signup and login processes with secure password hashing (e.g., bcrypt).
Session Management: Handles user sessions securely (e.g., JWTs for stateless APIs or server-side sessions).
Role-Based Access Control (RBAC): Differentiates between 'customer' and 'admin' roles, restricting access to sensitive endpoints and functionalities.
Product Catalog Management:
Product Listings: Allows administrators to add, update, and remove products with details like name, description, price, and stock levels.
Product Search & Filtering: Supports querying products based on various criteria.
Shopping Cart System:
Add/Remove Items: Users can add products to their cart and adjust quantities.
Cart Persistence: Maintains the state of a user's shopping cart.
Stock Validation: Checks product availability before adding to cart and during checkout.
Order Processing & Management:
Order Creation: Converts a user's cart into a formal order, deducting stock.
Order History: Users can view their past orders and their statuses.
Order Status Updates: Admins can update order statuses (e.g., pending, processing, shipped, delivered, cancelled).
Admin Panel (API Endpoints): Provides privileged APIs for:
Managing user accounts (e.g., toggling active status, changing roles).
Adding, updating, and deleting products.
Viewing and managing all system orders.
Monitoring overall system activity.
Technologies Used
Core Language: Python 3.x
Web Framework: Flask / Django (or FastAPI, depending on design choice)
Chosen for building RESTful APIs, providing routing, request/response handling, and middleware capabilities.
Database: PostgreSQL / SQLite (for development)
Relational database for structured data storage. PostgreSQL is preferred for production due to its robustness and features.
Object-Relational Mapper (ORM): SQLAlchemy / Django ORM
Provides an abstraction layer for interacting with the database using Python objects, simplifying database operations and schema management.
Password Hashing: bcrypt / Werkzeug.security (for Flask) / Django's built-in hashing
Essential for securely storing user passwords.
API Authentication: JWT (JSON Web Tokens) or Session-based authentication
For securing API endpoints and managing user sessions.
Validation: Marshmallow (for Flask) / Django Rest Framework serializers
For validating incoming request data and serializing outgoing responses.
Containerization (Optional but recommended): Docker
For packaging the application and its dependencies into isolated containers, ensuring consistent deployment across environments.
Architectural Highlights & Design Choices
RESTful API Design:
Designed with clear, resource-oriented endpoints (e.g., /products, /users, /orders).
Utilizes standard HTTP methods (GET, POST, PUT, DELETE) for corresponding CRUD operations.
Adheres to principles of statelessness (if using JWTs), allowing for easier scaling.
Modular & Layered Architecture:
models.py: Defines database schema and relationships.
schemas.py / serializers.py: Handles data validation and serialization/deserialization between Python objects and JSON.
views.py / routes.py: Contains API endpoint logic, processing requests and returning responses.
services.py / managers.py: Encapsulates business logic, abstracting database interactions from view logic.
Database Transaction Management: Ensures atomicity of critical operations (e.g., order placement involves deducting stock and creating order records as a single, all-or-nothing transaction).
Security Best Practices:
Password Hashing: As mentioned, never stores plaintext passwords.
Input Validation: Strict validation of all incoming API request data to prevent common vulnerabilities like SQL injection and cross-site scripting (XSS).
Authentication & Authorization: Securely verifies user identity and permissions for each API request.
Error Handling: Custom error handling for API responses, returning meaningful HTTP status codes and error messages.
Challenges and Solutions
Challenge: Concurrent Stock Management: Preventing race conditions when multiple users try to purchase the same limited stock item simultaneously.
Solution: Implemented database-level locking mechanisms or atomic updates where possible (e.g., using SELECT FOR UPDATE or careful transaction management) to ensure accurate stock deduction.
Challenge: API Security & Scalability: Maintaining security while allowing the API to scale to many users and requests.
Solution: Utilized JWTs for stateless authentication, reducing server load for session management. Ensured proper token validation and expiration. For production, would consider API Gateway for rate limiting and additional security layers.
Challenge: Data Consistency in Orders: Ensuring that order items accurately reflect product prices and stock at the moment of purchase, even if product details change later.
Solution: Stored price_at_purchase directly in OrderItem to snapshot the price, decoupled from the current Product price. This ensures historical order accuracy.
Future Enhancements
Payment Gateway Integration: Integrating with external payment processors (e.g., Stripe, PayPal) for real-money transactions.
Search Engine Integration: Implementing advanced search capabilities using technologies like Elasticsearch or Algolia.
Asynchronous Tasks: Using a message queue (e.g., RabbitMQ, Celery) for background tasks like order confirmation emails, inventory updates, or complex data processing.
Caching Layer: Implementing caching (e.g., Redis) for frequently accessed data (like product listings) to improve API response times and reduce database load.
Container Orchestration: Deploying with Kubernetes for robust scaling, load balancing, and self-healing capabilities.
Logging & Monitoring: Integrating with logging and monitoring tools (e.g., ELK Stack, Prometheus, Grafana) for operational insights and debugging.
Advanced Admin Features: Adding dashboards, sales reports, user analytics, and discount/coupon management.



Multi-User Chat Application
This project is a real-time, multi-user chat application developed using Python's low-level network programming capabilities (sockets) and concurrency management (threading). It consists of a central server and multiple client applications, enabling users to communicate instantaneously in a shared chat room. This project effectively demonstrates fundamental concepts of network communication, concurrent programming, and basic application-level protocols.
Key Features
Real-time Messaging: Facilitates instant message exchange between all connected clients.
Multi-Client Support: The server is designed to handle simultaneous connections from numerous clients, allowing multiple users to participate in the same chat session concurrently.
Unique Usernames: Each client connects with a user-defined nickname, which is displayed alongside their messages for clear identification. The server enforces uniqueness to prevent impersonation.
Message Broadcasting: When a message is sent by one client, the server broadcasts it to all other active clients, ensuring everyone sees the conversation.
Basic Moderation Commands: Includes rudimentary server-side moderation capabilities (e.g., /kick command for administrators to disconnect users), showcasing role-based actions within the chat environment.
Connection Management: Handles client connections and disconnections gracefully, notifying other users when someone joins or leaves.
Technologies Used
Core Language: Python 3.x
Network Programming: Python's built-in socket module for creating TCP/IP client and server sockets, managing connections, and sending/receiving data.
Concurrency: Python's threading module to allow the server to handle multiple client connections simultaneously without blocking. Each connected client runs in its own dedicated thread on the server side, ensuring responsiveness.
Standard Library: sys and os modules for system-level operations like program exit and terminal control.
Architectural Highlights & Design Choices
Client-Server Architecture: A clear separation between the central server (which manages communication) and individual clients (which send and receive messages).
Thread-per-Client Model: The server employs a "thread-per-client" model, where each incoming client connection is handled by its own dedicated thread. This design allows the server to concurrently listen for new connections while simultaneously processing messages from existing clients.
Blocking Sockets with Threads: Standard blocking socket operations are used, but the threading model prevents the overall application from freezing. Each thread blocks only on its specific client's I/O.
Shared Resource Management: A threading.Lock is used to protect shared data structures on the server (like the list of active clients and their nicknames) from race conditions, ensuring data consistency when multiple threads access them.
Simple Protocol: A lightweight, text-based protocol where clients send their nickname first, followed by chat messages. Commands are distinguished by a leading slash (/).
Error Handling: Includes try-except blocks to manage common network and I/O errors (e.g., ConnectionRefusedError, ConnectionResetError, UnicodeDecodeError, socket.error), providing resilience and informative feedback.
Challenges and Solutions
Challenge: Concurrent Client Handling: Directly managing multiple active network connections without blocking the main server loop.
Solution: Implemented threading.Thread for each client. The main server thread continuously accept()s new connections, and for each, it spawns a new thread to handle_client communication.
Challenge: Data Synchronization: Ensuring that shared server-side data (like the list of active clients and their nicknames) remains consistent when accessed or modified by multiple client-handling threads.
Solution: Employed threading.Lock to create critical sections around operations that modify shared client lists (clients.append, clients.remove, nicknames.append, nicknames.remove).
Challenge: Graceful Disconnection: Detecting and handling client disconnections, both graceful and abrupt.
Solution: The client.recv() method returning an empty bytes object (b'') signals a graceful client disconnect. ConnectionResetError is caught for abrupt disconnections. Clients are removed from tracking lists and their sockets are closed.
Future Enhancements
Persistent Chat History: Integrate with a database (like SQLite or PostgreSQL) to store chat messages, allowing users to view past conversations upon joining.
Private Messaging: Implement functionality for clients to send direct messages to specific users.
Chat Rooms/Channels: Introduce support for multiple chat rooms, allowing users to join different conversations.
Enhanced Moderation: Implement more sophisticated moderation features like muting, banning (with persistence), and a dedicated admin interface for managing users and messages.
Graphical User Interface (GUI): Develop a GUI client using libraries like Tkinter, PyQt, or web technologies for a more user-friendly experience.
Security: Implement encryption for messages (e.g., SSL/TLS sockets) to protect data in transit.
Scalability: For very large-scale applications, consider asynchronous I/O frameworks (like asyncio) or specialized message brokers (like RabbitMQ or Redis Pub/Sub) instead of a simple thread-per-client model.
















Custom File Encryption/Decryption Tool

Project Overview
This project is a standalone Python-based tool designed to provide robust file encryption and decryption capabilities. Its primary goal is to secure sensitive files using industry-standard cryptographic algorithms, ensuring data confidentiality and integrity. The tool empowers users to encrypt and decrypt files using a passphrase, demonstrating a practical application of modern cryptography for data protection.
Key Features
Symmetric Encryption (AES-256): Implements the Advanced Encryption Standard (AES) with a 256-bit key in CBC (Cipher Block Chaining) mode. This provides strong, efficient, and widely recognized encryption for bulk data.
Secure Key Derivation: Utilizes PBKDF2 (Password-Based Key Derivation Function 2) with SHA256 and a high iteration count (e.g., 100,000) to derive a strong cryptographic key from a user-provided passphrase. This makes brute-forcing passwords significantly harder.
Random Salt Generation: Employs a unique, cryptographically strong random salt for each encryption operation. The salt is stored alongside the ciphertext, ensuring that identical passwords encrypt to different ciphertexts, and protecting against rainbow table attacks.
Initialization Vector (IV) Management: Generates a unique, random Initialization Vector (IV) for each encryption. The IV is crucial for CBC mode to prevent identical plaintext blocks from producing identical ciphertext blocks, enhancing security.
Padding (PKCS7): Implements PKCS7 padding to ensure plaintext data always aligns with the block size of the AES algorithm, which is necessary for correct encryption and decryption.
File Stream Processing: Designed to encrypt and decrypt files chunk by chunk, making it suitable for large files without loading the entire content into memory.
Robust Error Handling: Includes comprehensive error handling for file operations (e.g., FileNotFoundError), incorrect passwords (via padding validation errors), and general cryptographic exceptions.
User-Defined Passphrases: Allows users to define their own strong passwords for encryption, providing personalized control over data security.
Technologies Used
Core Language: Python 3.x
Cryptography Library: cryptography
Chosen for its focus on modern, secure cryptographic primitives and its adherence to best practices. It provides a higher-level API compared to raw os.urandom and bitwise operations, reducing implementation errors.
Specifically, cryptography.hazmat.primitives.ciphers for AES and CBC mode.
cryptography.hazmat.primitives.kdf.pbkdf2 for PBKDF2HMAC key derivation.
cryptography.hazmat.primitives.padding for PKCS7 padding.
Randomness: Python's built-in secrets module for generating cryptographically strong random numbers for salts and IVs.
File I/O: Standard Python file handling for reading input files and writing output files in binary mode.
Hash Functions: hashlib for general hashing if needed, though cryptography's primitives often include hashing as part of KDF.
Architectural Highlights & Design Choices
Command-Line Interface (CLI): Provides a simple, interactive command-line interface for ease of use, guiding the user through encryption/decryption steps.
Symmetric Encryption Focus: Primarily focuses on AES for file encryption due to its speed and suitability for encrypting large amounts of data. RSA (asymmetric) is typically used for key exchange or digital signatures, not direct file encryption due to its performance characteristics.
Component Separation: Logic is modularized into distinct functions for key derivation, encryption, decryption, and the main CLI interaction, promoting readability and maintainability.
Security by Design:
No Hardcoded Keys: Passwords are user-provided and ephemeral for key derivation.
Unique Salt and IV per Encryption: Ensures that even identical plaintexts encrypted with the same password result in different ciphertexts, increasing resistance to various attacks.
Padding Oracle Attack Mitigation: Using authenticated modes like AES-GCM (though not implemented in the provided solution for simplicity, it's a key future enhancement) would offer protection against padding oracle attacks in addition to CBC mode's inherent properties.
Memory Efficiency: Processing files in chunks prevents memory overflow when dealing with very large files.
Challenges and Solutions
Challenge: Secure Key Management: Deriving a strong, consistent key from a user's potentially weak passphrase.
Solution: Employed PBKDF2HMAC, which intentionally adds computational cost (iterations) to the key derivation process. This makes brute-forcing the password, even if the hash is known, computationally infeasible.
Challenge: Maintaining Integrity and Authenticity: Ensuring that the encrypted file has not been tampered with and that it originates from the expected source.
Solution (Current): AES-CBC provides confidentiality but not inherent integrity or authenticity. Padding validation during decryption helps detect some tampering that corrupts the padding.
Future Solution: Implementing an Authenticated Encryption with Associated Data (AEAD) mode like AES-GCM would inherently provide both confidentiality and integrity/authenticity.
Challenge: Handling File Size and Padding: Ensuring that files of any size can be encrypted correctly and that decryption can reconstruct the original data precisely.
Solution: PKCS7 padding ensures that the final block of plaintext is correctly sized for encryption. Chunk-based reading and writing, along with careful handling of the final (possibly partial) block and padding application/removal, addresses arbitrary file sizes.
Future Enhancements
Authenticated Encryption (AES-GCM): Upgrade the encryption mode to AES-GCM for integrated confidentiality, integrity, and authenticity, providing stronger protection against tampering.
Asymmetric Encryption (RSA) for Key Exchange: For more advanced scenarios, implement RSA to encrypt the AES key, allowing secure key exchange when sharing files with specific recipients without sharing the passphrase directly.
Metadata Storage: Encrypt and store file metadata (original filename, size, checksum) within the encrypted file's header.
Graphical User Interface (GUI): Develop a user-friendly GUI using libraries like Tkinter or PyQt for easier interaction.
Directory Encryption: Extend functionality to encrypt entire directories, maintaining the directory structure.
Performance Optimization: For very large files, explore techniques like multi-threading for I/O operations (though Python's GIL can limit CPU-bound crypto operations).
Cross-Platform Compatibility: Ensure the tool runs seamlessly across different operating systems.









Library Management System
Library Management System — Project Documentation

Project Overview:
-----------------
The Library Management System is a desktop-based application developed using Python and Tkinter for the graphical interface, along with SQLite as the database. This application allows users (such as librarians or students) to manage a library by adding, issuing, returning, and deleting books. It also supports tracking the availability of books and calculating late return penalties.

The GUI provides an intuitive interface where users can perform operations such as searching for a book by title, issuing a book to a user with an issue date, returning it with an optional return date, and calculating the fine if the return is delayed beyond the grace period.

Key Features:
-------------
- Add books with title and author.
- View list of all available and issued books.
- Issue books to users with automatic status update.
- Return books and calculate late fees after 14-day grace period.
- Search books by title.
- Delete unissued books from the inventory.

Technologies Used:
------------------
- Python 3.12
- Tkinter (GUI Framework)
- SQLite (Embedded Database)

File Structure:
---------------
- main.py        → Launches the GUI application.
- ui.py          → Contains all GUI components and user interaction logic.
- database.py    → Handles all database-related operations such as insert, update, delete.
- utils.py       → Contains late fee calculation logic.
- library.db     → Auto-created database storing books and issue records.

How to Run:
-----------
1. Install Python 3.12.
2. Open the project in PyCharm or any IDE.
3. Run `main.py` to start the app.
4. Use the GUI to add books and manage inventory.

Future Enhancements:
--------------------
- Add authentication system for staff and students.
- Enable barcode scanning for quick check-in/out.
- Generate reports and export data to Excel/PDF.
- Add category/tags for books and advanced filtering.








PDF Merger & Splitter Utility
PDF Merger & Splitter Utility — Project Documentation

Project Overview:
-----------------
This is a lightweight desktop application for managing PDF files using Python. Built with Tkinter for GUI and PyPDF2 for PDF operations, the application allows users to merge multiple PDF files, split a PDF into individual pages, and extract specific pages from a given PDF. It simplifies the manipulation of PDF files through a user-friendly interface.

Key Features:
-------------
- Select and merge multiple PDF files into one document.
- Split one PDF file into multiple single-page files.
- Extract specific page numbers and save them into a new file.
- Simple GUI to allow easy file selection and execution.

Technologies Used:
------------------
- Python 3.12
- Tkinter (GUI)
- PyPDF2 (PDF library)

File Structure:
---------------
- main.py        → Entry point to the application.
- ui.py          → Contains GUI layout and control flow.
- pdf_utils.py   → All PDF operations (merge, split, extract).

How to Run:
-----------
1. Install Python 3.12 and PyPDF2: `pip install PyPDF2`.
2. Open the project in any IDE.
3. Run `main.py` and the GUI will open.
4. Use buttons to perform operations on selected PDF files.

Future Enhancements:
--------------------
- Allow reordering of PDF pages before merge.
- Add drag-and-drop support.
- Add progress bar and file preview.
- Allow password-protected PDFs.










Task Scheduler with Notifications
Task Scheduler with Notifications — Project Documentation

Project Overview:
-----------------
A desktop reminder application built using Python and Tkinter that helps users create and manage scheduled tasks. The app supports due dates, recurring tasks (daily or weekly), and sends real-time desktop notifications using the Plyer library. Task data is saved in SQLite, and unique task IDs are generated using base62 encoding.

Key Features:
-------------
- Add tasks with title, description, due date and time.
- Specify task repetition: once, daily, or weekly.
- Background thread monitors and triggers alerts on time.
- Tasks stored persistently in SQLite.
- Notification popup using cross-platform Plyer library.
- Task IDs are uniquely generated with custom base62 logic.

Technologies Used:
------------------
- Python 3.12
- Tkinter (GUI)
- SQLite3 (Local Database)
- Plyer (Desktop notifications)
- Base62 encoding (for ID logic)

File Structure:
---------------
- main.py        → App startup file.
- ui.py          → Interface layout and control events.
- db_utils.py    → Database interaction logic.
- notify.py      → Triggers plyer-based notifications.
- base62.py      → Encodes task IDs to readable short form.

How to Run:
-----------
1. Install Python 3.12 and Plyer: `pip install plyer`.
2. Open the folder in an IDE like PyCharm.
3. Run `main.py`.
4. Fill out task details and let the app notify you on schedule.

Future Enhancements:
--------------------
- Feature to edit/delete tasks.
- Display upcoming/past task list.
- Export/import task list to/from CSV or JSON.
- Add audible reminders and alarms.









URL Shortener Microservice
URL Shortener Microservice — Project Documentation

Project Overview:
-----------------
This microservice web application converts long URLs into short redirectable links using base62 encoding. It is developed using Flask for the web interface and SQLite for persistent storage. When users visit the short link, the app redirects them to the original URL.

Key Features:
-------------
- Form-based interface to submit long URLs.
- Generates compact, encoded short links.
- Stores and retrieves URL mappings from SQLite.
- Redirects short link to the original target.
- Supports full single-file implementation for deployment.

Technologies Used:
------------------
- Python 3.12
- Flask (Web framework)
- SQLite (Database)
- Base62 encoding (for short links)

File Structure:
---------------
- URLShortener.py → Single-file Flask application with logic for form, DB, redirect, and encode/decode.
- urls.db         → SQLite database for link storage.

How to Run:
-----------
1. Install Python 3.12 and Flask: `pip install flask`.
2. Run `python URLShortener.py`.
3. Open browser and visit: `http://localhost:5000/`.

Future Enhancements:
--------------------
- Admin dashboard to view/manage all shortened links.
- Add click analytics and expiration settings.
- Add custom alias feature.
- Deploy on cloud with domain and SSL.




Inventory Management System
Description
A GUI-based Inventory Management System built using Python and Tkinter. It helps small businesses
manage their stock by allowing them to add, update, delete, and search inventory items. It also supports
CSV export, total inventory value calculation, and alerts for low stock levels.
Features
Add, update, delete, and search inventory items
View total inventory value
Export inventory data to CSV
Restock alerts for low quantity
User-friendly GUI with real-time table display
Technologies
Python 3.x
Tkinter
CSV (built-in)
Getting Started
Create and activate a virtual environment
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

Install dependencies
pip install -r requirements.txt
Run the app
python inventory_gui.py
•
•
•
•
•

•
•
•

1

Requirements
tkinter






CLI-Based Project Tracker with GUI
Description
A GUI-based project tracker that helps freelancers or developers track project hours, time logs, billing, and
notes. It allows project-wise log entries, hourly billing computation, summary generation, and CSV export.
Features
Add projects with hourly rate
Log work hours with notes
View logs in a dynamic table
Generate and view billing summaries
Export time logs to CSV
GUI built using Tkinter
Technologies
Python 3.x
Tkinter
CSV
datetime
Getting Started
Create and activate a virtual environment
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

Install dependencies
pip install -r requirements.txt
•
•
•
•
•
•

•
•
•
•

2

Run the app
python project_tracker.py
Requirements
tkinter





DNS Lookup and Traceroute Tool
Description
A Python-based network diagnostic tool that performs DNS resolution, traceroutes, and latency checks. It
helps users and network engineers analyze connectivity issues.
Features
DNS Lookup
ICMP-based Traceroute
Latency testing using ping logic
Technologies
Python 3.x
socket
scapy
time
Getting Started
Create and activate a virtual environment
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
•
•
•

•
•
•
•

3

Install dependencies
pip install scapy
Run the app
python dns_tool.py

Requirements

scapy
⚠ Note: You might see a No libpcap provider available warning. It can be ignored if basic
traceroute and ping are functioning.








Advanced File Organizer Bot
Description
An intelligent file organization bot with a GUI that monitors a selected folder and organizes files in real-time
based on extension, type, or size. Ideal for automating cleanup in Downloads or Desktop folders.
Features
GUI for selecting folder and sorting options
Organizes files by extension/type/size
Real-time monitoring using Watchdog
Auto-creates categorized folders
Technologies
Python 3.x
Tkinter
Watchdog
OS / shutil
•
•
•
•

•
•
•
•

4

Getting Started
Create and activate a virtual environment
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

Install dependencies
pip install watchdog
Run the app
python file_organizer.py
Requirements
watchdog

Each project includes clean UI, error handling, and is beginner-friendly yet practical for real-world use.






Command-Line Password Manager
Project Description
This project is a secure Python-based command-line application designed to manage and protect user passwords. It uses a master password to control access and applies AES encryption (via the cryptography library) to store all credentials safely in a local file.
Users can add, view, and manage credentials for multiple websites or apps. Passwords are encrypted and stored in a JSON file (vault.json), and can only be accessed after entering the correct master key. The project uses getpass to securely input passwords without displaying them on the screen.

 Key Highlights
Local password storage with AES encryption
Simple command-line interface (CLI)
Passwords hidden during input using getpass
No internet or external database required — completely offline and secure
Technologies Used
Python 3.x – Core language for scripting
cryptography – Used for AES encryption (Fernet)
getpass – Hides password input in terminal
json – For storing encrypted data in a structured format
base64, os, hashlib – Utilities for secure key derivation and file handling

 Architectural Highlights & Design Choices
Master Password-Based Access:
Users must enter a master password at runtime. This password is used to derive an AES encryption key via PBKDF2HMAC with a salt.
AES Encryption via Fernet:
All site credentials (username + password) are encrypted using a symmetric key with the Fernet protocol, ensuring high security.
Local Vault File (vault.json):
The password vault is stored as an encrypted JSON file locally. No cloud or third-party storage is involved, reducing attack surfaces.
Modular Design:
The program separates concerns like encryption, file handling, and user interaction into functions for easy updates and debugging.

 Challenges and Solutions
Challenge
Solution
Securely storing passwords
Used cryptography.fernet to encrypt data
Protecting user input
Implemented getpass to hide password entries
Preventing brute force or misuse
Encrypted data using a derived key from a salted master password
First-run file setup
Automatically generates salt and vault file on the first execution


 Future Enhancements
 Search Functionality: Quickly find credentials by site name
 Delete or Update Entries: Allow modifying or removing existing passwords
 Export/Backup: Secure export and import of encrypted vaults
Auto-Lock: Lock the vault after a period of inactivity
Brute Force Protection: Add attempt limits and cooldown timers
Optional Cloud Sync: Encrypted vault sync to cloud (with user consent)
















Expense & Budget Tracker

 1. Project Overview
The Expense & Budget Tracker is a GUI-based personal finance tool built in Python using Tkinter.
Its primary purpose is to help users log daily expenses, set monthly budgets, and analyze their spending habits through clear reports and visual charts.
This project simplifies everyday money management by allowing users to enter expense details, store them locally, and view summaries that promote better financial decision-making.

 2. Key Features
Feature
Description
💵 Add Daily Expense
Users can enter an amount, category (e.g., Food, Travel), and notes
🧾 Monthly Budget
Allows setting a fixed monthly budget and checks how much remains
📊 View Reports
Shows total spent, remaining budget, and breakdown per category
📈 Pie Chart Visualization
Generates a visual summary of expenses using Matplotlib
💾 Persistent Storage
All expense data is stored in a CSV file for portability


 3. Technologies Used

Technology
Purpose
Python 3.x
Core programming language
Tkinter
GUI framework to create forms and buttons
CSV
Lightweight file-based storage for expenses
Matplotlib
To create pie charts and visual summaries
Datetime
For recording current date with each expense


 4. Architectural Highlights & Design Choices
 GUI-Centric Design:
Chose Tkinter for simplicity and wide support with Python.
Designed the app for non-technical users—everything is done via buttons and input fields, no terminal use.
File-Based Data Storage:
CSV was chosen over databases to keep it lightweight, portable, and dependency-free.
Data entries are timestamped, enabling future filtering by date.
 Modular Functional Layout:
UI and logic are separated cleanly.
Each action (add expense, view report, show chart) is encapsulated in a method.
 Visual Reporting:
Used Matplotlib to turn expense data into an easy-to-understand pie chart.
Helps users make informed decisions visually.

 5. Challenges and Solutions

Challenge
Solution
Input validation (e.g., non-numeric values)
Added try-except blocks and error prompts using messagebox
Avoiding UI clutter
Created a compact layout using grid() with proper padding
Data storage with no SQL
Used structured CSV format, readable and easy to manipulate
File not found / CSV missing on first run
Script checks and auto-creates data.csv if missing
User forgets category or input
Required field checks and defaults were added


 6. Future Enhancements

Improvement
Description
 User Accounts
       Add login system to support multiple users
Switch to SQLite or MongoDB
       Replace CSV with a real database for scalability
 Date-Based Filtering
        Allow users to filter by week/month or custom date range
 Export Reports
Export summaries to PDF or Excel for offline access
 Web Version
Rebuild using Flask or Django to make it available online
 Mobile App
Create an Android version using Kivy or React Native









Dynamic Web Scraper + Export to Excel


 Project Description
This project is a dynamic web scraping tool built using Python, Selenium, and OpenPyXL that extracts structured data (book titles and prices) from a paginated website: Books to Scrape. It automates browser interaction, handles dynamic content loading, and seamlessly exports the scraped data to an Excel spreadsheet.
The scraper is easily customizable for other sites and is intended to demonstrate real-world web automation, data extraction, and reporting using modern Python tools.

Features
🔄 Pagination Support: Automatically navigates through multiple pages.
🧠 Dynamic Content Handling: Uses Selenium to interact with JavaScript-rendered content.
📤 Excel Export: Data is saved in a clean Excel file (.xlsx) using OpenPyXL.
🔍 Targeted Data Extraction: Scrapes specific information like title and price.
🧩 Modular Code Structure: Organized functions for scraping, exporting, and handling navigation.
🛠️ Easy Customization: Adaptable for scraping other websites with minimal changes.

 Technologies Used
Tool
Purpose
Python 3.x
Core programming language
Selenium
Web browser automation and scraping
OpenPyXL
Writing data to Excel files
ChromeDriver
Driver for controlling Chrome browser
Google Chrome
Headed browser for rendering web content


Architectural Highlights & Design Choices
Selenium for Rendering Dynamic Content
Chosen over BeautifulSoup because the target website could include JavaScript-rendered elements. Selenium handles real browser interaction.
Pagination Loop
Implemented using a loop that dynamically updates the page URL (page-1.html, page-2.html, etc.), enabling scalable data scraping.
Excel Export via OpenPyXL
A structured and well-supported method to export tabular data into .xlsx format, allowing easy viewing and further processing.
Delays with time.sleep()
Used for simplicity and reliability to wait for pages to load. Can be replaced with WebDriverWait for more advanced handling.

 Challenges and Solutions
Challenge
Solution
Unicode errors from Windows file paths
Used raw strings (r"path\to\file") to fix \u escape errors.
Module errors like No module named selenium
Clarified proper pip install selenium usage within PyCharm/terminal.
Matching ChromeDriver version
Added instructions to match driver with the installed Chrome version.
Dynamic element loading delays
Introduced time.sleep() to allow pages to fully render.


 Future Enhancements
✅ Headless Mode: Run Chrome in headless mode to make the scraper faster and silent.
✅ CSV Export Option: Allow users to choose between .xlsx or .csv formats.
✅ WebDriverWait: Use explicit waits instead of time.sleep() for better control.
✅ Logging System: Add logs to track scraping progress and errors.
✅ User-Agent Rotation / Proxies: Add support for anonymous scraping and anti-blocking measures.
✅ GUI Interface: Build a simple UI using Tkinter or PyQt to allow non-coders to run the tool.






 17.System Resource Monitor
Description
A Python desktop tool that shows **real-time CPU, RAM, Disk, and Network usage** using `psutil` and `matplotlib`. It provides visual insights into system performance through live plots, making it useful for debugging, learning, or general monitoring.

 Features
- Real-time CPU, memory, disk, and network monitoring
- Live graphical display using `matplotlib`
- Auto-refreshes system usage stats
- Lightweight and easy to use

Technologies
- Python 3.x
- psutil
- matplotlib

Getting Started

#Create and activate a virtual environment
```bash
python -m venv .venv

#Windows
.\.venv\Scripts\activate

#macOS/Linux
source .venv/bin/activate
Install dependencies
pip install -r requirements.txt

Run the app
python system_monitor.py
Requirements
psutil
matplotlib





Automated Backup Script with Logging


Description
A Python script that automates the process of backing up files/folders by compressing them into timestamped ZIP archives. It also logs each backup with file names and backup time for reference or audits.

Features
- Automatic ZIP backups of files or folders
- Timestamps added to filenames
- Log file (`backup.log`) with detailed info
- Simple and customizable script


Technologies
- Python 3.x (standard library only)


Getting Started

#Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

No external dependencies required
Run the app
python backup_script.py
Requirements
Uses only built-in Python modules:
os, shutil, zipfile, datetime, logging




 News Aggregator CLI App

Description
A Python CLI app that pulls the latest headlines from [NewsAPI](https://newsapi.org). Users can view top headlines, filter by news category, or search by keywords directly from the terminal.

Features
- View top news headlines
- Filter by categories: business, entertainment, sports, etc.
- Search by custom keyword
- Real-time updates from NewsAPI

Technologies
- Python 3.x
- requests
- NewsAPI

Getting Started

# Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

Install dependencies
pip install -r requirements.txt

Run the app
python news_aggregator.py
Requirements
requests

✅ Also requires a free API key from https://newsapi.org.
 Replace your_api_key_here in the code with your actual API key.






 Bug Tracker Web App

Description
A web-based bug/issue tracking application built with Python and Flask. Users can create, view, update, and delete bugs with assigned priorities, statuses, and assignees. It helps small teams track and manage software bugs efficiently.

Features
- Add, update, and delete bugs
- Assign status (Open, In Progress, Resolved)
- Set priority (High, Medium, Low)
- Assign to specific users
- View all bugs in a table layout

Technologies
- Python 3.x
- Flask
- SQLite (built-in)
- HTML, CSS (for UI)

Getting Started

# Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

Install dependencies
pip install flask

Run the app
python app.py

Then open:
http://127.0.0.1:5000
Requirements
flask

SQLite will be auto-initialized (bug_tracker.db) on first run.


