package model;

import domain.Comment;
import domain.Topic;
import domain.User;


import java.sql.*;
import java.util.ArrayList;

public class DataBaseManager {
    private Statement stmt;
    private Statement stmt1;

    public DataBaseManager()
    {
        connect();
    }
    public void connect()
    {
        ResultSet rs;
        try
        {
            Class.forName("org.postgresql.Driver");
            Connection conn = DriverManager.getConnection("jdbc:postgresql://localhost:5432/UserForum","postgres", "accele123");

            stmt = conn.createStatement();
            stmt1 = conn.createStatement();
            rs = stmt.executeQuery("select topics.id from topics order by topics.id desc limit 1");
            if(rs.next())
            {
                Topic.genId = rs.getInt("id");

            }else
            {
                Topic.genId = 0;
            }
            rs = stmt.executeQuery("select comments.id from comments order by comments.id desc limit 1");
            if(rs.next())
            {
                Comment.generatedId = rs.getInt("id");

            }else {
                Comment.generatedId = 0;
            }
        }catch (Exception e)
        {
            System.out.println("Connection error"+e.getMessage());
            e.printStackTrace();
        }
    }
    public User autenticate(String username, String password)
    {
        ResultSet rs;
        User user = null;
        System.out.println(username+" "+password);
        try
        {
            rs = stmt.executeQuery("select * from users where users.user='"+username+"' and users.password= '"+password+"'");

            if (rs.next()) {

                user = new User(rs.getInt("id"), rs.getString("user"), rs.getString("password"));
            }
            rs.close();
        }catch (SQLException e)
        {
            e.printStackTrace();
        }

        return user;

    }
    public ArrayList<Topic> getUserTopics(int userId)
    {

        ArrayList<Topic> topics = new ArrayList<>();
        ArrayList<Comment> comment = new ArrayList<>();
        ResultSet rs;
        ResultSet rs1;
        try
        {
            rs = stmt.executeQuery(
                    "SELECT * " +
                            "FROM topics"
            );
            while(rs.next())
            {


                rs1 = stmt1.executeQuery(
                        "select * from comments where comments.topicid='"+rs.getInt("id")+"'"
                );

                while (rs1.next())
                {

                    comment.add(
                            new Comment(
                                    rs1.getInt("id"),
                                    rs1.getInt("userid"),
                                    rs1.getInt("topicId"),
                                    rs1.getString("comment")
                            )
                    );

                }


                topics.add(
                        new Topic(
                                rs.getInt("id"),
                                rs.getInt("userid"),
                                rs.getString("title")
                                )
                );


            }


            rs.close();

        }catch (SQLException e) {
            e.printStackTrace();
        }
        topics.forEach(topic -> comment.forEach(comment1 -> {
            if(topic.getId() == comment1.getTopicId()){
                topic.getComments().add(comment1);

            }
        }));

        return topics;
    }
    public boolean createTopic(int userId, String title)
    {
        Topic topic = new Topic(userId, title);

        int ok = 0;
        try{
            ok = stmt.executeUpdate(
                    "insert into topics values"+
                            "('"+topic.getId()+"','"+topic.getUserId()+"','"+topic.getTitle()+"',null)"
            );

        }catch (SQLException e) {
            e.printStackTrace();
        }
        if (ok > 0) return true;
        return false;

    }
    public boolean removeComment(int userId, int topicId){
        int result = 0, result1 = 0;

        try{
            result = stmt.executeUpdate(
                    "Delete from comments where comments.userid='"+userId+"' AND comments.topicid='"+topicId+"'"
            );
            result1 = stmt.executeUpdate(
                    "UPDATE topics set commentid='0' Where id='"+topicId+"'"
            );
        }catch (SQLException e){
            e.printStackTrace();
        }
        if((result>0) && (result1>0))return  true;
        return false;
    }
    public boolean leaveComment(Integer topicId, Integer commentringUserId, String comment)
    {
        Comment C = new Comment(commentringUserId, topicId,comment);
        //topic.getComments().add(C);
        int r = 0;
        try
        {

            stmt.executeUpdate(
                    "insert into comments values"+
                            "('"+C.getId()+"','"+C.getUserId()+"','"+C.getComment()+"','"+C.getTopicId()+"')"
            );

            r = stmt.executeUpdate(
                    "update topics set commentid='"+C.getId()+
                            "' where id='"+topicId+"'"
            );

        } catch (SQLException e) {
            e.printStackTrace();
        }
        if(r > 0) return true;
        return false;
    }
}
