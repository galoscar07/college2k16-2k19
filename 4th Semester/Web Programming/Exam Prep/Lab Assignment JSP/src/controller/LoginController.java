package controller;

import domain.User;
import model.DataBaseManager;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

public class LoginController extends HttpServlet {
    public LoginController(){super();}

    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response) throws ServletException, IOException
    {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        RequestDispatcher requestDispatcher = null;

        DataBaseManager dataBaseManager = new DataBaseManager();
        User user = dataBaseManager.autenticate(username, password);
        if( user != null)
        {
            requestDispatcher = request.getRequestDispatcher("/succes.jsp");
            HttpSession session = request.getSession();
            session.setAttribute("user", user);

        }
        else
        {
            requestDispatcher = request.getRequestDispatcher("/error.jsp");

        }
        requestDispatcher.forward(request, response);

    }
}
