# Menu Ordering System

## Overview

Just having fun while learning Python and wanted to create this where you receive an Iced Americano no matter what you order. 

The Menu Ordering System is a simple command-line application that allows users to view a menu, place an order, and decide if they want to order more. The application reads menu data from a CSV file and uses the `tabulate` library to format and display the menu in a grid format.

## Features

- Display a menu from a CSV file.
- Allow users to place an order.
- Confirm the order and offer the option to order more or exit.

## Requirements

- Python 3.x
- `tabulate` library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/menu-ordering-system.git
    cd menu-ordering-system
    ```

2. **Install the required library**:
    ```bash
    pip install tabulate
    ```

## Usage

1. **Prepare the menu CSV file**: Create a CSV file named `menu.csv` with the menu items. The first row should contain headers.

2. **Run the script**:
    ```bash
    python main.py
    ```

3. **Follow the prompts**:
    - Enter `y` to view the menu.
    - After viewing the menu, place an order.
    - You will receive a confirmation for your order and be asked if you want to order more.

## Code Explanation

- **`main()`**: The entry point of the program. It prompts the user to see the menu and handles the flow of the application.
- **`order_item()`**: Manages the ordering process, including confirming the order and asking if the user wants to order something else.
- **`menu(filename)`**: Reads the menu from a CSV file and displays it in a formatted grid using the `tabulate` library.

## Example
