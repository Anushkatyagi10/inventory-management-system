#  Inventory Management System (Python)

A **console-based Inventory Management System** built using **Python and Object-Oriented Programming (OOP)** principles.
The system allows users to manage products, track stock levels, place orders, cancel orders, and calculate total order cost.


🚀 Features

* ➕ Add new products to inventory
* 📋 View all available products
* 🛒 Place orders for products
* ❌ Cancel existing orders
* 📦 Automatic stock update after order placement or cancellation
* 💰 Automatic total bill calculation
* 🔍 View all orders with status



🛠 Tech Stack

Language: Python
Concepts Used:

  * Object-Oriented Programming (OOP)
  * Classes & Objects
  * Menu-driven CLI interface



📂 Project Structure

```
inventory-management-system
│
├── README.md
├── inventory_sys.py          # Main file to run the program
│
└── inventory/
    ├── __init__.py           # Makes the folder a Python package
    ├── product.py            # Product class (id, name, price, stock)
    ├── inventory.py          # Inventory management logic
    └── order.py              # Order handling (place/cancel order)
```



⚙️ How to Run the Project

 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/inventory-management-system.git
```

 2️⃣ Navigate to the Project Folder

```
cd inventory-management-system
```

 3️⃣ Run the Program

```
python inventory_system.py
```



 📸 Example Menu

```
=== Inventory Management System ===
1. Add Product
2. Place Order
3. Cancel Order
4. Exit
```

---

💡 Example Workflow

1. Add a product with ID, name, price, and stock.
2. Place an order for a product.
3. The system automatically reduces stock.
4. Cancel an order if needed.
5. Stock is restored after cancellation.



## 🧠 Key Learning Outcomes

* Implementing **OOP concepts in Python**
* Managing application state using **data structures**
* Designing a **menu-driven CLI application**
* Building a **real-world mini project**





👩‍💻 Author

**Anushka Tyagi**

If you like this project, feel free to ⭐ the repository.

