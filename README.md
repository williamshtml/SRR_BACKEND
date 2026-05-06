# SRR_BACKEND - Sistema de Recaudación 

 equipo Ya subí el core del backend para el sistema de recaudación de la empresa. Todo el código está ordenado para que podamos trabajar en conjunto siguiendo la arquitectura que definimos.

##  Estructura del Proyecto
He organizado las carpetas para que el código sea fácil de mantener y escalar:

- /app: Contiene toda la lógica principal del sistema.
  - /config: Configuraciones generales de la aplicación.
  - /controller: Donde se reciben las peticiones de la API.
  - /dto: Objetos de transferencia de datos para asegurar que recibimos lo que queremos.
  - /entity: Definición de las tablas de la base de datos.
  - /repository: Lógica para guardar y sacar datos de la BD.
  - /service: La lógica de negocio pesada del sistema.
  - /util: Herramientas y funciones de apoyo.
- docker-compose.yml: Archivo para levantar todo el entorno de trabajo con un solo comando.
- requirements.txt: Lista de todas las librerías de Python que usamos.

## Pruebas con Postman (Paso a Paso)
He subido la colección oficial al repositorio para que todos probemos lo mismo y no haya errores de rutas.

1. Descarga el archivo: Busquen el archivo "SRR_BACKEND_Postman_Collection.json" que está en la raíz del proyecto.
2. Importar: Abran su Postman, denle al botón "Import" y arrastren ese archivo.
3. Endpoints listos: Ya tienen configurado el flujo de POST /api/v1/sync/collect para sincronizar transacciones.
4. Validación de Tokens: El sistema valida los UUID de seguridad. Usen los tokens asignados a Juan Santos y a la cuenta de la empresa Aldo Malpica S.A.. Si el token no existe, el sistema los rebotará.
5. Verificación: Si les responde un "200 OK", es que la transacción se guardó correctamente en la tabla de pagos.

## 🛠️ Cómo levantar el entorno
Para no perder tiempo configurando la base de datos manualmente, usen Docker. Solo ejecuten en la terminal:

docker-compose up --build

Esto dejará el servidor arriba en http://localhost:8000.

---
*Si tienen problemas con los contenedores o los tokens de la empresa, me avisan de inmediato para chequearlo.*
