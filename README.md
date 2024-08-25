# API Banking System

A FastAPI application for managing a banking system, including user authentication, account management, transactions, and advanced reporting features.

## Features

1. **Authentication and Authorization**
   - **User Registration and Login:** Allows users to register and log in with authentication.
   - **Access Tokens:** Uses JWT (JSON Web Tokens) to protect routes and manage user sessions.

2. **User Management**
   - **User Registration:** Register new users.
   - **User Login:** Authenticate users and issue JWT tokens.

3. **Account Management**
   - **Create Account:** Create new bank accounts.
   - **Update Account:** Update account information such as address and phone number.
   - **Close Account:** Functionality to close accounts upon request.

4. **Transaction Management**
   - **Deposit and Withdrawal:** Allow transactions to deposit or withdraw funds.
   - **View Transaction History:** View the history of transactions for an account.

5. **Account Statements**
   - **Generate Detailed Reports:** Allow clients to generate detailed transaction reports for specific periods.
   - **Categorized Statements:** Classify and display transactions by categories such as "Food", "Leisure", etc.

6. **Optimization Features**
   - **Personalized Recommendations:** Offer personalized recommendations for financial products based on transaction history and client profile.
   - **Resource Optimization:** Implement features like loan and investment simulators.

## Directory Structure


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Windows use .venv\Scripts\activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database:**
   - Set up your PostgreSQL or SQLite database as described in `app/core/db.py`.

5. **Run the application:**

    ```bash
    uvicorn app.main:app --reload
    ```

## API Endpoints

### Authentication

- **POST /auth/register/**: Register a new user.
- **POST /auth/login/**: Authenticate a user and get a JWT token.

### Clients

- **POST /clientes/**: Register a new client.
- **PUT /clientes/{cpf}**: Update client details.
- **DELETE /clientes/{cpf}**: Close a client account.

### Accounts

- **POST /contas/**: Create a new account.
- **GET /contas/{cpf}**: Get account details for a client.

### Transactions

- **POST /transacoes/**: Create a new transaction (deposit/withdrawal).

### Categories

- **GET /categorias/extrato-categorias/**: Get categorized transaction reports for a client.

## Running Tests

To run the tests, use:

```bash
pytest
