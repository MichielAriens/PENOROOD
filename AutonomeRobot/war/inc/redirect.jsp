<%

if(request.getSession().getAttribute("student")==null){
	response.sendRedirect("/login.jsp?msg=Beveiligde pagina");
}

%>