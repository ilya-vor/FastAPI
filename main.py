from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Экземпляр приложения FastAPI
app = FastAPI(title="Кейс «Разработка сервиса на Python»")


# Модель данных для входного JSON
class InputData(BaseModel):
    array: List[Optional[str]]


# Словарь для хранения сессий и соответствующих результатов
session_storage = {}


def sum_numbers(numbers: List[Optional[str]]) -> int:
    """
    Суммирует цифры из списка строк.

    Parameters:
    - numbers (List[Optional[str]]):  Список строк или null-значений.

    Returns:
    - int: Сумма цифр из списка.

    Raises:
    - N/A
    """
    total_sum = sum(map(int, [n for n in numbers if isinstance(n, str) and n.isdigit()]))
    return total_sum


@app.post("/sync_sum")
def sync_sum(data: InputData) -> dict:
    """
    Синхронный метод для суммирования чисел.

    Parameters:
    - data (InputData): Данные в формате InputData, содержащие список строк или null-значений.

    Returns:
    - dict: Словарь со статусом и результатом суммирования.

    Raises:
    - N/A
    """
    total_sum = sum_numbers(data.array)
    return {"status": 200, "result": total_sum}


@app.post("/async_sum")
async def async_sum(data: InputData) -> dict:
    """
    Асинхронный метод для суммирования цифр и сохранения результата в словарь сессий.

    Parameters:
    - data (InputData): Данные в формате InputData, содержащие список строк или null-значений.

    Returns:
    - dict: Словарь со статусом и идентификатором сессии.

    Raises:
    - N/A
    """
    session_id = str(len(session_storage))
    total_sum = sum_numbers(data.array)
    session_storage[session_id] = total_sum
    return {"status": 200, "session_id": session_id}


@app.get("/get_result/{session_id}")
def get_result(session_id: str) -> dict:
    """
    Метод для получения результата суммирования по идентификатору сессии.

    Parameters:
    - session_id (str): Идентификатор сессии.

    Returns:
    - dict: Словарь со статусом и результатом суммирования.

    Raises:
    - HTTPException: Если идентификатор сессии не найден.
    """
    if session_id not in session_storage:
        raise HTTPException(status_code=404, detail="Session ID not found")
    return {"status": 200, "result": session_storage[session_id]}
