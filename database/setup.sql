-- Create the database
CREATE DATABASE IF NOT EXISTS management;

-- Use the database
USE management;

-- Create customer table
CREATE TABLE IF NOT EXISTS customer (
    ref VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    `id proof type` VARCHAR(50),
    `id no` VARCHAR(50) NOT NULL,
    gender VARCHAR(10),
    state VARCHAR(50),
    pincode VARCHAR(10),
    mobile VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    nationality VARCHAR(50)
);

-- Create room table
CREATE TABLE IF NOT EXISTS room (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    floor VARCHAR(5),
    room_no VARCHAR(5) UNIQUE,
    room_type VARCHAR(50),
    price DECIMAL(10,2),
    status ENUM('Available', 'Occupied', 'Maintenance') DEFAULT 'Available'
);

-- Create booking table to link customers with rooms
CREATE TABLE IF NOT EXISTS booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_ref VARCHAR(20),
    room_id INT,
    check_in DATETIME,
    check_out DATETIME,
    days INT,
    total_cost DECIMAL(10,2),
    payment_status ENUM('Pending', 'Partial', 'Complete') DEFAULT 'Pending',
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_ref) REFERENCES customer(ref),
    FOREIGN KEY (room_id) REFERENCES room(room_id)
);

-- Create payment table
CREATE TABLE IF NOT EXISTS payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    amount DECIMAL(10,2),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    FOREIGN KEY (booking_id) REFERENCES booking(booking_id)
);

-- Create staff table
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50),
    mobile VARCHAR(20),
    email VARCHAR(100),
    address VARCHAR(255),
    salary DECIMAL(10,2),
    join_date DATE
);

-- Create services table for additional hotel services
CREATE TABLE IF NOT EXISTS services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100),
    cost DECIMAL(10,2),
    description VARCHAR(255)
);

-- Create booking_services junction table
CREATE TABLE IF NOT EXISTS booking_services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    service_id INT,
    quantity INT DEFAULT 1,
    service_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES booking(booking_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Insert some sample room data
INSERT INTO room (floor, room_no, room_type, price) VALUES
('1', '101', 'Single', 1000.00),
('1', '102', 'Single', 1000.00),
('1', '103', 'Double', 1800.00),
('1', '104', 'Double', 1800.00),
('2', '201', 'Single', 1200.00),
('2', '202', 'Single', 1200.00),
('2', '203', 'Double', 2000.00),
('2', '204', 'Suite', 3500.00),
('3', '301', 'Suite', 4000.00),
('3', '302', 'Suite', 4000.00);

-- Insert some sample services
INSERT INTO services (service_name, cost, description) VALUES
('Room Service', 500.00, 'Food delivery to room'),
('Laundry', 300.00, 'Laundry service per load'),
('Spa', 1500.00, 'Full body spa treatment'),
('Airport Pickup', 800.00, 'Pickup service from airport'),
('Breakfast', 200.00, 'Breakfast buffet per person');

-- Create hotel_info table for system settings
CREATE TABLE IF NOT EXISTS hotel_info (
    id INT PRIMARY KEY DEFAULT 1,
    hotel_name VARCHAR(100),
    address VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(100),
    website VARCHAR(100),
    tax_rate DECIMAL(5,2) DEFAULT 18.00,
    check_in_time TIME DEFAULT '14:00:00',
    check_out_time TIME DEFAULT '12:00:00',
    logo_path VARCHAR(255),
    footer_text VARCHAR(255)
);

-- Insert default hotel info
INSERT INTO hotel_info (hotel_name, address, phone, email, website, tax_rate)
VALUES ('Luxury Hotel', '123 Main Street, City, Country', '+1234567890', 'info@luxuryhotel.com', 'www.luxuryhotel.com', 18.00);

-- Create users table for system login
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    role ENUM('admin', 'manager', 'receptionist', 'staff') DEFAULT 'staff',
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert admin user (password should be hashed in actual implementation)
INSERT INTO users (username, password, role)
VALUES ('admin', 'admin123', 'admin');