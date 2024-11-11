Proyecto: Sistema de Comandas de Restaurante
Situación inicial
Este proyecto tiene como objetivo desarrollar un sistema de comandas que permite a los clientes realizar pedidos directamente a la cocina desde una aplicación web o móvil, sin necesidad de que los clientes creen una cuenta, salvo que quieran recibir ofertas o personalización adicional. Los pedidos serán gestionados en tiempo real y el sistema deberá facilitar tanto la personalización de los platos como la gestión eficiente de los pedidos por parte de la cocina.

Requisitos Funcionales
1.  Acceso al menú sin registro
•   El cliente podrá visualizar el menú completo de la aplicación o página web sin necesidad de registrarse ni iniciar sesión. Se probará accediendo como usuario anónimo y verificando que el menú está completamente accesible y que no te pide credenciales.
2.  Personalización de platos
•   El cliente podrá personalizar su pedido, eligiendo opciones como eliminar ingredientes o ajustar porciones. Se validará haciendo un pedido con personalización y comprobando que estos cambios llegan correctamente a la cocina.
3.  Añadir productos al carrito sin cuenta
•   El usuario debe poder agregar productos al carrito sin estar registrado. Se verificará agregando productos como cliente anónimo y comprobando que los productos se añaden correctamente.
4.  Modificar el carrito antes de confirmar el pedido
•   El cliente podrá modificar el contenido de su carrito (añadir, eliminar o cambiar cantidades) antes de finalizar el pedido. Se comprobará realizando modificaciones en el carrito y revisando que se actualizan correctamente.
5.  Confirmar el pedido sin registro
•   Los clientes podrán confirmar y enviar su pedido sin estar registrados en la plataforma. La validación se hará comprobando que el pedido se envía a la cocina sin necesidad de iniciar sesión.
6.  Notificación de pedido recibido cliente
•   Al enviar un pedido a la cocina, el cliente recibirá una confirmación visual en la pantalla. Se comprobará que la notificación aparece correctamente tras hacer un pedido.
7.  Seguimiento del estado del pedido
•   El cliente podrá consultar el estado de su pedido en tiempo real (por ejemplo, en preparación o listo para recoger). Para validarlo, se verificarán los cambios de estado de los pedidos en la interfaz del cliente.
8.  Notificación de pedido listo
•   El sistema debe notificar al cliente cuando el pedido esté listo para entregar. Se probará simulando un pedido que pasa a estar listo y revisando que la notificación aparece en la pantalla del cliente.
9.  Historial temporal de pedidos
•   El cliente podrá ver un historial temporal de sus pedidos realizados durante la misma sesión, sin necesidad de estar registrado. Se validará realizando varios pedidos y revisando que el historial se mantiene mientras la sesión esté activa.
10. Pago invitado
•   Los usuarios podrán realizar el pago de su pedido utilizando diversas formas de pago (tarjeta de crédito/débito, por ejemplo) sin registrarse. Se probará completando un pago con un cliente no registrado y verificando que se procesa correctamente.
11. Registro opcional para recibir ofertas o ver su historial.
•   Los clientes tendrán la opción de registrarse para recibir promociones especiales o bien ver sus compras previas. Se verificará permitiendo a los usuarios registrarse y comprobar que reciben las promociones como corresponde.
12. Gestión de ofertas y descuentos por parte de la cocina
•   El personal de cocina o administración podrá crear, modificar y eliminar ofertas y descuentos especiales. Se validará añadiendo una oferta y comprobando que se muestra correctamente en la interfaz del cliente.
13. Aplicación automática de descuentos
•   Si el cliente tiene derecho a una oferta o descuento, estos deben aplicarse automáticamente al total de su pedido. Se comprobará realizando pedidos con descuentos activos y validando que el sistema los aplica correctamente.
14. pago cliente
•   El cliente podrá elegir entre diferentes métodos de pago disponibles, como tarjetas de crédito, débito o plataformas de pago online. Se validará seleccionando varios métodos de pago y verificando que todos funcionan correctamente.
15. Generación de factura digital
•   Tras completar el pedido, el sistema debe generar y enviar una factura digital al cliente si lo desea. Se probará haciendo un pedido y verificando que la factura llega al correo electrónico del cliente.
16. Mostrar tiempo estimado de preparación
•   El sistema debe mostrar al cliente el tiempo estimado de preparación de su pedido antes de confirmar la compra. Se verificará realizando un pedido y comprobando que el tiempo estimado se muestra correctamente.
17. Cancelar pedido antes de la preparación
•   El cliente podrá cancelar su pedido siempre y cuando no haya entrado aún en preparación. Se validará haciendo un pedido y cancelándolo antes de que cambie su estado a "en preparación".
18. Modificar el menú en tiempo real
•   La cocina podrá agregar, eliminar o modificar platos del menú en tiempo real. Se comprobará actualizando el menú y verificando que los cambios se reflejan inmediatamente en la interfaz del cliente.

Requisitos No Funcionales
19. Tiempo de respuesta inferior a 2 segundos
•   El sistema debe responder a las acciones de los usuarios en menos de 2 segundos. Se medirá el tiempo de respuesta de varias interacciones con herramientas de monitoreo.

20. Tiempo de carga del menú inferior a 3 segundos
•   El menú debe cargarse completamente en menos de 3 segundos en condiciones normales. Se medirá el tiempo de carga en varios escenarios para comprobar que cumple con este requisito.

21. Protección contra errores comunes del usuario
•   El sistema debe prevenir errores comunes del usuario, como pedir platos que ya no están disponibles. Se simularán estos errores para asegurarse de que el sistema los maneja adecuadamente.
22. Procesamiento de pagos rápido
•   El sistema debe completar el procesamiento de pagos en menos de 5 segundos. Se harán pruebas con distintos métodos de pago para comprobar que el tiempo es el adecuado.

23. Impresión de tickets en cocina
•   La cocina debe poder imprimir un ticket con los detalles del pedido. Para validar esto, se hará un pedido y se comprobará que la impresora genera correctamente el ticket con toda la información del pedido.
24. Ordenación de pedidos por prioridad
•   La cocina debe poder ordenar los pedidos según la prioridad o el tiempo que llevan esperando. Se probará haciendo varios pedidos y verificando que el sistema los organiza correctamente en la pantalla de la cocina.

25. Programación de pedidos para una hora futura
•   El cliente podrá programar un pedido para una hora específica más tarde en el día. Se probará programando un pedido para una hora futura y verificando que se envía a la cocina en el momento adecuado.

26. Visualización de ofertas activas
•   Los usuarios, aunque no estén registrados, deben poder ver las ofertas activas en el menú. Se validará accediendo al menú sin cuenta y verificando que las ofertas aparecen correctamente.

27. Cierre automático de pedidos completados
•   Una vez que el pedido ha sido recogido o entregado, el sistema debe cerrarlo automáticamente. Se probará completando un pedido y verificando que el estado del pedido cambia a "cerrado" una vez entregado.
28. Desactivación de productos según horarios
•   Algunos platos solo estarán disponibles en horarios específicos (ejemplo: menú de desayuno). Se validará configurando horarios para ciertos productos y verificando que aparecen o desaparecen del menú en función de la hora.
29. Registro de errores en los pedidos
•   El sistema debe registrar cualquier error o incidencia que surja con un pedido (por ejemplo, ingredientes faltantes). Se simularán errores y se revisará que el sistema los registre correctamente para posterior revisión.

30. Mostrar información nutricional de los platos
•   El sistema debe permitir que los clientes vean la información nutricional de cada plato antes de hacer el pedido. Se validará seleccionando platos del menú y comprobando que la información nutricional está disponible y es correcta.
31. Opción de dejar propina
•   Los clientes podrán añadir una propina opcional durante el proceso de pago. Se verificará haciendo un pedido y añadiendo propina, para comprobar que se refleja correctamente en el total y se registra en el sistema.

32. Temporizador de pedidos en cocina
•   La cocina debe ver un temporizador que muestre cuánto tiempo lleva cada pedido en preparación. Se validará haciendo varios pedidos y verificando que el temporizador se actualiza correctamente en la interfaz de la cocina.

33. Confirmación de pedidos por email o SMS registrado
•   Los clientes registrados deben poder recibir una confirmación de su pedido por email/SMS. Se validará haciendo un pedido desde una cuenta registrada y comprobando que el SMS de confirmación llega correctamente al número asociado.
34. Revisión del pedido antes de la confirmación
•   El cliente podrá revisar todos los detalles de su pedido (platos, personalización, precios) antes de confirmar la compra. Se probará haciendo un pedido y verificando que la pantalla de confirmación muestra toda la información correctamente.

35. Opción de dejar comentarios sobre el servicio
•   Tras completar el pedido, el cliente debe poder dejar comentarios sobre su experiencia. Se hará un pedido y se verificará que el sistema permite al cliente dejar un comentario y que este se registra correctamente.

36. Historial de pedidos para usuarios registrados
•   Los usuarios registrados deben poder acceder a su historial de pedidos en cualquier momento. Se validará haciendo varios pedidos desde una cuenta registrada y comprobando que el historial se muestra correctamente.
37. Mostrar tiempo estimado de entrega
•   El cliente debe poder ver el tiempo estimado de entrega al confirmar el pedido. Se verificará haciendo un pedido para entrega y comprobando que el tiempo estimado aparece en la pantalla de confirmación.

38. Opción para duplicar un pedido anterior (registrado)
Los clientes registrados deben poder duplicar un pedido pasado sin tener que reconfigurarlo desde cero. Se comprobará accediendo al historial y repitiendo un pedido.
39. Vista previa del pedido en cocina
El personal de cocina podrá ver una vista previa de los ingredientes y personalización de los platos antes de confirmar su preparación. Se validará verificando que las personalizaciones están correctas antes de comenzar.

40. Información sobre alérgenos en tiempo real
El sistema debe alertar al cliente sobre alérgenos presentes en los platos seleccionados. Se validará seleccionando platos con alérgenos y verificando la aparición de la advertencia.

41. Autocompletado de datos de usuario registrado
Los usuarios registrados deben ver sus datos de contacto y pago autocompletados al realizar un pedido. Se probará verificando que los datos se llenan automáticamente en un pedido.

42. Filtrador de productos en menú.
Los clientes podrán filtrar el menú con  botones según dietas especiales como vegana, vegetariana o sin gluten, precios(rango), . Se validará haciendo búsquedas en el menú y verificando que se muestra el filtro correcto.
43. Visualización de platos más pedidos
El sistema mostrará los platos más solicitados en un restaurante. Se validará haciendo varios pedidos y comprobando que los platos populares se actualizan correctamente.

44. Cancelación automática de pedidos inactivos
Si un pedido no se confirma después de un tiempo determinado, será cancelado automáticamente. Se validará creando un pedido sin confirmar y verificando que el sistema lo cancela tras el tiempo límite.

45. Visualización de pedidos en cola por cliente
Los clientes podrán ver en tiempo real cuántos pedidos están antes del suyo en la cola de la cocina. Se validará haciendo varios pedidos y verificando el número de pedidos en espera.

46. Opción de agregar notas especiales para el pedido
El cliente podrá añadir notas especiales o comentarios adicionales para la cocina. Se validará añadiendo notas y verificando que lleguen a la cocina.

47. Pedidos de bebidas por separado
El cliente podrá hacer pedidos de bebidas independientemente de los platos principales, incluso durante la preparación de un pedido ya existente. Se validará haciendo un pedido de bebidas separado.

48. Acceso a la aplicación mediante QR
•  Al escanear el código QR, el usuario es redirigido automáticamente a la aplicación web. Verificar que el QR redirige correctamente a la URL de la aplicación.

49. **Acceso a la aplicación mediante QR** 
    Al escanear el código QR, el usuario es redirigido automáticamente a la aplicación web. 
    Verificar que el QR redirige correctamente a la URL de la aplicación.

50. **Pantalla de bienvenida** 
    Al acceder, el usuario debe ver una pantalla de bienvenida que le ofrece dos opciones: acceder con cuenta (login) o acceder sin registrarse. 
    Verificar que la pantalla de bienvenida se carga correctamente tras acceder desde el QR.

51. **Botón de acceso sin cuenta** 
    En la pantalla de bienvenida, debe haber un botón que permita al usuario acceder sin necesidad de registrarse.
    Verificar que el botón redirige al usuario a la siguiente pantalla sin requerir credenciales.

52. **Botón de login** 
    En la pantalla de bienvenida, debe haber un botón que permita al usuario acceder introduciendo sus credenciales (usuario y contraseña). 
    Comprobar que el botón redirige correctamente a la pantalla de login.

53. **Formulario de login** 
    La pantalla de login debe mostrar un formulario donde el usuario pueda introducir su nombre de usuario y contraseña. 
    Comprobar que el formulario recoge correctamente los datos y valida las credenciales del usuario.

54. **Redirección tras login exitoso** 
    Una vez que el usuario introduce correctamente sus credenciales, debe ser redirigido a la página principal de la aplicación. 
    Verificar que tras el login exitoso, el usuario accede a la página principal.

55. **Validación de credenciales** 
    Si el usuario introduce credenciales incorrectas, el sistema debe mostrar un mensaje de error indicando que los datos no son válidos. 
    Comprobar que el sistema valida las credenciales correctamente y muestra un mensaje de error en caso de fallo.

56. **Acceso sin cuenta directo al menú** 
    Si el usuario elige acceder sin cuenta, debe ser redirigido directamente al menú de comidas o productos disponibles. 
    Verificar que el acceso sin cuenta redirige correctamente al menú.

57. **Carga del menú de comidas y crear base de datos** 
    Al acceder a la página del menú, se deben cargar los productos disponibles desde la base de datos. 
    Comprobar que el menú muestra correctamente los productos disponibles.

58. **Opciones de personalización de productos** 
    Al seleccionar un producto, debe mostrarse la opción de personalizar (por ejemplo, añadir o quitar ingredientes). 
    Verificar que las opciones de personalización se muestran y funcionan correctamente.

59. **Carrito de compras vacío inicialmente** 
    Al acceder al menú por primera vez, el carrito de compras debe estar vacío y debe mostrarse una indicación al usuario. 
    Comprobar que el carrito está vacío cuando se accede por primera vez.

60. **Agregar productos al carrito** 
    El usuario debe poder agregar productos desde el menú al carrito de compras. 
    Verificar que los productos seleccionados se añaden correctamente al carrito.

61. **Visualización del carrito de compras** 
    Al acceder al carrito, el usuario debe poder ver los productos que ha seleccionado, junto con los precios y la cantidad. 
    Comprobar que el carrito muestra correctamente todos los productos seleccionados.

62. **Modificar cantidad de productos en el carrito** 
    El usuario debe poder modificar la cantidad de una clase de productos seleccionados en el carrito. 
    Verificar que al cambiar la cantidad de un producto, el total del pedido se actualiza correctamente.

63. **Eliminar productos del carrito** 
    El usuario debe poder eliminar productos del carrito antes de confirmar su pedido. 
    Comprobar que los productos se eliminan correctamente del carrito y el total se actualiza.

64. **Confirmación del pedido sin cuenta** 
    Si el usuario no tiene una cuenta, debe poder confirmar el pedido sin registrarse. 
    Verificar que el pedido se procesa correctamente aunque el usuario no esté registrado.

65. **Proceso de pago básico sin registro** 
    El usuario debe poder completar el proceso de pago sin necesidad de registrarse. 
    Comprobar que el sistema permite realizar el pago sin cuenta y guarda la información del pedido en la base de datos.

66. **Guardar pedido en la base de datos** 
    Al confirmar el pedido, este debe guardarse en la base de datos con el detalle de los productos seleccionados. 
    Verificar que cada pedido se guarda correctamente con su detalle en la base de datos.

67. **Notificación de pedido realizado** 
    Tras completar el pedido, el cliente y el invitado debe recibir una notificación visual indicando que el pedido ha sido procesado con éxito. 
    Comprobar que el sistema muestra la notificación una vez el pedido ha sido registrado.

68. **Manejo de errores en el proceso de pedido** 
    Si ocurre un error durante el proceso de pedido (por ejemplo, un problema con el pago), el sistema debe notificar al usuario y permitirle corregir el error. 
    Verificar que el sistema maneja correctamente los errores y permite al usuario repetir el proceso.

69. **Visualizar menú con opciones de comida** 
    La página web debe mostrar un menú con las opciones de todos los platos que hayan sido agregados al menú. 
    Observar gráficamente que hay un menú con varias opciones de platos.

70. **Añadir platos al menú** 
    Añadir platos al menú de forma persistente desde la página principal (función cocinero). 
    Agregar un plato y, tras apagar y volver a iniciar el programa, comprobar que el plato sigue estando disponible.

71. **Persistencia de sesión** 
    Al registrarse un usuario, su sesión debe mantenerse activa de forma persistente. Al apagar la máquina y volver a iniciar el programa, la sesión debe seguir en pie. 
    Verificar que la sesión del usuario se mantiene activa después de apagar y reiniciar la máquina.

72. **Clasificar por categorías** 
 La página principal debe tener menu y carta, con su primero,segundo y postre, por otro lado, entrantes, primero,segundo y postre, respectivamente

73. **Añadir función registrarse desde Invitado** 
 Añadir boton registrarse para el invitado desde su interfaz alladodelboton azul, y al pinchar en iniciar sesion que te ponga ahi crear cuenta también. Debe verse visualmente y funcionar al pinchar que te redirije a la ventana correspondiente.

 74.  **Notificación de pedido recibido invitado**
•   Al enviar un pedido a la cocina, el invitado recibirá una confirmación visual en la pantalla. Se comprobará que la notificación aparece correctamente tras hacer un pedido.

 75.  **Al registrarse recibir un email**
 Al registrarse un cliente debe llegarle un email a través de su servidor de correo. 

 76. **El sistema debe soportar 5 usuarios al momento**
 Comprobar que tiene la capacidad de soportar clientes en paralelo y realizar funciones sin que se caiga.

 77. **Formulario de login con olvidaste clave** 
    La pantalla de login debe mostrar un formulario donde el usuario pueda recuperar su nombre de usuario y contraseña. 
    Comprobar que el formulario recoge correctamente los datos y valida las credenciales nuevas del usuario,verificando desde email.

