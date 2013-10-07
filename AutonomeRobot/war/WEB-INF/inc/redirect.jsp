<%

if(request.getSession().getAttribute("student")==null){
	response.sendRedirect("/jsp/login/login.jsp?msg=Om deze pagina te bekijken moet je eerst inloggen!");
}

%>