# CAR MARKETPLACE SERVICE
![Python](https://img.shields.io/badge/Python->=3.10.1,<3.12-blue?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-^0.109.0-dark?style=for-the-badge)
![Supabase](https://img.shields.io/badge/Supabase-black?style=for-the-badge)
![Pydantic](https://img.shields.io/badge/Pydantic-^2.5.3-green?style=for-the-badge)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-^2.0.25-black?style=for-the-badge)
![alembic](https://img.shields.io/badge/alembic-^1.13.1-black?style=for-the-badge)
![dependency-injector](https://img.shields.io/badge/dependencyinjector-^4.41.0-blue?style=for-the-badge)
![uvicorn](https://img.shields.io/badge/uvicorn-^0.27.0.post1-green?style=for-the-badge)


[Introduction](#1-introduction) | [Environment variables](#2-environment-variables) | [Installation](#3-installation) [Flows](#4-flows)
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

# 1. Introduction
Car marketplace is service for selling car.

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

# 2. Environment variables
| **Name**                 | **Type** | **Description**               | **Default value** |
|--------------------------|----------|-------------------------------|-------------------|
| DEBUG                    | Boolean  | Debug mode.                   | False             |
| DB_CONNECTION_LINK       | String   | Link to db connection.        | ---               |
| SUPABASE_SECRET_KEY      | String   | Secret key from Supabase.     | ---               |
| SUPABASE_SECRETE_JWT_KEY | String   | Secret key jwt from Supabase. | ---               |
| SUPABASE_URL             | String   | Url to supabase project       | ---               |
| ENVIRONMENT              | String   | Environment.                  | "local"           |


-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

# 3. Installation
Follow these steps to install and run the service:
1. Install docker and docker-compose
2. Set required environment variables to `web.env` file according to `web_example.env`
3. Run `docker compose -f local.yml up`
4. In container need run `poetry run alembic upgrade head` for upgraded migrations

If you need generate migration run `poetry run alembic revision --autogenerate -m "migration name"`

Be free to ask any help from the contributors.

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

# 4. Flows
## Authentication

### Sign Up

- **Endpoint:** `/auth/sign_up/`
- **Method:** POST
- **Description:** Registers a new user by taking their email and password.
- **Request Body:** `SignUpRequestSchema`
- **Responses:**
  - `200` - Successful registration.
  - `422` - Validation error on input data.

### Sign In

- **Endpoint:** `/auth/sign_in/`
- **Method:** POST
- **Description:** Authenticates a user and returns JWT access and refresh tokens.
- **Request Body:** `SignInRequestSchema`
- **Responses:**
  - `200` - JWT tokens provided in response.
  - `422` - Validation error on input data.

### Refresh Tokens

- **Endpoint:** `/auth/refresh_tokens/`
- **Method:** POST
- **Description:** Refreshes the JWT access and refresh tokens using an existing refresh token.
- **Request Body:** `RefreshRequestSchema`
- **Responses:**
  - `200` - New JWT tokens provided.
  - `422` - Validation error on input data.

## Users

### Get User by ID

- **Endpoint:** `/users/{user_id}/`
- **Method:** GET
- **Security:** Requires JWT authentication.
- **Parameters:** `user_id` - The ID of the user to retrieve.
- **Responses:**
  - `200` - Returns user information.
  - `422` - Validation error.

### Get All Users

- **Endpoint:** `/users/`
- **Method:** GET
- **Security:** Requires JWT authentication.
- **Responses:**
  - `200` - List of users.

## Cars

### View All Cars

- **Endpoint:** `/cars/`
- **Method:** GET
- **Security:** Requires JWT authentication.
- **Responses:**
  - `200` - List of cars.

### Create Car

- **Endpoint:** `/cars/`
- **Method:** POST
- **Security:** Requires JWT authentication.
- **Request Body:** `CreateCarRequestSchema`
- **Responses:**
  - `200` - Car successfully created.
  - `422` - Validation error on input data.

### View Car by ID

- **Endpoint:** `/cars/{car_id}/`
- **Method:** GET
- **Security:** Requires JWT authentication.
- **Parameters:** `car_id` - The ID of the car to retrieve.
- **Responses:**
  - `200` - Returns car information.
  - `422` - Validation error.

### Update Car

- **Endpoint:** `/cars/{car_id}/`
- **Method:** PUT
- **Security:** Requires JWT authentication.
- **Parameters:** `car_id` - The ID of the car to update.
- **Request Body:** `UpdateCarRequestSchema`
- **Responses:**
  - `200` - Car updated successfully.
  - `422` - Validation error on input data.

### Delete Car

- **Endpoint:** `/cars/{car_id}/`
- **Method:** DELETE
- **Security:** Requires JWT authentication.
- **Parameters:** `car_id` - The ID of the car to delete.
- **Responses:**
  - `200` - Car deleted successfully.
  - `422` - Validation error.

## Brands and Series

### View All Brands

- **Endpoint:** `/brand/`
- **Method:** GET
- **Security:** Requires JWT authentication.
- **Responses:**
  - `200` - List of brands.

### Create Brand

- **Endpoint:** `/brand/`
- **Method:** POST
- **Security:** Requires JWT authentication.
- **Request Body:** `CreateBrandRequestSchema`
- **Responses:**
  - `200` - Brand created successfully.
  - `422` - Validation error on input data.

### Update Brand

- **Endpoint:** `/brand/{brand_id}/`
- **Method:** PUT
- **Security:** Requires JWT authentication.
- **Parameters:** `brand_id` - The ID of the brand to update.
- **Request Body:** `UpdateBrandRequestSchema`
- **Responses:**
  - `200` - Brand updated successfully.
  - `422` - Validation error on input data.

### View All Series

- **Endpoint:** `/series/`
- **Method:** GET
- **Security:** Requires JWT authentication.
- **Responses:**
  - `200` - List of series.

### Create Series

- **Endpoint:** `/series/`
- **Method:** POST
- **Security:** Requires JWT authentication.
- **Request Body:** `CreateSeriesRequestSchema`
- **Responses:**
  - `200` - Series created successfully.
  - `422` - Validation error on input data.

### Update Series

- **Endpoint:** `/series/{series_id}/`
- **Method:** PUT
- **Security:** Requires JWT authentication.
- **Parameters:** `series_id` - The ID of the series to update.
- **Request Body:** `UpdateSeriesRequestSchema`
- **Responses:**
  - `200` - Series updated successfully.
  - `422` - Validation error on input data.

## Security

- All secured endpoints require a JWT token provided via the `Authorization: Bearer <token>` header.
- Security schema is defined under `JWTVerificationService`.

For detailed field definitions and requirements, refer to the schema documentation linked in each endpoint section.

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
