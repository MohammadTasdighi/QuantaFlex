from flask import Flask, render_template, redirect, url_for, flash
from models import db, Project, EntityProfile, SpecificProfile
from forms import ProjectForm, SpecificProfileForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    form = ProjectForm()
    if form.validate_on_submit():
        new_project = Project(name=form.name.data, features=form.features.data)
        db.session.add(new_project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('user_projects'))
    return render_template('create_project.html', form=form)

@app.route('/user_projects')
def user_projects():
    projects = Project.query.all()
    return render_template('user_projects.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_details(project_id):
    project = Project.query.get_or_404(project_id)
    profiles = EntityProfile.query.filter_by(project_id=project.id).all()
    return render_template('project_details.html', project=project, profiles=profiles)

@app.route('/add_profile/<int:entity_id>', methods=['GET', 'POST'])
def add_profile(entity_id):
    form = SpecificProfileForm()
    if form.validate_on_submit():
        new_profile = SpecificProfile(
            entity_id=entity_id,
            profile_name=form.profile_name.data,
            profile_id=form.profile_id.data,
            age=form.age.data,
            profile_details=form.details.data
        )
        db.session.add(new_profile)
        db.session.commit()
        flash('Profile added successfully!', 'success')
        return redirect(url_for('view_profiles', entity_id=entity_id))
    
    return render_template('add_profile.html', form=form)

@app.route('/profiles/<int:entity_id>')
def view_profiles(entity_id):
    profiles = SpecificProfile.query.filter_by(entity_id=entity_id).all()
    return render_template('view_profiles.html', profiles=profiles, entity_id=entity_id)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)