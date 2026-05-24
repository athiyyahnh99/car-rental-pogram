# Python CRUD Application Car Rental Management

A comprehensive Python application for managing car rental data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to car rental businesses by providing a streamlined solution for managing vehicle inventory and availability. Efficient car rental management ensures vehicle availability, minimizes booking conflicts, and optimizes fleet utilization.

**Benefits:**

* Improved fleet accuracy: Real-time vehicle data reduces discrepancies and ensures informed decision-making.
* Enhanced booking fulfillment: Accurate availability status enables efficient rental management and customer satisfaction.
* Reduced operational costs: Optimized fleet management minimizes idle vehicles and prevents overbooking.
* Improved availability forecasting: Data-driven insights support better forecasting of vehicle demand.

**Target Users:**

This application is designed for rental managers and staff within a car rental business to manage vehicle inventory, track availability, and maintain accurate fleet data.

## Features

* **Create:**
    * Add new vehicle entries to the rental system, specifying details like brand (merk), model, license plate, daily rate, and availability status.
    * Implement validation rules to ensure data accuracy (e.g., unique license plate, valid license plate format, positive daily rate).
* **Read:**
    * Search and retrieve specific vehicle information by brand or model name.
    * Display all vehicles with filter options (available only or currently rented).
    * Display comprehensive vehicle details in a user-friendly table format, including availability status and daily rate.
* **Update:**
    * Modify existing vehicle information to reflect changes in availability, pricing, or vehicle details.
    * Support searching vehicle by brand, model, or license plate before updating.
    * Provide clear confirmation messages for update success or cancellation, with rollback if cancelled.
* **Delete:**
    * Allow for the removal of vehicles from the fleet with index-based selection.
    * Requires confirmation before permanent deletion to prevent accidental data loss.

## Installation

1. **Prerequisites:**
    * Python version 3.7 or later
    * Built-in libraries only:
        * `re` (regular expressions — included in Python standard library)

2. **Installation:**
    ```bash
    git clone https://github.com/athiyyahnh99/car-rental-pogram.git
    cd car-rental-crud
    ```

3. **No additional setup required.** The application uses an in-memory list as the data store. Data resets on every program restart.

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new vehicle to the fleet, providing details like brand, model, license plate, daily rate, and availability.
    * **Read:** View all vehicles or search by brand/model name. Filter by availability status.
    * **Update:** Search for a vehicle by brand, model, or license plate, then select which field to modify.
    * **Delete:** Select a vehicle by index number to remove it from the fleet (with confirmation).

## Data Model

* **car_data:**
    * `id` (Integer): Unique identifier for each vehicle, auto-incremented.
    * `merk` (String): Brand of the vehicle (e.g., Toyota, Honda).
    * `model` (String): Model name of the vehicle (e.g., Avanza, Brio).
    * `license_plate` (String, Unique): License plate number in format `AA 1234 BBB`.
    * `daily_rate` (Integer): Rental price per day in Indonesian Rupiah (IDR).
    * `availability` (Boolean): `True` if the vehicle is available for rent, `False` if currently rented.

## Validation Rules

* `license_plate` must follow the format: 1-2 letters, space, 1-4 digits, space, 1-3 letters (e.g., `B 1234 ABC`).
* `license_plate` must be unique across all vehicles.
* `daily_rate` must be a positive integer.
* `merk` and `model` cannot be empty.
* Delete and update index input must be a valid number within the list range.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to [your_email] or submit an issue if you encounter any problems or have suggestions for improvements.

