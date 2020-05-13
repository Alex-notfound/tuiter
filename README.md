Voy a hacer un clon de twitter, de manera que cada usuario (del que se guarda el nombre y la fecha de nacimiento), 
pueda crear comentarios (texto y fecha y hora de publicación), y acceder a los que ha creado anteriormente. 
Todos los usuarios pueden dar un "me gusta" a los comentarios de los otros, almacenándose estos de manera que un usuario pueda 
comprobar qué usuarios han dado ese "me gusta", así como el número total.

Entidades: usuarios (nombre completo, email y fecha de nacimiento), comentarios (texto, fecha y hora de publicación), y likes (fecha y hora, comentario, usuario).

En resumen, las funcionalidades esenciales son las siguientes:
* Registrarse
* Iniciar sesión mediante correo electrónico
* Tuitear (publicar un texto)
* Consultar todos los tuits por orden de más reciente a más antiguo
* Consultar el perfil de un usuario (incluído el suyo propio)
* Dar un like a un tuit
* Ver el número de likes de un tuit y los usuarios que han dado like
* Cerrar sesión