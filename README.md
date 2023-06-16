Prueba Tecnica

Se debe desarrollar sitio web en el que se registran pedido de préstamos de usuarios que acceden a él.

El usuario no necesita registrarse para solicitar un préstamo.
Para definir si al usuario se le aprueba o no el préstamo usaremos una API definida debajo.

endpoint: https://api.moni.com.ar/api/v4/scoring/pre-score/[dni]
tenés que pasarle en los headers credential: ZGpzOTAzaWZuc2Zpb25kZnNubm5u

ejemplo: curl https://api.moni.com.ar/api/v4/scoring/pre-score/30156149 -H "credential: ZGpzOTAzaWZuc2Zpb25kZnNubm5u"

En el formulario de pedido de préstamos, el usuario debe ingresar dni, nombre y apellido, género, email y monto solicitado.

El usuario luego de ingresar los datos debe recibir la respuesta negativa o positiva en la misma página que ingresó sus datos.
Contemplar casos de datos ingresados con errores.

También se debe desarrollar un sitio de administración en el que se puedan ver los pedidos de préstamo, con la opción de editarlos y eliminarlos. A este sitio sólo pueden acceder usuarios administradores. No usar admin de Django.