# ProyectoFinal_Rodriguez
 Proyecto Final - Alejandro Rodriguez - Curso: Python, Camada: 50195

 Desarrollado en Python 3.11.4, con Django 5.0

La web se accede desde la direccion por defecto del server, la cual ya está configurada para que nos lleve a la página de inicio, sin la necesidad de poner la URL '/inicio'. De todas formas se puede hacer y también es funcional. Si se desea ingresar al panel de admin o a la web con usuario admin para ver todas las funcionalidades, el superusuario es **admin** y la password es **admin123**.

El proyecto es una web para un local de comidas rápidas. En la barra de navegación superior se pueden encontrar 3 links (los 3 funcionales) a **Inicio**, **Carta** y **Hacé tu Pedido**.

**Inicio**, que es el logo de la empresa, lleva a la página de inicio.
**Carta** nos da acceso a lo que sería la Carta, donde están integrados los 4 modelos a través de 4 botones. Al ingresar a los mismos nos muestra un read de la base de datos con los productos de la categoría seleccionada. Y debajo nos brinda la opción (a través de su respectivo botón) de Agregar, que nos permite agregar productos a la BD. También está la opción de Buscar, que nos permite buscar en la BD por el nombre (o incluso por algunas letras) del producto.
**Hacé tu Pedido** lleva a un formulario que es funcional, pero que no cumple con la función de Carrito de Compras. El botón nos lleva a una URL en Construcción.

Sin haberse autenticado, las unicas urls accesibles son inicio/, login/ y signup/. Asimismo, hay algunas urls en las que se realiza la validacion definida en la funcion es_staff, bloqueando así el acceso a funcionalidades (C), (U) y (D) del CRUD de los modelos a los usuarios que no sean staff. Si un usuario general intenta acceder directo desde la barra de direcciones a una de estas url, lo redirigirá a otra que le envía un mensaje de error.

En la navbar, además de los tres links mencionados previamente, también aparece el avatar y un saludo al usuario. En el saludo, si se hace clic en el nombre, se accede a la url para editar el perfil. En la página para editar el perfil, también se accede la opción de editar avatar, donde se podrá cargar una nueva imagen.

Las URL con las que cuenta el proyecto son las siguientes (copio y pego desde urls.py):

    path('admin/', admin.site.urls),
    
    #URLs generales
    path('', InicioView.as_view(), name='Inicio'),
    path('inicio/', InicioView.as_view(), name='inicio'),
    path('carta/', CartaView.as_view(), name='carta'),
    path('pedido/', PedidoView.as_view(), name='pedido'),
    path('about/', AboutView.as_view(), name='about'),

    #URLs de los modelos creados (R)
    path('comida/', ComidaView.as_view(), name='comida'),
    path('bebida/', BebidaView.as_view(), name='bebida'),
    path('guarnicion/', GuarnicionView.as_view(), name='guarnicion'),
    path('postre/', PostreView.as_view(), name='postre'),

    #URLs para agregar elementos (C)
    path('agregarComida/', AgregarComida.as_view(), name='agregarComida'),
    path('agregarBebida/', AgregarBebida.as_view(), name='agregarBebida'),
    path('agregarGuarnicion/', AgregarGuarnicion.as_view(), name='agregarGuarnicion'),
    path('agregarPostre/', AgregarPostre.as_view(), name='agregarPostre'),

    #URLs para editar elementos (U)
    path('actualizarComida/<int:pk>/', ActualizarComida.as_view(), name='actualizarComida'),
    path('actualizarBebida/<int:pk>/', ActualizarBebida.as_view(), name='actualizarBebida'),
    path('actualizarGuarnicion/<int:pk>/', ActualizarGuarnicion.as_view(), name='actualizarGuarnicion'),
    path('actualizarPostre/<int:pk>/', ActualizarPostre.as_view(), name='actualizarPostre'),

    #URLs para eliminar elementos (D)
    path('eliminarComida/<int:pk>/', EliminarComida.as_view(), name='eliminarComida'),
    path('eliminarBebida/<int:pk>/', EliminarBebida.as_view(), name='eliminarBebida'),
    path('eliminarGuarnicion/<int:pk>/', EliminarGuarnicion.as_view(), name='eliminarGuarnicion'),
    path('eliminarPostre/<int:pk>/', EliminarPostre.as_view(), name='eliminarPostre'),

    #URLs para buscar elementos
    path('buscarComida/', buscarComida, name='Buscar Comida'), 
    path('buscarBebida/', buscarBebida, name='Buscar Bebida'),
    path('buscarGuarnicion/', buscarGuarnicion, name='Buscar Guarnicion'),
    path('buscarPostre/', buscarPostre, name='Buscar Postre'),

    #URLs para resultados de busqueda:
    path('resultadosComida/', resultadosComida, name='Resultados Comida'),
    path('resultadosBebida/', resultadosBebida, name='Resultados Bebida'),
    path('resultadosGuarnicion/', resultadosGuarnicion, name='Resultados Guarnicion'),
    path('resultadosPostre/', resultadosPostre, name='Resultados Postre'),

    #URLs para manejo de usuarios
    path('login/', user_login, name='Login'),
    path('signup/', user_signup, name='Signup'),
    path('logout/', user_logout, name='Logout'),

    #URLs para manejo de perfiles
    path('editarPerfil/', editar_perfil, name='Editar Perfil'),
    path('agregarAvatar/', agregar_avatar, name='Agregar Avatar'),

    #URLs varias
    path('accesoDenegado/', acceso_denegado, name='accesoDenegado'),
    path('enConstruccion/', en_construccion, name='enConstruccion'),
