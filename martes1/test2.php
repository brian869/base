<?php
    $meses = array("Enero","Febrero", "Marzo",
                   "Abril", "Mayo", "Junio",
                   "Octubre", "Noviembre", "Diciembre");

$fecha = date("Y-m-d");
$dia = date("d");
$mes = date("n");
$año = date("Y");
$nombre = "brian";
echo "Hoy es el dia $dia del mes $mes del año $año";
print("hola ".$nombre);