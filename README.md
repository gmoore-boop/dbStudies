# Python + SQLite Roadmap

Hello! 

 This repository documents my study of database and backend development with Python, targeting the mastering of this subject.

 I designed this roadmap with AI to create a structured, progressive learning path that starts with SQLite fundamentals and gradually advances toward modern backend development using technologies such as SQLAlchemy, FastAPI, Docker, Redis, and production-ready software. 

 I'll be implementing every exercise myself, reviewing my solutions with AI, official documentation, and other learning resources. 

 If you're learning Python backend development as well, feel free to follow along, solve the exercises yourself, compare approaches, or use this repository for your own studies.

## Learning Objectives

By completing this roadmap, I will learn how to:

- Build and manage SQLite databases with Python
- Design normalized relational database schemas
- Perform complete CRUD operations
- Write efficient and secure SQL queries
- Work with joins, aggregations, filtering, and pagination
- Implement transactions and rollback mechanisms
- Optimize database performance
- Import, export, and back up data
- Apply SQLAlchemy Core and ORM
- Manage database migrations with Alembic
- Write automated tests for database applications
- Build REST APIs with FastAPI
- Implement authentication and authorization
- Integrate Redis caching
- Containerize applications using Docker
- Apply professional software architecture patterns
- Prepare applications for production environments

---

## Technologies

- Python
- SQLite
- SQL
- `sqlite3`
- SQLAlchemy Core
- SQLAlchemy ORM
- Alembic
- FastAPI
- Docker
- Redis
- Pandas
- JWT Authentication
- Async SQLAlchemy
- Automated Testing
- Environment Variables
- Repository Pattern
- Unit of Work Pattern
- Layered Architecture
- RBAC (Role-Based Access Control)

---

## Repository Structure

```text
.
├── level-1/
│   ├── exercise-01/
│   ├── exercise-02/
│   └── ...
├── level-2/
│   └── ...
├── level-3/
│   └── ...
├── level-4/
│   └── ...
└── README.md
```

---

# Roadmap

## Level 1 — Python & SQLite Fundamentals

This level introduces the core concepts of database programming with Python. I'll learn how to create and connect to SQLite databases, model relationships, perform CRUD operations, write secure SQL queries, organize your project, and build a complete command-line application.

| # | Exercise | Description |
|---|----------|-------------|
| 1 | Create the Database | Create a SQLite database named `library.db` and establish a connection using Python's built-in `sqlite3` module. | 
| 2 | Create Tables | Create the `authors` and `books` tables with appropriate primary keys and foreign key relationships. | 
| 3 | Basic Data Insertion | Insert multiple authors and books into the database using SQL statements executed from Python. | 
| 4 | Simple Queries | Retrieve and display all books in a clear and organized format. | 
| 5 | Filtered Queries | Prompt the user for an author's name and display only the books written by that author. |
| 6 | Update Records | Modify the title of an existing book. | 
| 7 | Delete Records | Remove a book from the database using its ID. | 
| 8 | Complete CRUD | Combine all previous operations into an interactive command-line menu. | 
| 9 | Exception Handling | Handle connection failures, invalid queries, and incorrect user input gracefully. |
| 10 | Parameterized Queries | Refactor every query that accepts external input to use parameterized SQL statements. |
| 11 | JOIN Operations | Display each book alongside its corresponding author using SQL joins. |
| 12 | Aggregate Queries | Calculate the number of books per author, identify the author with the most books, and display the total number of books. |
| 13 | Project Organization | Organize the application into separate modules for connections, queries, interface, and models. |
| 14 | Data Persistence | Ensure that all data remains available across multiple executions of the application. |
| 15 | Final Project | Build a complete command-line Library Management System using everything learned throughout this level. 
---

## Level 2 — SQL Modeling & Database Design

In this stage, I'll move beyond basic CRUD operations and explore the core principles of relational database design. I'll learn how to model real-world systems, enforce data integrity, optimize queries, work with transactions, and handle data import, export, and backup—essential skills for building reliable database applications.

| # | Exercise | Description |
|---|----------|-------------|
| 16 | Database Modeling | Design a relational database for an online store containing customers, products, orders, and order items. |
| 17 | Referential Integrity | Define and enforce all foreign key relationships to maintain data consistency. |
| 18 | Transactions | Implement a complete purchase workflow using SQL transactions. |
| 19 | Rollback | Simulate a failed purchase and roll back the entire transaction. |
| 20 | Batch Inserts | Insert thousands of products efficiently using batch operations. |
| 21 | Pagination | Retrieve data using `LIMIT` and `OFFSET` for paginated results. |
| 22 | Dynamic Search | Build queries with optional filters based on user input. |
| 23 | Indexes | Create indexes and compare query performance before and after optimization. |
| 24 | Views | Create SQL views to simplify frequently executed queries. |
| 25 | Triggers | Implement triggers to automatically log changes in an audit table. |
| 26 | Custom SQL Functions | Register Python functions with `sqlite3.create_function()` and use them in SQL queries. |
| 27 | CSV Import | Import CSV data into SQLite using Pandas. |
| 28 | Data Export | Export query results to CSV and Excel files. |
| 29 | Database Backup | Build a backup system for the SQLite database. |
| 30 | Final Project | Develop a complete Sales Management System. |

---

## Level 3 — Professional Backend Architecture

This level focuses on writing maintainable, scalable, and production-quality code. I'll transition from the standard `sqlite3` module to SQLAlchemy, apply widely adopted architectural patterns, automate database migrations, write tests, optimize performance, and package your application with Docker.

| # | Exercise | Description |
|---|----------|-------------|
| 31 | SQLAlchemy Core | Refactor an existing project using SQLAlchemy Core. |
| 32 | SQLAlchemy ORM | Model the database using SQLAlchemy's Object Relational Mapper (ORM). |
| 33 | Relationships | Implement one-to-many, many-to-many, and one-to-one relationships using the ORM. |
| 34 | Repository Pattern | Introduce a Repository layer to encapsulate data access logic. |
| 35 | Unit of Work | Implement the Unit of Work pattern for transaction management. |
| 36 | Alembic Migrations | Manage database schema evolution with Alembic. |
| 37 | Connection Management | Build a reusable layer responsible for creating, reusing, and safely closing database connections. |
| 38 | Logging | Automatically log every SQL query executed by the application. |
| 39 | Automated Testing | Write automated tests covering all database operations. |
| 40 | In-Memory Database | Use SQLite's `:memory:` database to speed up automated tests. |
| 41 | Docker | Containerize and run the application using Docker. |
| 42 | Configuration | Configure the application using environment variables. |
| 43 | Performance Optimization | Analyze and optimize queries with `EXPLAIN QUERY PLAN`. |
| 44 | Concurrency | Simulate concurrent users and handle conflicting database operations safely. |
| 45 | Final Project | Build a complete e-commerce backend using SQLAlchemy, Alembic, Docker, and automated testing. |

---

## Level 4 — Modern Production Backend Development

The final stage brings together everything I've learned to build production-ready backend applications. I'll develop secure REST APIs, implement authentication and authorization, integrate caching, improve observability, and structure my project following modern software engineering practices.

| # | Exercise | Description |
|---|----------|-------------|
| 46 | REST API | Build a RESTful API with FastAPI integrated with SQLite. |
| 47 | Advanced ORM Queries | Implement complex database queries using SQLAlchemy ORM. |
| 48 | Pagination & Filtering | Add pagination, sorting, and advanced filtering to the API. |
| 49 | Soft Delete | Implement logical deletion across all entities. |
| 50 | Auditing | Record and track every significant change made by users. |
| 51 | Concurrency Control | Prevent conflicts during simultaneous database updates. |
| 52 | Redis Cache | Integrate Redis to reduce repetitive database queries. |
| 53 | Asynchronous Database | Refactor the application to use SQLAlchemy's `AsyncSession`. |
| 54 | JWT Authentication | Implement user authentication using JSON Web Tokens (JWT). |
| 55 | Role-Based Access Control | Build a complete RBAC system with users, roles, and permissions. |
| 56 | Automated Backup | Implement automatic database backups and restoration. |
| 57 | Observability | Monitor errors, slow queries, and application performance. |
| 58 | Scalability | Refactor the application to support future migration to PostgreSQL or MySQL with minimal changes. |
| 59 | Layered Architecture | Organize the project into controllers, services, repositories, models, and schemas. |
| 60 | Professional Final Project | Develop a complete business management API featuring authentication, inventory, payments, auditing, automated testing, Docker, Redis, automatic API documentation, layered architecture, and database portability. |