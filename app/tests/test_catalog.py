import json
import logging
from app import create_app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_get_prizes():
    app = create_app()
    app.testing = True
    client = app.test_client()

    # Test valid request
    catalog_id = 1
    data = {'filter': {'id': 1}, 'pagination': {'page': 1, 'per_page': 10}}
    response = client.get(f'/api/catalogs/{catalog_id}/prizes', json=data)
    result = json.loads(response.data)

    assert response.status_code == 200
    assert 'total' in result
    assert 'prizes' in result
    logger.info("Test for valid request passed.")

    # Test invalid filter parameter
    data = {'filter': {'id': "text not valid"}, 'pagination': {'page': 1, 'per_page': 10}}
    response = client.get(f'/api/catalogs/{catalog_id}/prizes', json=data)
    assert response.status_code == 400
    logger.info("Test for invalid filter parameter passed.")

    # Test invalid pagination parameter
    data = {'pagination': {'page': "page not valid", 'per_page': 10}}
    response = client.get(f'/api/catalogs/{catalog_id}/prizes', json=data)
    assert response.status_code == 400
    logger.info("Test for invalid pagination parameter passed.")

    # Test invalid catalog_id parameter
    data = {'pagination': {'page': "page not valid", 'per_page': 10}}
    catalog_id = "string not valid"
    response = client.get(f'/api/catalogs/{catalog_id}/prizes', json=data)
    assert response.status_code == 404
    logger.info("Test for invalid catalog_id parameter passed.")

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "tests"])
