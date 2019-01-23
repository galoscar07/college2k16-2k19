<%--
  Created by IntelliJ IDEA.
  User: Cata
  Date: 27-May-18
  Time: 14:24
  To change this template use File | Settings | File Templates.
--%>
<%@page import="domain.User" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Forum</title>
    <script src="js/jquery-3.2.1.js"></script>
    <script src="js/ajax-utils.js"></script>
</head>
<body>
<%! User user; %>
<%  user = (User) session.getAttribute("user");
    if (user != null) {
        out.println("Welcome "+user.getUsername());
%>
    <br/>
    <p><button id="getTopicsButton" type="button">Get Topics</button></p>


    <section>
        <span style="font-weight: bold; background-color: mediumpurple">Start a new Topic !</span><br/>
        <table>
            <tr><td>Title: </td><td><input type="text" id="titleOfTopic"></td></tr>
            <tr><td><button type="button" id="addTopic">Create Topic</button></td><td></td></tr>
        </table>
    </section>
    <section id="createResultSection"></section>

    <section><table id="topic-table"></table></section>
    <p style="height: 50px;"></p>
    <section id="leave-comment">
        <span style="font-weight: bold; background-color: mediumseagreen">Leave Comment</span><br/>
        <table>
            <tr><td>Topic Id: </td><td><input type="text" id="topicId"></td></tr>
            <tr><td>Comment: </td><td><input type="text" id="post"></td></tr>
            <tr><td><button type="button" id="commentButton">Submit</button></td><td></td></tr>
        </table>
    </section>
    <section id="commentSection"></section>


    <section id="DeleteMyComments">
        <span style="font-weight: bold; background-color: greenyellow">Delete My Comments</span>
        <table>
            <tr><td>Topic Id: </td><td><input type="text" id="topicIdDelete"></td></tr>
            <tr><td><button type="button" id="deleteCommentBtn">Remove Comments</button></td><td></td></tr>
        </table>
    </section>
    <section id="DeleteResult"></section>
    <script>
        $(document).ready(function(){



            $("#addTopic").click(function () {
                createTopic(<%= user.getId()%> , $("#titleOfTopic").val(), function (response) {
                    $("#createResultSection").html(response)
                })
            });

            $("#getTopicsButton").click(function () {
                getUserTopics(<%= user.getId() %>, function (topics) {
                    console.log(topics);
                    $("#topic-table").html("");
                    $("#topic-table").append("<tr style='background-color: mediumseagreen'><td>Id</td><td>UserId</td><td>Title</td><td>Comments</td></tr>")
                    for(var name in topics)
                    {
                        $("#topic-table").append(
                            "<tr><td class='topic-name'>"+topics[name].id+"</td>"+
                            "<td>"+topics[name].userid+"</td>" +
                            "<td>"+topics[name].title+"</td>" +
                            "<td>"+topics[name].comments+"</td></tr>");
                    }
                })
            });
            $("#commentButton").click(function () {
                commentOnTopic(
                    <%= user.getId()%>,
                    $("#topicId").val(),
                    $("#post").val(),
                    function (response) {
                        $("#commentSection").html(response);
                    }
                )
            });

            $("#deleteCommentBtn").click(function () {
                deleteComment(
                    <%=user.getId()%>,
                    $("#topicIdDelete").val(),
                    function (response) {
                        $("#DeleteResult").html(response);
                    }
                )
            });


        })

    </script>
<%
    }
%>
</body>
</html>
