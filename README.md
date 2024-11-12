# Simple Calculator Project

A simple calculator application built using **Python** and **SQLite**. The calculator performs basic arithmetic operations (addition, subtraction, multiplication, division) and stores the results in an SQLite database for later retrieval.

## Features

- **Basic Operations**: Supports addition, subtraction, multiplication, and division.
- **View Results**: Users can view the history of previous calculations stored in the database.
- **Persistent Storage**: All calculation results are saved in an SQLite database.

## Project Structure


## Getting Started

### Prerequisites

- Python 3.x
- SQLite (comes pre-installed with Python)

### Installation Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/SimpleCalculator.git
   cd SimpleCalculator
python app.py
Use the Calculator:

Select an operation (addition, subtraction, multiplication, or division).
Input the numbers for the operation.
View the result immediately.
Optionally, view the history of previous results by selecting the "View Results" option.
Exit: Choose the exit option to terminate the program.

Database Structure
The SQLite database contains a table called results with the following fields:

id: Integer (Primary Key)
operation: Text (Operation performed, e.g., "5 + 3")
result: Real (Result of the operation)
How It Works
The Python script app.py handles the logic of performing arithmetic operations and storing results.
The results are stored in an SQLite database, ensuring that they persist across program runs.
Users interact with the calculator through a simple text-based interface in the terminal.
License
This project is open-source and available under the MIT License.
