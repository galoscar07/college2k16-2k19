

function getUserTopics(userid, callbackFunction) {
    $.getJSON(
        "TopicController",
        { action: 'getAll', userid: userid },
        callbackFunction
    );
}

function commentOnTopic(userId, topicId, comment, callbackFunction) {
    $.get("TopicController",
        { action: "comment",
            userId: userId,
            topicId: topicId,
            comment: comment
        },
        callbackFunction
    );
}
function createTopic(userId, title, callbackFunction) {

    $.post(
        "TopicController",
        {
            uId: userId,
            title: title
        },
        callbackFunction
    );
}
function deleteComment(userId, topicId, callbackFunction){
    $.get(
        "CommentController",
        {
            userId:userId,
            topicId:topicId
        },
        callbackFunction
    );
}
function godDamnDeleteTheComment(userId, topicId, callbackFunction) {
    $.get(
        "CommentController",
        {
            userId:userId,
            topicId:topicId
        },
        callbackFunction
    );
}
