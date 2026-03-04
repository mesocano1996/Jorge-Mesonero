import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client

def test_api_sin_token(client):
    """PRUEBA: Frontend no expone rutas API internas."""
    response = client.get('/api/notas/alumno@colegio.es')
    
    assert response.status_code == 404  # Frontend NO tiene /api/
    print("✅ Frontend protegido: 404 en rutas API")
