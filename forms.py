from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):
    name = StringField('Project Name', validators=[DataRequired()])
    features = SelectMultipleField('Select Features', choices=[
        ('profile', 'Profile Management'),
        ('record_keeping', 'Record Keeping'),
        ('performance_metrics', 'Performance Metrics'),
        ('health_records', 'Health Records'),
        ('financial_tracking', 'Financial Tracking'),
        ('scheduling', 'Scheduling'),
        ('documentation', 'Documentation'),
        ('user_management', 'User Management'),
        ('reporting', 'Reporting'),
        ('feedback_system', 'Feedback System'),
        ('data_import_export', 'Data Import/Export'),
        ('search_filter', 'Search and Filter'),
        ('integration', 'Integration'),
        ('notifications', 'Notifications'),
        ('analytics_dashboard', 'Analytics Dashboard')
    ])
    submit = SubmitField('Create Project')

class SpecificProfileForm(FlaskForm):
    profile_name = StringField('Profile Name', validators=[DataRequired()])
    profile_id = StringField('Profile ID', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    details = StringField('Profile Details (JSON)', validators=[DataRequired()])
    submit = SubmitField('Add Profile')