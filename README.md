# 🛒 OnlineFakerStore -- API Automation Testing Framework

This project is an **API Automation Testing Framework** built to test
the public **FakeStore API**, which provides pseudo-real e-commerce data
for products, carts, users, and authentication.\
It is designed using **Python, Pytest, and Requests** following
industry-standard automation architecture.

The project is ideal for: - Learning **API automation** - Practicing
**real-world e-commerce API testing** - Demonstrating **framework design
for interviews & portfolios**

------------------------------------------------------------------------

## 🔗 FakeStore API Reference

FakeStore API is a free public REST API that provides realistic shopping
data without requiring any backend setup.

Official API Base URL:

    https://fakestoreapi.com

------------------------------------------------------------------------

## 🚀 Why This Project?

When building or testing an e-commerce system, realistic test data is
essential. Instead of using dummy "lorem ipsum" data, **FakeStore API
provides structured real-like data** such as:

-   ✅ Products
-   ✅ Shopping Carts
-   ✅ Users
-   ✅ Authentication Tokens

This project automates all these APIs using a **scalable Pytest
framework**.

------------------------------------------------------------------------

## 🧰 Tech Stack Used

-   **Programming Language:** Python\
-   **Test Framework:** Pytest\
-   **API Library:** Requests\
-   **Test Data:** Faker\
-   **Reporting:** Allure Reports *(if enabled)*\
-   **Design Pattern:** Modular Framework\
-   **Version Control:** Git & GitHub

------------------------------------------------------------------------

## 📂 Project Features

✔ Data-driven API Testing\
✔ Modular Framework Structure\
✔ Token-based Authentication Handling\
✔ CRUD API Validations\
✔ Status Code & Response Validation\
✔ Reusable Payloads\
✔ Reporting Ready\
✔ CI/CD Friendly

------------------------------------------------------------------------

## 📦 Main API Resources Covered

### ✅ Products API

    /products

  Operation                  Endpoint
  -------------------------- ---------------------------------
  Get all products           `/products`
  Get single product         `/products/{id}`
  Add new product            `/products`
  Update product             `/products/{id}`
  Delete product             `/products/{id}`
  Get categories             `/products/categories`
  Get products by category   `/products/category/{category}`
  Sort & limit               `/products?limit=5&sort=desc`

------------------------------------------------------------------------

### ✅ Carts API

    /carts

  Operation           Endpoint
  ------------------- --------------------------------------------------
  Get all carts       `/carts`
  Get single cart     `/carts/{id}`
  Get carts by user   `/carts/user/{userId}`
  Add new cart        `/carts`
  Update cart         `/carts/{id}`
  Delete cart         `/carts/{id}`
  Filter by date      `/carts?startdate=YYYY-MM-DD&enddate=YYYY-MM-DD`

------------------------------------------------------------------------

### ✅ Users API

    /users

  Operation         Endpoint
  ----------------- ----------------------------
  Get all users     `/users`
  Get single user   `/users/{id}`
  Create user       `/users`
  Update user       `/users/{id}`
  Delete user       `/users/{id}`
  Sort & limit      `/users?limit=5&sort=desc`

------------------------------------------------------------------------

### ✅ Authentication API

    /auth/login

Used to generate authentication tokens for secured requests.

------------------------------------------------------------------------

## ⚠ Important API Notes

-   POST requests return a **fake ID**
-   PUT/PATCH requests **do not update data permanently**
-   DELETE requests **do not remove data from server**
-   API is only for **testing & learning purposes**

------------------------------------------------------------------------

## 🛠 Installation & Setup

### 1. Clone the Repository

    git clone https://github.com/your-username/OnlineFakerStore.git
    cd OnlineFakerStore

### 2. Create and Activate Virtual Environment

    python -m venv venv
    venv\Scripts\activate

### 3. Install Dependencies

    pip install -r requirements.txt

------------------------------------------------------------------------

## ▶ Running Tests

    pytest -v

Run with Allure Report:

    pytest --alluredir=allure-results
    allure serve allure-results

------------------------------------------------------------------------

## 📊 Framework Structure

    OnlineFakerStore/
    │
    ├── testCases/
    ├── routes/
    ├── payloads/
    ├── utils/
    ├── conftest.py
    ├── pytest.ini
    ├── requirements.txt
    └── run.bat

------------------------------------------------------------------------

## 🎯 Learning Outcomes

-   API Automation using Pytest
-   Real-world API testing exposure
-   Framework design knowledge
-   Token handling
-   Reporting & CI/CD readiness

------------------------------------------------------------------------

## 🤝 Author

Your Name\
Automation Tester \| QA Engineer

------------------------------------------------------------------------

⭐ If you like this project, please star the repository!
