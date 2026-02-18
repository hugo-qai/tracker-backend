# Software Design Document - Tracker Backend

## Overview
This document defines the core API endpoints for the Tracker Backend system. The system is designed to track items (e.g., tasks, issues) with basic CRUD operations.

## API Endpoints

### 1. List Items
- **Endpoint**: `GET /items`
- **Description**: Retrieve a list of all tracked items.
- **Response**:
  - `200 OK`: JSON array of items.

### 2. Create Item
- **Endpoint**: `POST /items`
- **Description**: Create a new item.
- **Request Body**:
  - `title` (string): Title of the item.
  - `description` (string, optional): Description of the item.
  - `status` (string, default: "open"): Status of the item (e.g., "open", "in-progress", "closed").
- **Response**:
  - `201 Created`: The created item object.

### 3. Get Item
- **Endpoint**: `GET /items/{item_id}`
- **Description**: Retrieve a specific item by its ID.
- **Response**:
  - `200 OK`: The item object.
  - `404 Not Found`: If the item does not exist.

### 4. Update Item
- **Endpoint**: `PUT /items/{item_id}`
- **Description**: Update an existing item.
- **Request Body**:
  - `title` (string, optional)
  - `description` (string, optional)
  - `status` (string, optional)
- **Response**:
  - `200 OK`: The updated item object.
  - `404 Not Found`: If the item does not exist.

### 5. Delete Item
- **Endpoint**: `DELETE /items/{item_id}`
- **Description**: Delete an item.
- **Response**:
  - `204 No Content`: Successful deletion.
  - `404 Not Found`: If the item does not exist.

## Data Model
- **Item**:
  - `id`: Integer (unique identifier)
  - `title`: String
  - `description`: String
  - `status`: String
  - `created_at`: Timestamp
