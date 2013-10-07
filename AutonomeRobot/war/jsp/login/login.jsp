<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<!-- The HTML 4.01 Transitional DOCTYPE declaration-->
<!-- above set at the top of the file will set     -->
<!-- the browser's rendering engine into           -->
<!-- "Quirks Mode". Replacing this declaration     -->
<!-- with a "Standards Mode" doctype is supported, -->
<!-- but may lead to some differences in layout.   -->

<html>
<head>
<%@include file="/WEB-INF/inc/head.jsp"%>
</head>
<body>
<div data-role="page">
<div data-role="header" data-id='header' data-position="fixed">
		<h1>Login</h1>
</div><!-- /header -->
<div data-role="content">
<%
String msg = (request.getParameter("msg")==null) ? "" : request.getParameter("msg");
%>
<form method='post' action='/login'>
<p style='color:red;'><%= msg%>
<p>Gebruikersnaam<input type='text' name='username'>
Wachtwoord<input type='password' name='password'>
<p><input type='submit' value='AANMELDEN'>
<p><a href='/jsp/register/register.jsp'>Nieuw account maken</a>
</form>
</div><!-- /content -->
</div><!-- /page -->
</body>
</html>