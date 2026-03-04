import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client

def test_login_correcto(client):
    """PRUEBA UNITARIA: Login con credenciales válidas."""
    response = client.post('/login', data={
        'email': 'alumno@colegio.es',
        'password': 'alumno123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Panel del alumno" in response.data
    print("✅ Login correcto: Dashboard cargado")
