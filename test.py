import azure.functions as func
import pytest
from unittest.mock import Mock
from function_app import app  # Import the app instance

def test_main():
    # Create a mock HTTP request
    req = Mock(spec=func.HttpRequest)
    req.params = {}
    req.get_json = Mock(return_value={})

    # Retrieve the registered function by route name
    function_handler = app.get_functions()["http_trigger1"]

    # Call the function with the mock request
    response = function_handler(req)

    # Validate the response
    assert response.status_code == 200
    assert response.get_body().decode() == "Hello, Prof Aagam!, Assignment3 Completed 8934575!"
