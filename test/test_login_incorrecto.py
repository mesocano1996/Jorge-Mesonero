import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client

def test_login_incorrecto(client):
    """PRUEBA UNITARIA: Login con credenciales invalidas."""
    response = client.post('/login', data={
        'email': 'falso@noexiste.es',
        'password': 'mal'
    }, follow_redirects=True)
    
    # Busca el alert de error (genérico)
    assert b'alert-danger' in response.data
    assert b'btn-close' in response.data  # Cierre del alert
    print("✅ Login incorrecto: Alert danger detectado")
