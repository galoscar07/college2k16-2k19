//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

package controller;

import domain.Topic;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import model.DataBaseManager;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;


public class TopicController extends HttpServlet {
    public TopicController() {
        super();
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");

        if (action != null && action.equals("getAll")) {
            int userId = Integer.parseInt(request.getParameter("userid"));
            response.setContentType("application/json");
            DataBaseManager manager = new DataBaseManager();
            ArrayList<Topic> topics = manager.getUserTopics(userId);
            JSONArray jsonTopics = new JSONArray();

            for(int i = 0; i < topics.size(); ++i) {
                JSONObject jobj = new JSONObject();

                jobj.put("id", ((Topic)topics.get(i)).getId());
                jobj.put("userid", ((Topic)topics.get(i)).getUserId());
                jobj.put("title", ((Topic)topics.get(i)).getTitle());
                jobj.put("comments", ((Topic)topics.get(i)).getComments1());
                jsonTopics.add(jobj);
            }

            PrintWriter out = new PrintWriter(response.getOutputStream());
            out.println(jsonTopics.toJSONString());
            out.flush();
        }else if(action != null && action.equals("comment"))
        {
            int userId = Integer.parseInt(request.getParameter("userId"));
            int topicId = Integer.parseInt(request.getParameter("topicId"));
            String commentary = request.getParameter("comment");
            DataBaseManager manager = new DataBaseManager();
            PrintWriter out = new PrintWriter(response.getOutputStream());
            Boolean result = manager.leaveComment(topicId, userId, commentary);
            if(result)
            {
                out.println("Comment Added !");
            }
            else {
                out.println("No Comm Added!");
            }
            out.flush();

        }

    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {


        int id = Integer.parseInt(request.getParameter("uId"));
        String title = request.getParameter("title");
        DataBaseManager manager = new DataBaseManager();
        Boolean result = manager.createTopic(id, title);
        PrintWriter out = new PrintWriter(response.getOutputStream());
        if(result)
        {
            out.println("New topic created !!");
        }else {
            out.println("Failed to create topic!");
        }
        out.flush();

    }

}
