# ProyectoRecomendacionVuelos

Elaborado por: Luis Rey Sanchez

Link: https://youtu.be/VWb6aYOuxYI

1. Barra de Navegación: 

	- Inicio, Operadores, Trayectos, Busqueda,

	- Boton Ingreso (Login/Logout)

2. Detalle: 

2.1 Inicio: Pagina principal, Incluye boton de login /logout

2.2 Operadores: Para su ingreso es necesario login (pagina de login y Registro).

	- Ingreso a operadores: Lista de operadores, detalle de operadores
	- A manera de ejemplo se ha incluido CRUD completo (Ver, Editar, Borrar, Agregar)
	- Luego de salir ingresar a pagina de INICIO

2.3 Trayectos: Para su ingreso no es necesario login

	- Cronograma de Todos los trayectos (Ruta, Fecha de salida).
	- A manera de ejemplo se ha incluido CRUD completo (Ver, Editar, Borrar, Agregar)

2.4 Busqueda: 

	- Barra de busqueda de Viaje (de toda la lista de trayectos)
	- Boton de busqueda de trayectos

2.5 Usuarios:

	- Login: mensaje de saludo personalizado a usuario
	- Logout: mensaje deslogueo
	- Editar Perfil: Solo aparece opcion si esta logueado

3. Footer:
	Contenido: About, Contact,Terms of Use, Redes Sociales
	Aparece al final de todas las paginas

3.1 About: Página con mensaje que indica que esta en mantenimiento

3.2 Contact: Se ha incluido un App de mensajería para estar en contacto con el adm

	Mail
	- Para el envio y recepcción de correo se utiliza el servicio de gmail.
	- Se necesita configurar una cuenta de gmail y contraseña (settings.py, views.py) 
	- Ajustar configuracion de Cuenta de Google, para permitir el acceso de aplicaciones poco seguras

	Mensaje
	- Campos: Nombre, Email, Mensaje
	- No permite enviar informacion en blanco
	- Al pulsar boton enviar: mensaje enviado con exito
	- Solo aparece mensaje enviado con exito cuando se valida y envia mensaje de forma exitosa

3.3 Terms of Use: Página con mensaje que indica que esta en mantenimiento

3.4 Contacto por Redes sociales

	- Instagram: Link de ingreso a instagram
	- Facebook: Link de ingreso a facebook
