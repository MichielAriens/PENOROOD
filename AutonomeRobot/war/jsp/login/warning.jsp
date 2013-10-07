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
<div data-role="dialog" id="dialog_login_warning" class="app-dialog">
<div data-role="header" data-id='header' data-position="fixed">
</div><!-- /header -->
<div data-role="content">
<form method='post' action='/register'>
	<h2>U hebt nog geen vakken!</h2>
	<p>Wilt u deze nu aanduiden?</p>
	<button type="submit" name="submit" value="register2" data-inline="true" data-icon="check">Ja</button>
	<a href="/track" data-role="button" data-inline="true" data-icon="delete">Nee</a>
</form>
</div><!-- /content -->
</div><!-- /dialog -->
</body>
</html>