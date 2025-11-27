# Tests automatizados - Mayte Anahi Anchapanta Vinueza
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test de la ruta principal"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['estudiante'] == 'Mayte Anahi Anchapanta Vinueza'
    assert data['segundo_apellido'] == 'Vinueza'
    assert data['version'] == '1.0.5'

def test_health(client):
    """Test del endpoint de salud"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert data['estudiante'] == 'Vinueza'

def test_ia_hola(client):
    """Test del chatbot IA con saludo"""
    response = client.post('/ia', json={'mensaje': 'hola'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'respuesta' in data
    assert data['estudiante'] == 'Mayte Vinueza'

def test_ia_quien_eres(client):
    """Test del chatbot IA preguntando quién es"""
    response = client.post('/ia', json={'mensaje': 'quien eres'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'Mayte' in data['respuesta']