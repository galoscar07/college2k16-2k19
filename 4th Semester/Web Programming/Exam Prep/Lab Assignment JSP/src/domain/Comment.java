package domain;

public class Comment {
    private int id;
    private int userId;
    private int topicId;
    private String comment;
    public static int generatedId = 0;


    public Comment(int userId, int topicId, String comment) {
        this.generateId();
        this.topicId = topicId;
        this.userId = userId;
        this.comment = comment;
    }
    public Comment(int id, int userId, int topicId, String comment) {
        this.id = id;
        this.topicId = topicId;
        this.userId = userId;
        this.comment = comment;
    }

    private void generateId()
    {
        generatedId = generatedId + 1;
        this.id = generatedId;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public int getTopicId() {
        return topicId;
    }

    public int getId() {

        return id;
    }

    public int getUserId() {
        return userId;
    }

    public String getComment() {
        return comment;
    }
}
