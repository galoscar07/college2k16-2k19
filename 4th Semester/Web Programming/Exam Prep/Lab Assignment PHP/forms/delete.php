<?php
	session_start();
	include '../functions/remove.php';
	remove_car($_GET['id']);
	header('Location: ../index.php?deleted=success');
?>