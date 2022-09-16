# Backend Challenge 

Este es el challenge de backend de Tecnoandina SPA.

# Tarea
Queremos una API REST que permita crear, editar, eliminar y listar brokers mqtt. Estos brokers tienen topicos y targets, por lo que tambien necesitamos endpoints para crear, editar, eliminar y listar topicos y targets.
Actualmente tenemos esta configuracion en un json, y queremos que todo este en una base de datos sql.

```json
{
  "brokers": [
    {
      "id": "broker1_id",
      "hostname": "mosquitto",
      "port": 1883,
      "username": "mqttuser",
      "password": "mqttpass",
      "transport": "tcp",
      "targets": [
        {
            "url": "localhost:5000/target1"
        },
        {
            "url": "localhost:3000/target2"
        }
      ],
      "topics": [
        {
          "topic": "test1/#",
          "qos": 0
        }
      ]
    },
    {
      "id": "broker2_id",
      "hostname": "mosquitto",
      "port": 1883,
      "username": "mqttuser",
      "password": "mqttpass",
      "transport": "tcp",
      "targets": [
        {
            "url": "localhost:5000/target3"
        },
        {
            "url": "localhost:3000/target4"
        }
      ],
      "topics": [
        {
          "topic": "test2/#",
          "qos": 0
        }
      ]
    }
  ]
}
```

El endpoint de creacion y edicion de los brokers, debe probar la conexion y ver que sea posible antes de guardarla en la base de datos. En caso de no ser positiva, debe retornar un error.

# Stack

En general estariamos buscando que el stack sea el siguiente:

- Python (FastAPI + SQLModel)
- MySQL
- Mosquitto
- Docker + docker-compose

En caso de que sientas mas comodo con otro stack, puedes usarlo. Pero debes explicar por que lo usaste. Pero igual debes usar MySQL, docker y mosquitto.
Parte de la entrega es un docker-compose que levante todo lo necesario, es decir la API, la base de datos y mosquitto.

# Extras

Puedes agregar todo lo que quieras de buenas practicas, documentacion, tests, etc.
Si quieres agregar un frontend, puedes hacerlo. Pero no es necesario.

# Entrega

Tienes 5 días para resolverlo contando desde el dia que recibiste el mail con este link. Debes resolverlo y subirlo a un repositorio publico de github/gitlab/etc. Luego debes enviar el link del repositorio a la persona que te envio este link.
Cualquier duda o consulta que tengas la puedes hacer por mail.