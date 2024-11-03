from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from website.models import Topic, Thread, Comment, GeminiComment
from website import db
from website.pages.gemini_reply import gemini_reply

forum_page = Blueprint ('forum_page', __name__, template_folder='/templates')


@forum_page.route ('/forum', methods = ['GET', 'POST'])
@login_required
def topic ():
    # adding new topic to database
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        topic =  Topic(title = title, description = description)
        db.session.add (topic)
        db.session.commit ()

    # retrieve topics
    topics = db.session.execute (db.select(Topic)).scalars ()

    return render_template ("forum_topic.html", user=current_user, topics=topics)

@forum_page.route ('/forum/<title>', methods = ['GET', 'POST'])
@login_required
def thread (title):
    # adding new thread to database
    if request.method == 'POST':
        thread_title = request.form.get('title')
        thread_description = request.form.get('description')
        threads = Thread (title = thread_title, description = thread_description, topic_title=title)
        db.session.add (threads)
        db.session.commit ()

    # retrieve comments
    threads = Thread.query.filter_by (topic_title=title).all ()

    # retrieve topic
    topic = Topic.query.get(title)

    return render_template ("forum_thread.html", user=current_user, threads=threads, topic=topic)

@forum_page.route ('/forum/<title>/<int:id>', methods = ['GET', 'POST'])
@login_required
def comment (title, id):
    # adding new topic to database
    if request.method == 'POST':
        comment = Comment (comment = request.form['comment'], thread_id=id)
        db.session.add (comment)
        db.session.commit ()

        # gemini's reply
        reply = gemini_reply (request.form['comment'])
        gemini_comment = GeminiComment (comment=reply, comment_id=comment.id, thread_id=id)
        db.session.add (gemini_comment)
        db.session.commit ()

    # retrieve topic
    topic = Topic.query.get(title)
    
    # retrieve thread
    thread = Thread.query.get(id)

    # retrieve comments
    comments = Comment.query.filter_by (thread_id=id).all ()
    print (f'comments: {comments}')

    # retrieve gemini replies
    gemini_replies  = GeminiComment.query.filter_by (thread_id=id).all ()
    print (f'gemini replies: {gemini_replies}')

    return render_template ("forum_comment.html", user=current_user, topic=topic, thread=thread, comments=comments, gemini_replies=gemini_replies)