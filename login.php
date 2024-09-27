<?php
session_start(); // Iniciar sesión para manejar mensajes de error

// Archivo donde se almacenan los usuarios válidos
$archivo_usuarios = 'usuarios.json';

// Verificar si el archivo de usuarios existe, si no, crearlo
if (!file_exists($archivo_usuarios)) {
    file_put_contents($archivo_usuarios, json_encode([]));
}

// Obtener el contenido del archivo JSON
$contenido_json = file_get_contents($archivo_usuarios);
$usuarios_validos = json_decode($contenido_json, true);

// Obtener el correo y la contraseña del formulario
$email = $_POST['email'];
$password = $_POST['password'];

// Verificar si el correo existe en la lista de usuarios válidos
if (isset($usuarios_validos[$email]) && $usuarios_validos[$email] === $password) {
    // Si el correo y la contraseña son correctos, redirigir a la página principal
    header("Location: PaginaPrincipal.html");
    exit();
} else {
    // Si las credenciales no son correctas, guardar un mensaje de error en la sesión
    $_SESSION['error'] = "Correo electrónico o contraseña incorrectos. Por favor, intente nuevamente.";
    header("Location: InicioSesion2.html"); // Redirigir a la página de inicio de sesión
    exit();
}
?>

