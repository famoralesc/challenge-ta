# Backend Ssr Challenge

### NOTA IMPORTANTE

Para correr el servicio-2 y 3 correctamente, debes setear en `docker-compose.yml` (`servicio-2` y `servicio-3`) la variable de entorno **INFLUX_TOKEN**, la cual debes obtener desde influx CLI en http://localhost:8086/ como se muestra a continuación:

```
  servicio-2:
    ...
    environment:
      - INFLUX_TOKEN=set-your-own-token-here
    ...

  servicio-3:
    ...
    environment:
      - INFLUX_TOKEN=set-your-own-token-here
    ...
```

## Desafio

El desafío consiste en desarrollar 3 microservicios(servicio-1, 2 y 3) que cumplan lo requerido en el *README* de cada carpeta.
Para ello debe desarrollar el código de cada servicio y confeccionar el Dockerfile correspondiente a cada servicio que puede o no ser el mismo dependiendo como lo haga.

La forma de entrega es subir la resolucion en un repositorio publico y luego envíar el link con la resolución.

Para facilitar un poco las cosas ya hay un archivo docker-compose con todos los servicios necesarios para poder realizar el desafío.

El plazo es de una semana desde recibido el link a este repositorio y no hay restricciones en cuanto a lenguajes o tecnologías, aunque se recomienda Python o Typescript para la resolución.

Puntos extras si se quiere agregar un front sencillo que utilice el servicio-3.

Diagrama

![Esquema de resolución](./challenge.png "Esquema de resolución")