package domain;


import java.util.ArrayList;


public class Topic {
    private int id;
    private int userId;
    private String title;
    private ArrayList<Comment> comments;


    public static int genId = 0;


    public Topic(int userId, String title) {
        this.id = generateId();
        this.userId = userId;
        this.title = title;
        comments = new ArrayList<>();
    }
    public Topic(int id, int userId, String title) {
        this.id = id;
        this.userId = userId;
        this.title = title;
        this.comments = new ArrayList<>();
       // this.comments.forEach(c ->System.out.println(c.getComment()));

    }
    private int generateId()
    {
        genId = genId + 1;
        return genId;
    }

    public ArrayList<Comment> getComments() {
        return comments;
    }
    public String getComments1(){
        String result = "";

        for(int i = 0; i < this.comments.size(); i++){

            result = result + "User with ID:"+ this.comments.get(i).getUserId()+ " "+ this.comments.get(i).getComment()+"||\n";

        }
        System.out.println(result);
        return result;
    }

    public void setComments(ArrayList<Comment> comments) {
        this.comments = comments;
    }

    public int getId() {
        return id;
    }

    public int getUserId() {
        return userId;
    }

    public String getTitle() {
        return title;
    }

}
