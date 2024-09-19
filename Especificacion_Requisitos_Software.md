Proyecto: Sistema de Comandas de Restaurante
Situación inicial
Este proyecto tiene como objetivo desarrollar un sistema de comandas que permite a los clientes realizar pedidos directamente a la cocina desde una aplicación web o móvil, sin necesidad de que los clientes creen una cuenta, salvo que quieran recibir ofertas o personalización adicional. Los pedidos serán gestionados en tiempo real y el sistema deberá facilitar tanto la personalización de los platos como la gestión eficiente de los pedidos por parte de la cocina.

Requisitos Funcionales
1.  Acceso al menú sin registro
o   El cliente podrá visualizar el menú completo de la aplicación o página web sin necesidad de registrarse ni iniciar sesión. Se probará accediendo como usuario anónimo y verificando que el menú está completamente accesible y que no te pide credenciales.
2.  Personalización de platos
o   El cliente podrá personalizar su pedido, eligiendo opciones como eliminar ingredientes o ajustar porciones. Se validará haciendo un pedido con personalización y comprobando que estos cambios llegan correctamente a la cocina.
3.  Añadir productos al carrito sin cuenta
o   El usuario debe poder agregar productos al carrito sin estar registrado. Se verificará agregando productos como cliente anónimo y comprobando que los productos se añaden correctamente.
4.  Modificar el carrito antes de confirmar el pedido
o   El cliente podrá modificar el contenido de su carrito (añadir, eliminar o cambiar cantidades) antes de finalizar el pedido. Se comprobará realizando modificaciones en el carrito y revisando que se actualizan correctamente.
5.  Confirmar el pedido sin registro
o   Los clientes podrán confirmar y enviar su pedido sin estar registrados en la plataforma. La validación se hará comprobando que el pedido se envía a la cocina sin necesidad de iniciar sesión.
6.  Notificación de pedido recibido
o   Al enviar un pedido a la cocina, el cliente recibirá una confirmación visual en la pantalla. Se comprobará que la notificación aparece correctamente tras hacer un pedido.
7.  Seguimiento del estado del pedido
o   El cliente podrá consultar el estado de su pedido en tiempo real (por ejemplo, en preparación o listo para recoger). Para validarlo, se verificarán los cambios de estado de los pedidos en la interfaz del cliente.
8.  Notificación de pedido listo para recoger
o   El sistema debe notificar al cliente cuando el pedido esté listo para recoger o entregar. Se probará simulando un pedido que pasa a estar listo y revisando que la notificación aparece en la pantalla del cliente.
9.  Historial temporal de pedidos
o   El cliente podrá ver un historial temporal de sus pedidos realizados durante la misma sesión, sin necesidad de estar registrado. Se validará realizando varios pedidos y revisando que el historial se mantiene mientras la sesión esté activa.
10. Pago sin necesidad de cuenta
•   Los usuarios podrán realizar el pago de su pedido utilizando diversas formas de pago (tarjeta de crédito/débito, por ejemplo) sin registrarse. Se probará completando un pago con un cliente no registrado y verificando que se procesa correctamente.
11. Registro opcional para recibir ofertas
•   Los clientes tendrán la opción de registrarse para recibir ofertas y promociones especiales. Se verificará permitiendo a los usuarios registrarse y comprobar que reciben las promociones como corresponde.
12. Gestión de ofertas y descuentos por parte de la cocina
•   El personal de cocina o administración podrá crear, modificar y eliminar ofertas y descuentos especiales. Se validará añadiendo una oferta y comprobando que se muestra correctamente en la interfaz del cliente.
13. Aplicación automática de descuentos
•   Si el cliente tiene derecho a una oferta o descuento, estos deben aplicarse automáticamente al total de su pedido. Se comprobará realizando pedidos con descuentos activos y validando que el sistema los aplica correctamente.
14. Selección de métodos de pago
•   El cliente podrá elegir entre diferentes métodos de pago disponibles, como tarjetas de crédito, débito o plataformas de pago online. Se validará seleccionando varios métodos de pago y verificando que todos funcionan correctamente.
15. Generación de factura digital
•   Tras completar el pedido, el sistema debe generar y enviar una factura digital al cliente si lo desea. Se probará haciendo un pedido y verificando que la factura llega al correo electrónico del cliente.
16. Mostrar tiempo estimado de preparación
•   El sistema debe mostrar al cliente el tiempo estimado de preparación de su pedido antes de confirmar la compra. Se verificará realizando un pedido y comprobando que el tiempo estimado se muestra correctamente.
17. Cancelar pedido antes de la preparación
•   El cliente podrá cancelar su pedido siempre y cuando no haya entrado aún en preparación. Se validará haciendo un pedido y cancelándolo antes de que cambie su estado a "en preparación".
18. Modificar el menú en tiempo real
•   La cocina podrá agregar, eliminar o modificar platos del menú en tiempo real. Se comprobará actualizando el menú y verificando que los cambios se reflejan inmediatamente en la interfaz del cliente.
19. Desactivar automáticamente platos no disponibles
•   Si un plato no está disponible (por ejemplo, por falta de ingredientes), el sistema debe desactivarlo automáticamente. Se validará simulando la falta de ingredientes y comprobando que el plato desaparece del menú.
 
Requisitos No Funcionales
20. Tiempo de respuesta inferior a 2 segundos
•   El sistema debe responder a las acciones de los usuarios en menos de 2 segundos. Se medirá el tiempo de respuesta de varias interacciones con herramientas de monitoreo.
21. Disponibilidad del sistema del 99%
•   El sistema debe estar operativo al menos el 99% del tiempo durante las horas de servicio. Se realizará un monitoreo de la disponibilidad para validar que cumple con este requisito.
22. Compatibilidad con dispositivos móviles
•   La aplicación debe ser completamente funcional en dispositivos móviles y de escritorio. Se probará en varios dispositivos para asegurarse de que el sistema es compatible y responsivo.
23. Cifrado de datos personales y de pago
•   Toda la información sensible, como los datos personales y los métodos de pago, debe estar cifrada en la base de datos. Se verificará que la información almacenada esté cifrada y protegida.
24. Escalabilidad para manejar múltiples pedidos simultáneos
•   El sistema debe ser capaz de gestionar hasta 100 pedidos simultáneos sin experimentar problemas de rendimiento. Se realizará una simulación con carga masiva para probar la escalabilidad.
25. Interfaz intuitiva y fácil de usar
•   La aplicación debe ser intuitiva y de fácil uso, de modo que cualquier cliente pueda navegar sin problemas. Se harán pruebas de usabilidad con usuarios reales para asegurarse de que la experiencia es sencilla.
26. Tiempo de carga del menú inferior a 3 segundos
•   El menú debe cargarse completamente en menos de 3 segundos en condiciones normales. Se medirá el tiempo de carga en varios escenarios para comprobar que cumple con este requisito.
27. Soporte para múltiples idiomas
•   La aplicación debe ofrecer soporte en, al menos, español e inglés. Se verificará que el sistema permita cambiar entre estos idiomas sin problemas.
28. Protección contra errores comunes del usuario
•   El sistema debe prevenir errores comunes del usuario, como pedir platos que ya no están disponibles. Se simularán estos errores para asegurarse de que el sistema los maneja adecuadamente.
29. Procesamiento de pagos rápido
•   El sistema debe completar el procesamiento de pagos en menos de 5 segundos. Se harán pruebas con distintos métodos de pago para comprobar que el tiempo es el adecuado.
30. Facilidad de integración con otros sistemas
•   La aplicación debe ser fácil de integrar con otros sistemas, como impresoras de cocina o sistemas de inventario. Se realizarán pruebas de integración para verificar su funcionamiento.
 
31. Impresión de tickets en cocina
•   La cocina debe poder imprimir un ticket con los detalles del pedido. Para validar esto, se hará un pedido y se comprobará que la impresora genera correctamente el ticket con toda la información del pedido.
32. Ordenación de pedidos por prioridad
•   La cocina debe poder ordenar los pedidos según la prioridad o el tiempo que llevan esperando. Se probará haciendo varios pedidos y verificando que el sistema los organiza correctamente en la pantalla de la cocina.
33. Gestión de pedidos agrupados
•   Los pedidos realizados por el mismo cliente en un intervalo de tiempo deben poder ser agrupados para que se preparen juntos. Se verificará haciendo varios pedidos de un mismo cliente y comprobando que llegan agrupados a la cocina.
34. Programación de pedidos para una hora futura
•   El cliente podrá programar un pedido para una hora específica más tarde en el día. Se probará programando un pedido para una hora futura y verificando que se envía a la cocina en el momento adecuado.
35. Notificación de ingredientes agotados
•   Si un plato no puede ser preparado por falta de ingredientes, el cliente deberá ser notificado antes de confirmar el pedido. Se simulará la falta de ingredientes y se validará que el sistema muestra la notificación correspondiente.
36. Selección de recogida o entrega en mesa
•   El cliente podrá seleccionar si quiere recoger el pedido en el mostrador o recibirlo en la mesa. Para comprobar esto, se hará un pedido con ambas opciones y se verificará que el sistema gestiona correctamente la entrega.
37. Generación de código QR para recoger el pedido
•   El sistema debe generar un código QR que el cliente pueda escanear al recoger su pedido. Se hará un pedido y se validará que el QR se genera correctamente y puede ser escaneado en el punto de recogida.
38. Visualización de ofertas activas
•   Los usuarios, aunque no estén registrados, deben poder ver las ofertas activas en el menú. Se validará accediendo al menú sin cuenta y verificando que las ofertas aparecen correctamente.
39. Aplicación de descuentos por cupones
•   El cliente podrá introducir códigos de descuento (cupones) para aplicar reducciones en el precio del pedido. Se verificará creando un pedido y aplicando varios cupones para comprobar que el descuento se refleja correctamente en el total.
40. Cierre automático de pedidos completados
•   Una vez que el pedido ha sido recogido o entregado, el sistema debe cerrarlo automáticamente. Se probará completando un pedido y verificando que el estado del pedido cambia a "cerrado" una vez entregado.
41. Desactivación de productos según horarios
•   Algunos platos solo estarán disponibles en horarios específicos (ejemplo: menú de desayuno). Se validará configurando horarios para ciertos productos y verificando que aparecen o desaparecen del menú en función de la hora.
42. Registro de errores en los pedidos
•   El sistema debe registrar cualquier error o incidencia que surja con un pedido (por ejemplo, ingredientes faltantes). Se simularán errores y se revisará que el sistema los registre correctamente para posterior revisión.
43. Descuento por frecuencia de compra
•   Los clientes registrados deben recibir descuentos automáticos basados en la frecuencia con la que hacen pedidos. Se probará creando una cuenta y haciendo varios pedidos para verificar que el descuento se aplica tras alcanzar un umbral.
44. Mostrar información nutricional de los platos
•   El sistema debe permitir que los clientes vean la información nutricional de cada plato antes de hacer el pedido. Se validará seleccionando platos del menú y comprobando que la información nutricional está disponible y es correcta.
45. Opción de dejar propina
•   Los clientes podrán añadir una propina opcional durante el proceso de pago. Se verificará haciendo un pedido y añadiendo propina, para comprobar que se refleja correctamente en el total y se registra en el sistema.
46. Visualización del estado del inventario en cocina
•   El personal de cocina debe poder consultar el estado del inventario en tiempo real. Se validará revisando el inventario tras varios pedidos y comprobando que las actualizaciones son visibles para el personal de cocina.
47. Sugerencias de platos alternativos
•   Si algún ingrediente de un plato no está disponible, el sistema debe sugerir automáticamente opciones alternativas. Se verificará haciendo un pedido que incluya un plato con ingredientes agotados y revisando que el sistema sugiere opciones alternativas.
48. Temporizador de pedidos en cocina
•   La cocina debe ver un temporizador que muestre cuánto tiempo lleva cada pedido en preparación. Se validará haciendo varios pedidos y verificando que el temporizador se actualiza correctamente en la interfaz de la cocina.
49. Compatibilidad con impresoras térmicas de tickets
•   El sistema debe ser compatible con impresoras térmicas para generar tickets de los pedidos. Se hará una prueba de impresión para confirmar que los tickets se generan y se imprimen correctamente.
50. Soporte para múltiples monedas
•   Los usuarios registrados que realicen pedidos desde otros países deben poder seleccionar su moneda local. Se verificará cambiando la configuración de la moneda y haciendo un pedido para comprobar que los precios se muestran correctamente.
51. Confirmación de pedidos por SMS
•   Los clientes registrados deben poder recibir una confirmación de su pedido por SMS. Se validará haciendo un pedido desde una cuenta registrada y comprobando que el SMS de confirmación llega correctamente al número asociado.
52. Revisión del pedido antes de la confirmación
•   El cliente podrá revisar todos los detalles de su pedido (platos, personalización, precios) antes de confirmar la compra. Se probará haciendo un pedido y verificando que la pantalla de confirmación muestra toda la información correctamente.
53. Integración con Google Maps para la recogida
•   El sistema debe permitir al cliente recibir indicaciones de cómo llegar al punto de recogida a través de Google Maps. Se validará haciendo un pedido para recoger y verificando que el enlace a Google Maps aparece y funciona correctamente.
54. Opción de dejar comentarios sobre el servicio
•   Tras completar el pedido, el cliente debe poder dejar comentarios sobre su experiencia. Se hará un pedido y se verificará que el sistema permite al cliente dejar un comentario y que este se registra correctamente.
55. Advertencia de horarios de cocina cerrada
•   El sistema debe notificar al cliente si intenta hacer un pedido cuando la cocina está cerrada. Se verificará intentando hacer pedidos fuera de horario y comprobando que la notificación aparece correctamente.
56. Validación de edad para productos restringidos
•   El sistema debe solicitar la verificación de edad para productos restringidos (como alcohol). Se probará haciendo un pedido que incluya un producto restringido y comprobando que el sistema solicita la validación de edad.
57. Historial de pedidos para usuarios registrados
•   Los usuarios registrados deben poder acceder a su historial de pedidos en cualquier momento. Se validará haciendo varios pedidos desde una cuenta registrada y comprobando que el historial se muestra correctamente.
58. Mostrar tiempo estimado de entrega
•   El cliente debe poder ver el tiempo estimado de entrega al confirmar el pedido. Se verificará haciendo un pedido para entrega y comprobando que el tiempo estimado aparece en la pantalla de confirmación.
59. Personalización de la interfaz para usuarios registrados
•   Los usuarios registrados podrán personalizar ciertos aspectos de la interfaz (como el tema oscuro o el tamaño de la fuente). Se validará permitiendo que los usuarios hagan estos ajustes y comprobando que los cambios se aplican correctamente.
60. Programación de pedidos recurrentes
•   Los usuarios registrados podrán programar pedidos recurrentes, como pedidos diarios o semanales. Se probará configurando un pedido recurrente y verificando que el sistema lo procesa automáticamente en las fechas establecidas.
61. Sugerencia de menú según historial de pedidos
El sistema debe sugerir platos basados en los pedidos anteriores del cliente registrado. Se validará verificando que las sugerencias aparecen correctamente en función del historial de pedidos.
62. Opción para duplicar un pedido anterior
Los clientes registrados deben poder duplicar un pedido pasado sin tener que reconfigurarlo desde cero. Se comprobará accediendo al historial y repitiendo un pedido.
63. Vista previa del pedido en cocina
El personal de cocina podrá ver una vista previa de los ingredientes y personalización de los platos antes de confirmar su preparación. Se validará verificando que las personalizaciones están correctas antes de comenzar.
64. Pedidos agrupados por tiempo de preparación
Los pedidos que tienen platos con tiempos de preparación similares se agruparán automáticamente para optimizar el flujo de trabajo en la cocina. Se validará haciendo varios pedidos y comprobando su agrupación.
65. Configuración de niveles de picante o condimentos
El cliente debe poder elegir el nivel de picante o añadir condimentos específicos en sus platos. Se probará realizando pedidos con diferentes niveles de condimentos.
66. Información sobre alérgenos en tiempo real
El sistema debe alertar al cliente sobre alérgenos presentes en los platos seleccionados. Se validará seleccionando platos con alérgenos y verificando la aparición de la advertencia.
67. Opción de dividir la cuenta entre varios clientes
El sistema permitirá dividir el costo de un pedido entre varios usuarios antes de confirmar el pago. Se validará realizando un pedido y dividiendo la cuenta entre varias formas de pago.
68. Autocompletado de datos de usuario registrado
Los usuarios registrados deben ver sus datos de contacto y pago autocompletados al realizar un pedido. Se probará verificando que los datos se llenan automáticamente en un pedido.
69. Personalización de combos de menú
El cliente debe poder armar combos personalizados seleccionando diferentes opciones dentro de un conjunto. Se validará creando un combo personalizado y verificando que la cocina lo recibe correctamente.
70. Aviso de tiempo de espera prolongado
El sistema debe alertar al cliente si el tiempo de preparación estimado excede un cierto umbral. Se probará simulando demoras en la cocina y revisando las notificaciones.
71. Asignación automática de pedidos a chefs especializados
El sistema debe asignar automáticamente platos específicos a chefs con especialización en esos platos. Se validará verificando que los pedidos se distribuyen según las especialidades.
72. Programación de pedidos según turnos de cocina
El cliente podrá programar un pedido en función de la disponibilidad de chefs y turnos en la cocina. Se validará creando un pedido para un turno específico.
73. Filtrado de platos por dietas especiales
Los clientes podrán filtrar el menú según dietas especiales como vegana, vegetariana o sin gluten. Se validará haciendo búsquedas en el menú y verificando que se muestra el filtro correcto.
74. Visualización de platos más pedidos
El sistema mostrará los platos más solicitados en un restaurante. Se validará haciendo varios pedidos y comprobando que los platos populares se actualizan correctamente.
75. Pedido múltiple desde varias mesas
Los camareros podrán hacer pedidos desde diferentes mesas en una sola orden. Se validará realizando pedidos desde varias mesas y confirmando que llegan agrupados.
76. Opción de dividir platos entre varios clientes
Los clientes podrán compartir un plato dividiendo porciones y costos entre varios usuarios. Se validará haciendo un pedido compartido y verificando que el sistema divide correctamente.
77. Integración con programas de lealtad
El sistema se integrará con programas de puntos o recompensas para clientes frecuentes. Se probará realizando pedidos y verificando que se acumulan puntos en el programa de lealtad.
78. Alerta de confirmación de pedido duplicado
El sistema alertará al cliente si intenta hacer un pedido que ya ha realizado recientemente. Se validará haciendo dos pedidos idénticos y revisando que se muestra la alerta.
79. Menú dinámico basado en disponibilidad de chefs
Los platos en el menú se mostrarán u ocultarán en función de la disponibilidad de chefs capacitados para prepararlos. Se validará modificando la disponibilidad de los chefs y revisando los cambios en el menú.
80. Pedidos agrupados por mesa
Los pedidos que provienen de una misma mesa se agruparán automáticamente para facilitar la entrega. Se validará haciendo varios pedidos desde la misma mesa y comprobando que llegan juntos a la cocina.
81. Personalización del tamaño de las porciones
El cliente podrá elegir el tamaño de las porciones para cada plato. Se probará realizando pedidos con diferentes tamaños de porciones.
82. Cancelación automática de pedidos inactivos
Si un pedido no se confirma después de un tiempo determinado, será cancelado automáticamente. Se validará creando un pedido sin confirmar y verificando que el sistema lo cancela tras el tiempo límite.
83. Pedido exprés desde historial
El cliente podrá hacer un pedido rápido seleccionando uno de sus pedidos previos desde el historial. Se validará probando la opción de "pedido exprés".
84. Opción de menú en modo familiar
El cliente podrá hacer pedidos de tamaño familiar o para grupos grandes. Se validará creando un pedido para múltiples personas y verificando que el sistema ajusta las porciones y el precio.
85. Visualización de pedidos en cola por cliente
Los clientes podrán ver en tiempo real cuántos pedidos están antes del suyo en la cola de la cocina. Se validará haciendo varios pedidos y verificando el número de pedidos en espera.
86. Registro de preferencias de clientes registrados
Los clientes registrados podrán guardar sus preferencias de comida para futuros pedidos. Se validará haciendo un pedido y comprobando que las preferencias se guardan correctamente.
87. Control de acceso para personal de cocina
El sistema permitirá asignar diferentes niveles de acceso al personal de cocina (chef, ayudante, administrador). Se validará configurando usuarios con diferentes roles y verificando los permisos.
88. Opción de agregar notas especiales para el pedido
El cliente podrá añadir notas especiales o comentarios adicionales para la cocina. Se validará añadiendo notas y verificando que lleguen a la cocina.
89. Visualización del progreso de la preparación:
El cliente podrá ver una barra de progreso que muestra en qué etapa se encuentra la preparación de su pedido. Se validará haciendo un pedido y revisando el estado de la barra de progreso.
90. Pedidos de bebidas por separado
El cliente podrá hacer pedidos de bebidas independientemente de los platos principales, incluso durante la preparación de un pedido ya existente. Se validará haciendo un pedido de bebidas separado.

