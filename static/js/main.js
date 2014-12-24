$(document).ready(function() {
	if (window.location.pathname == '/cuentas/login/') {
		$('#id_username').addClass('form-control');
		$('#id_password').addClass('form-control');
	};
	if (window.location.pathname == '/cuentas/registro/') {
		$('#id_username').addClass('form-control');
		$('#id_nombre').addClass('form-control');
		$('#id_apellido').addClass('form-control');
		$('#id_email').addClass('form-control');
		$('#id_password1').addClass('form-control');
		$('#id_password2').addClass('form-control');
	};
});