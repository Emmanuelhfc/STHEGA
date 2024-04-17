# HeatExGA
 Software desenvolvido como projeto de TCC sobre dimensionamento de Trocadores de Calor Casco e Tubo com o uso de GA's.



## Comandos 

```
pyside6-uic interface/ui_MainWindow.ui -o interface/ui_mainwindow.py

```

Como no projeto pode ser que eu fique alterando os models vou suar Alembic para fazer migrações
ver mais em [Alembic Tutorial](https://simplyprashant.medium.com/how-to-use-alembic-for-your-database-migrations-d3e93cacf9e8)

```
alembic init alembic
```

makemigration
```
alembic revision — autogenerate -m “First commit”
```

migrate
```
alembic upgrade head
```