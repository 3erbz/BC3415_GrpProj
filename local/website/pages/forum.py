from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from website.models import Comment, Topic, GeminiComment
from website import db
from website.pages.gemini_reply import gemini_reply

forum_page = Blueprint ('forum_page', __name__, template_folder='/templates')
@forum_page.route ('/forum', methods = ['GET', 'POST'])
@login_required
def forum ():
    # adding new topic to database
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        topic = Topic (title = title, description = description)
        db.session.add (topic)
        db.session.commit ()

    # retrieve topics
    topics = db.session.execute (db.select(Topic)).scalars ()

    return render_template ("forum_topic.html", user=current_user, topics=topics)

@forum_page.route ('/forum/<int:id>', methods = ['GET', 'POST'])
@login_required
def comment (id):
    # adding new topic to database
    if request.method == 'POST':
        comment = Comment (comment = request.form['comment'], topicID=id)
        db.session.add (comment)
        db.session.commit ()

        # gemini's reply
        reply = gemini_reply (request.form['comment'])
        gemini_comment = GeminiComment (comment = reply, comment_id=comment.id, topicID=id)
        db.session.add (gemini_comment)
        db.session.commit ()

    # retrieve topic
    topic = db.get_or_404 (Topic, id)

    # retrieve comments
    comments = Comment.query.filter_by (topicID=id).all ()

    # retrieve gemini replies
    gemini_replies  = GeminiComment.query.filter_by (topicID=id).all ()

    return render_template ("forum_comment.html", user=current_user, topic=topic, comments=comments, gemini_replies=gemini_replies)