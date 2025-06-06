# FastAPI MVC Blog

A FastAPI-based web application following the *MVC design pattern* with *MySQL integration* for user authentication and post management. This project demonstrates token-based authentication, field validation, in-memory caching, and efficient database handling using SQLAlchemy and Pydantic.

---

## Features

- *Modular MVC Design*:
  - Separate layers for routing, business logic, and database interactions.
  
- *Endpoints*:
  - *Signup Endpoint*: User registration with email and password.
  - *Login Endpoint*: User authentication and token generation.
  - *AddPost Endpoint*: Create a new post with token authentication.
  - *GetPosts Endpoint*: Retrieve all posts for a user with caching.
  - *DeletePost Endpoint*: Remove a post using token authentication.

- *Database Integration*:
  - MySQL handled via SQLAlchemy ORM.
  - Efficient query handling and dependency injection for database sessions.

- *Validation*:
  - Extensive type validation using Pydantic models.
  - Payload size validation for AddPost endpoint.

- *Caching*:
  - In-memory caching for GetPosts endpoint (TTL: 5 minutes).

---

## Technologies Used

- *Python*: Backend programming language.
- *FastAPI*: Framework for building APIs.
- *SQLAlchemy*: ORM for database interaction.
- *MySQL*: Relational database.
- *Pydantic*: Data validation and parsing.
- *CacheTools*: For response caching.

---

## Project Structure

The project follows the *MVC* design pattern:
