package servlet;

import java.io.IOException;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import util.RegistryInitializer;
import Model.User;

public class ControlServlet extends HttpServlet {
	
	private static final long serialVersionUID = -786837324508180891L;
	
	public void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
		HttpSession session = req.getSession();
		if(!RegistryInitializer.initialized()){
			RegistryInitializer.initialize(session.getServletContext());
		}
	User user = (User)session.getAttribute("user");
	
	if(user!=null){
		
	} else {
		resp.sendRedirect("/jsp/login/login.jsp");
	}
}
}
