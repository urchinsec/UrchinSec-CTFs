from flask import Flask, render_template, request, abort, render_template_string
from model import db, Note
from helpers import SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = SECRET_KEY

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        title = request.form.get('title')
        description = request.form.get('description')
        comment = request.form.get('comment')
        user_ip = request.remote_addr

        if title is not None and description is not None and username is not None:
            create_note = Note(user_ip, username, title, description, comment)
            db.session.add(create_note)
            db.session.commit()

            # confirm that it's uploaded and fetch it's ID for URL
            check_note = Note.query.filter_by(title=title).first()
            if check_note is not None:
                return render_template('index.html', note_link=f"<a href='/{check_note.username}/note/{check_note.id}'>Visit Note</a>")
            else:
                return render_template('index.html', note_link="Something Went Wrong")
        else:
            return render_template('index.html', note_link="No Input Provided")


@app.route('/<username>/note/<id>', methods=['GET'])
def get_note(username, id):
    # fetch the note_id from the model
    note = Note.query.filter_by(id=id).first()
    if note is not None:
        # check if username inserted matches the note
        if note.username == username:
            return f"""{note.title}
                       {note.description}
                    """
        else:
            return abort(403)
    else:
        return abort(404)


@app.route('/<username>/note/<id>/comment', methods=['GET'])
def get_comments_note(username, id):
    note = Note.query.filter_by(id=id).first()
    if note is not None:
        # check if username inserted matches the note
        if note.username == username:
            return render_template_string(note.comment)
        else:
            return abort(403)
    else:
        return abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)