import requests
import json

def test_api():
    base_url = "http://localhost:8021"
    
    # Test 1: Check if API is running
    print("🔍 Проверка доступности API...")
    try:
        response = requests.get(f"{base_url}/users/")
        if response.status_code == 200:
            print("✅ API работает!")
            print(f"📋 Текущие студенты: {response.json()}")
        else:
            print(f"❌ API вернул статус: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Ошибка подключения к API: {e}")
        return
    
    # Test 2: Add a test student
    print("\n👤 Добавление тестового студента...")
    test_student = {"name": "Иван Петров"}
    try:
        response = requests.post(
            f"{base_url}/users/",
            json=test_student,
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            student = response.json()
            print(f"✅ Студент добавлен: {student['name']} (ID: {student['id']})")
        else:
            print(f"❌ Ошибка при добавлении: {response.status_code}")
            print(f"Ответ: {response.text}")
    except Exception as e:
        print(f"❌ Ошибка при добавлении студента: {e}")
    
    # Test 3: Add more students
    print("\n👥 Добавление дополнительных студентов...")
    students = [
        {"name": "Мария Сидорова"},
        {"name": "Алексей Козлов"},
        {"name": "Анна Волкова"}
    ]
    
    for student_data in students:
        try:
            response = requests.post(
                f"{base_url}/users/",
                json=student_data,
                headers={"Content-Type": "application/json"}
            )
            if response.status_code == 200:
                student = response.json()
                print(f"✅ Добавлен: {student['name']} (ID: {student['id']})")
            else:
                print(f"❌ Ошибка при добавлении {student_data['name']}: {response.status_code}")
        except Exception as e:
            print(f"❌ Ошибка: {e}")
    
    # Test 4: Get all students
    print("\n📋 Получение всех студентов...")
    try:
        response = requests.get(f"{base_url}/users/")
        if response.status_code == 200:
            students = response.json()
            print(f"📊 Всего студентов: {len(students)}")
            for student in students:
                print(f"  - {student['name']} (ID: {student['id']})")
        else:
            print(f"❌ Ошибка при получении списка: {response.status_code}")
    except Exception as e:
        print(f"❌ Ошибка при получении списка: {e}")

if __name__ == "__main__":
    test_api() 