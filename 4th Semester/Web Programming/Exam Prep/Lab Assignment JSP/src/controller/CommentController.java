package controller;

import model.DataBaseManager;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

public class CommentController extends HttpServlet {
    public CommentController() {
        super();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int userId = Integer.parseInt(request.getParameter("userId"));
        int topicId = Integer.parseInt(request.getParameter("topicId"));
        DataBaseManager manager = new DataBaseManager();
        Boolean result;
        result = manager.removeComment(userId, topicId);
        PrintWriter out = new PrintWriter(response.getOutputStream());
        if(result){
            out.println("Comment deleted!");
        }else {
            out.println("Failed to delete!");
        }
        out.flush();
    }
}
