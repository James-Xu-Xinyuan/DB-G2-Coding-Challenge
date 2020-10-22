from flask import Response 
import requests

def test_get_data_from_data_gen():
    
    # arrange
    expResult = 200 
    result = None

    # act
    r = requests.get('http://www.google.com')
    result = r.status_code

    # assert 
    assert result == expResult 


def test_print_hello_world():

    # arrange
    expResult = "Hello World!"
    result = None

    # act
    r = requests.get("http://localhost:8080/printHelloWorldData")
    result = r.content.decode("UTF-8")

    # assert 
    assert result == expResult 

 
def test_Response():

    # arrange
    expResult = 200
    result = None

    # act 
    r = requests.get("http://localhost:8080/printHelloWorldData")
    result = Response(r.iter_content(chunk_size=1), mimetype="text/json")
    
    # assert 
    assert result.status_code == expResult 



