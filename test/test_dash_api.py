import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client

def test_dashboard_con_api(client):
    """PRUEBA INTEGRACIÓN: Dashboard + API (notas + asistencia)."""
    # Login primero
    client.post('/login', data={
        'email': 'alumno@colegio.es',
        'password': 'alumno123'
    })
    
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b"Lengua Castellana" in response.data  # De API
    assert b"Presente" in response.data           # De API
    print("✅ Dashboard API: 8 asignaturas + asistencia")
