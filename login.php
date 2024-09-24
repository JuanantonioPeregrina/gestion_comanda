<?php
session_start(); // Iniciar sesión para manejar mensajes de error

// Datos de ejemplo en el archivo o en la base de datos para validación
$usuarios_validos = [
    'ceo@comanda.com' => '1',
    'usuario2@example.com' => 'password2'
];

// Obtener el correo y contraseña del formulario
$email = $_POST['email'];
$password = $_POST['password'];

// Verificar si el correo existe en la lista de usuarios válidos
if (isset($usuarios_validos[$email]) && $usuarios_validos[$email] === $password) {
    // Si el correo y la contraseña son correctos, redirigir al área protegida
    header("Location: protected.php");
    exit();
} else {
    // Si las credenciales no son correctas, guardar un mensaje de error en la sesión
    $_SESSION['error'] = "Correo electrónico o contraseña incorrectos. Por favor, intente nuevamente.";
    header("Location: login.php"); // Redirigir a la página de inicio de sesión
    exit();
}
?>

