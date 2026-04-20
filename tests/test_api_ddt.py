import pytest
import requests
import json
import os
import allure  # <-- 1. Import library allure

JSON_PATH = os.path.join(os.path.dirname(__file__), 'test_data', 'tasks.json')

def load_test_data():
    with open(JSON_PATH, 'r') as f:
        return json.load(f)

BASE_URL = "http://localhost:8000"

# 2. Tambahkan anotasi Feature dan Story di atas fungsi test
@allure.feature("Task API Management")
@allure.story("Data-Driven Task Creation")
@pytest.mark.parametrize("test_case", load_test_data())
def test_create_task_ddt(test_case):
    """
    Menjalankan pengujian API pembuatan tugas berdasarkan data dari JSON.
    """
    # 3. (Opsional tapi keren) Jadikan nama test dinamis di laporan
    allure.dynamic.title(f"Test: {test_case['test_name']}")
    
    url = f"{BASE_URL}/api/tasks"
    payload = test_case['payload']
    expected_status = test_case['expected_status']
    
    response = requests.post(url, json=payload)
    
    assert response.status_code == expected_status, \
        f"Gagal pada {test_case['test_name']}. Harusnya {expected_status} tapi dapat {response.status_code}"