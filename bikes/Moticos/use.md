# 🏍 Motorcycle Dealership Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Async](https://img.shields.io/badge/async-supported-green.svg)](https://docs.python.org/3/library/asyncio.html)

A simple yet powerful motorcycle dealership management system that handles bike inventory, customer management, and sales transactions asynchronously.

## 🌟 Features

- Motorcycle inventory management
- Customer profile handling
- Asynchronous transaction processing
- Real-time availability checking
- Sales tracking

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/motorcycle-dealership.git
cd motorcycle-dealership
```

2. Run the main program:
```bash
python bikes/Moticos/main.py
```

## 📖 Usage Example

```python
# Create a dealership
bike_dealership = BikeDealership()

# Add a new bike
kawasaki = Bike(101, "Kawasaki", "H2-R", 56.000)
bike_dealership.add_bike(kawasaki)

# Create a customer
customer = Customer(105347132, "John", 25, "john@example.com")

# Process a purchase
if bike_dealership.check_availability(101):
    await process_transaction("John", 56.000)
    customer.buy_bike(kawasaki)
```

## 🔍 Project Structure

```
bikes/Moticos/
├── main.py              # Main application entry point
├── dealership/
│   ├── bikes.py        # Bike and dealership management
│   ├── customer.py     # Customer handling
│   └── processes.py    # Transaction processing
```

## 💡 Class Overview

### `Bike`
- Stores motorcycle information (ID, brand, model, price)
- Tracks availability status

### `BikeDealership`
- Manages motorcycle inventory
- Handles addition/removal of bikes
- Checks bike availability
- Displays inventory

### `Customer`
- Stores customer information
- Manages purchased motorcycles

### `DealershipCustomer`
- Manages customer database
- Handles customer registration
- Retrieves customer information

## ⚡ Async Features

The system uses Python's `asyncio` for handling transactions:
- Simulated payment processing
- Account verification
- Transaction completion

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!
