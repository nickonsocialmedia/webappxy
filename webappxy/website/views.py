# views.py
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, Post, User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/profile', methods=['GET', 'POST'])
@login_required
def home():
    if current_user.is_authenticated:
        # Render the profile page for authenticated users
        return render_template("home.html", user=current_user)

    # Render the landing page for unauthenticated users
    return render_template("landing.html", user=current_user)


@views.route('/')
def landing():
    # Render the landing page
    return render_template("landing.html", user=current_user)


@views.route('/home', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        note = request.form.get('note')  # Gets the note from the HTML

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)  # providing the schema for the note
            db.session.add(new_note)  # adding the note to the database
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/maze')
@login_required
def maze():
    return render_template('maze.html', depth=5, user=current_user)  # Adjust depth as needed


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)  # this function expects a JSON from the INDEX.js file
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/forum', methods=['GET', 'POST'])
@login_required
def forum():
    if request.method == 'POST':
        post_content = request.form.get('post_content')

        if not post_content:
            flash('Post content cannot be empty!', category='error')
        else:
            new_post = Post(content=post_content, author=current_user)
            db.session.add(new_post)
            db.session.commit()
            flash('Post added!', category='success')

    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('forum.html', user=current_user, posts=posts)


@views.route('/update-profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        bio = request.form.get('bio')
        # Update user's profile information
        current_user.full_name = full_name
        current_user.bio = bio

        db.session.commit()
        flash('Profile updated successfully!', category='success')
        return redirect(url_for('views.home'))

    return render_template('update_profile.html', user=current_user)


@views.route('/21')
def page_21():
    return render_template('maze_folder/21.html', user=current_user)


@views.route('/22')
def page_22():
    return render_template('maze_folder/22.html', user=current_user)


@views.route('/23')
def page_23():
    return render_template('maze_folder/23.html', user=current_user)


@views.route('/24')
def page_24():
    return render_template('maze_folder/24.html', user=current_user)


@views.route('/25')
def page_25():
    return render_template('maze_folder/25.html', user=current_user)


@views.route('/26')
def page_26():
    return render_template('maze_folder/26.html', user=current_user)


@views.route('/27')
def page_27():
    return render_template('maze_folder/27.html', user=current_user)


@views.route('/28')
def page_28():
    return render_template('maze_folder/28.html', user=current_user)


@views.route('/29')
def page_29():
    return render_template('maze_folder/29.html', user=current_user)


@views.route('/30')
def page_30():
    return render_template('maze_folder/30.html', user=current_user)


@views.route('/31')
def page_31():
    return render_template('maze_folder/31.html', user=current_user)


@views.route('/32')
def page_32():
    return render_template('maze_folder/32.html', user=current_user)


@views.route('/33')
def page_33():
    return render_template('maze_folder/33.html', user=current_user)


@views.route('/34')
def page_34():
    return render_template('maze_folder/34.html', user=current_user)


@views.route('/35')
def page_35():
    return render_template('maze_folder/35.html', user=current_user)


@views.route('/36')
def page_36():
    return render_template('maze_folder/36.html', user=current_user)


@views.route('/37')
def page_37():
    return render_template('maze_folder/37.html', user=current_user)


@views.route('/38')
def page_38():
    return render_template('maze_folder/38.html', user=current_user)


@views.route('/39')
def page_39():
    return render_template('maze_folder/39.html', user=current_user)


@views.route('/40')
def page_40():
    return render_template('maze_folder/40.html', user=current_user)


@views.route('/41')
def page_41():
    return render_template('maze_folder/41.html', user=current_user)


@views.route('/42')
def page_42():
    return render_template('maze_folder/42.html', user=current_user)


@views.route('/43')
def page_43():
    return render_template('maze_folder/43.html', user=current_user)


@views.route('/44')
def page_44():
    return render_template('maze_folder/44.html', user=current_user)


@views.route('/45')
def page_45():
    return render_template('maze_folder/45.html', user=current_user)


@views.route('/46')
def page_46():
    return render_template('maze_folder/46.html', user=current_user)


@views.route('/47')
def page_47():
    return render_template('maze_folder/47.html', user=current_user)


@views.route('/48')
def page_48():
    return render_template('maze_folder/48.html', user=current_user)


@views.route('/49')
def page_49():
    return render_template('maze_folder/49.html', user=current_user)


@views.route('/50')
def page_50():
    return render_template('maze_folder/50.html', user=current_user)


@views.route('/51')
def page_51():
    return render_template('maze_folder/51.html', user=current_user)


@views.route('/52')
def page_52():
    return render_template('maze_folder/52.html', user=current_user)


@views.route('/53')
def page_53():
    return render_template('maze_folder/53.html', user=current_user)


@views.route('/54')
def page_54():
    return render_template('maze_folder/54.html', user=current_user)


@views.route('/55')
def page_55():
    return render_template('maze_folder/55.html', user=current_user)


@views.route('/56')
def page_56():
    return render_template('maze_folder/56.html', user=current_user)


@views.route('/57')
def page_57():
    return render_template('maze_folder/57.html', user=current_user)


@views.route('/58')
def page_58():
    return render_template('maze_folder/58.html', user=current_user)


@views.route('/59')
def page_59():
    return render_template('maze_folder/59.html', user=current_user)


@views.route('/60')
def page_60():
    return render_template('maze_folder/60.html', user=current_user)


@views.route('/61')
def page_61():
    return render_template('maze_folder/61.html', user=current_user)


@views.route('/62')
def page_62():
    return render_template('maze_folder/62.html', user=current_user)


@views.route('/63')
def page_63():
    return render_template('maze_folder/63.html', user=current_user)


@views.route('/64')
def page_64():
    return render_template('maze_folder/64.html', user=current_user)


@views.route('/65')
def page_65():
    return render_template('maze_folder/65.html', user=current_user)


@views.route('/66')
def page_66():
    return render_template('maze_folder/66.html', user=current_user)


@views.route('/67')
def page_67():
    return render_template('maze_folder/67.html', user=current_user)


@views.route('/68')
def page_68():
    return render_template('maze_folder/68.html', user=current_user)


@views.route('/69')
def page_69():
    return render_template('maze_folder/69.html', user=current_user)


@views.route('/70')
def page_70():
    return render_template('maze_folder/70.html', user=current_user)


@views.route('/71')
def page_71():
    return render_template('maze_folder/71.html', user=current_user)


@views.route('/72')
def page_72():
    return render_template('maze_folder/72.html', user=current_user)


@views.route('/73')
def page_73():
    return render_template('maze_folder/73.html', user=current_user)


@views.route('/74')
def page_74():
    return render_template('maze_folder/74.html', user=current_user)


@views.route('/75')
def page_75():
    return render_template('maze_folder/75.html', user=current_user)


@views.route('/76')
def page_76():
    return render_template('maze_folder/76.html', user=current_user)


@views.route('/77')
def page_77():
    return render_template('maze_folder/77.html', user=current_user)


@views.route('/78')
def page_78():
    return render_template('maze_folder/78.html', user=current_user)


@views.route('/79')
def page_79():
    return render_template('maze_folder/79.html', user=current_user)


@views.route('/80')
def page_80():
    return render_template('maze_folder/80.html', user=current_user)


@views.route('/81')
def page_81():
    return render_template('maze_folder/81.html', user=current_user)


@views.route('/82')
def page_82():
    return render_template('maze_folder/82.html', user=current_user)


@views.route('/83')
def page_83():
    return render_template('maze_folder/83.html', user=current_user)


@views.route('/84')
def page_84():
    return render_template('maze_folder/84.html', user=current_user)


@views.route('/85')
def page_85():
    return render_template('maze_folder/85.html', user=current_user)


@views.route('/86')
def page_86():
    return render_template('maze_folder/86.html', user=current_user)


@views.route('/87')
def page_87():
    return render_template('maze_folder/87.html', user=current_user)


@views.route('/88')
def page_88():
    return render_template('maze_folder/88.html', user=current_user)


@views.route('/89')
def page_89():
    return render_template('maze_folder/89.html', user=current_user)


@views.route('/90')
def page_90():
    return render_template('maze_folder/90.html', user=current_user)


@views.route('/91')
def page_91():
    return render_template('maze_folder/91.html', user=current_user)


@views.route('/92')
def page_92():
    return render_template('maze_folder/92.html', user=current_user)


@views.route('/93')
def page_93():
    return render_template('maze_folder/93.html', user=current_user)


@views.route('/94')
def page_94():
    return render_template('maze_folder/94.html', user=current_user)


@views.route('/95')
def page_95():
    return render_template('maze_folder/95.html', user=current_user)


@views.route('/96')
def page_96():
    return render_template('maze_folder/96.html', user=current_user)


@views.route('/97')
def page_97():
    return render_template('maze_folder/97.html', user=current_user)


@views.route('/98')
def page_98():
    return render_template('maze_folder/98.html', user=current_user)


@views.route('/99')
def page_99():
    return render_template('maze_folder/99.html', user=current_user)
