# Инструкция по поднятию данного сервиса

1. Регистрируемся на render.com
2. Нажимаем "New" --> "Web Service"
3. Выбираем "Build and deploy from a Git repository"
4. Выбираем нужный репозиторий
5. В поле "Build Command" пишем: pip install -r requirements.txt
6. В поле "Start Command" пишем: uvicorn main:app --host=0.0.0.0 --port=$PORT
7. Нажимаем "Create Web Service"
8. Под названием сервиса появляется ссылка, в моем случае это: https://case-2024-vorobev-ilya.onrender.com
9. Ожидем в логах сообщения "Your service is live 🎉"
10. Сервис работает!

