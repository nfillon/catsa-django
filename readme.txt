Proyecto Administrador de contenido simple para sitio web.

En esta liga de pude administrar el contendido dinamico del sito, CRUD A/B/M de clientes y proyecto, los formularios en este caso los arme con django.


Estructura del Proyecto:


/catsawebsite
    /Catsaweb
	  /template base.html  (Base de todos los html del proyecto)
			    index.html (index del proyecto)
			    instrastructura.html (pagina contenido statico)
   /clientes. 
        /template proyectos.html (Renderiza del modelo clientes la información que se carga desde la app “admcatsa”)
 			  expereiencia.html (Renderiza del modelo proyecto la información que se carga desde la app “admcatsa”)	
        modelos.py (se encuentra los modelos para trabajar con todas las vistas del cliente, produtos, es esta app y en “admcatsa como en “Catsaweb””) 
  /contacto.
	/template contacto.html (En contactos podemos completar el formulario y este se guarda en la DB por el momento solo se puede ver por el administrador de django, 
						   la app de llama contactos donde esta el modelo que arma la estructura, y con la vista armo el formulario el cual esta desarrollado con bootstrap)

        modelos.py (se encuentra todo el modelo del formulario)
        Views.py   (tengo la vista del formulario) Este formulario la idea es que guarde todo en sqllite, y que haga envíos del mail por SMPT pero la integración con SES de Aws no funciono)
  /admcatsa (Es donde se entuerta todo el trabajo de crud)
       /template admcatsa.html (ABM de listado/actualización/borrado de Cliente y Productos.)
			admcatsa-form.html (Agregado de clientes)
                        admcatsa-form-proyecti.html (Agregado de proyecto, permite subir una imagen, la idea es que la imagen se vea en el carrusel de proyectos.html en la app clientes)
			adm-delete-confirmacion/proyecto/mensaje (se utilizar para el borrado de los clientes, proyectos o mensajes)
                       mensajes.html (Es para poder ver los mensajes o borrar)
                       login.html (Logueo en la app)  
                       login.html (Logout en la app)
                       register.html (Register un usuarios)

Solo puede editar borra agregar los usuarios autenticas los permisos que se están manejando son login_required también para la registracion de un usuario nuevo tiene que estar registrado.  


Acceso a la web, en el menu de navegación tiene iniciar sección, comparo el user y pass por medio de el char de coder, una ves que tiene acceso al sitio ya se pueden ver el ABM completo.

http://127.0.0.1:8000/
