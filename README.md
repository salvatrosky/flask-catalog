# Flask Catalog API

Welcome to Flask Catalog API, a simple API for managing catalogs and prizes.

## Getting Started

To run this application using Docker, follow these steps:

### Prerequisites

Make sure you have Docker installed on your machine.

### Build the Docker Image

Build the Docker image with the following command:

```bash
docker build -t flask-catalog .
```

This command creates a Docker image named flask-catalog based on the Dockerfile in the project directory.

### Run the Docker container

Run the Docker container with the following command:

```bash
docker run -p 5000:5000 -v $(pwd):/app flask-catalog
```

This command creates a Docker image named flask-catalog based on the Dockerfile in the project directory.

### Access the Application

Once the container is running, the Flask Catalog API will be accessible at http://localhost:5000.

### Endpoint

#### Get Prizes for a Catalog

To retrieve prizes for a catalog, make a GET request to the following endpoint:

```http
GET http://localhost:5000/api/catalogs/{catalog_id}/prizes
```

**Request Body:**

```json
{
    "filter": {
        "id": 1,
        "description": "text"
    },
    "pagination": {
        "page": 1,
        "per_page": 10
    }
}
```

- `catalog_id` (path parameter): ID of the catalog (required).
- `filter` (optional): Filter prizes based on ID and description.
- `pagination` (optional): Specify the page number and items per page.