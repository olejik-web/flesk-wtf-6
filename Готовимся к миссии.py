from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('id ����������', validators=[DataRequired()])
    password = PasswordField('������ ����������', validators=[DataRequired()])
    cap_name = StringField('id ��������', validators=[DataRequired()])
    cap_password = PasswordField('������ ��������', validators=[DataRequired()])
    submit = SubmitField('������')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='�����������', form=form)


@app.route('/index/<name>')
def index(name):
    return render_template('base.html', title=name)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', list=list)


@app.route('/auto_answer')
@app.route('/answer')
def answer():
    dictt = {
        'title': '������ �. �.',
        'surname': '��������',
        'name': '����',
        'education': '���� ��������',
        'profession': '������� ���������',
        'sex': 'male',
        'motivation': '������ ������ �������� �� �����!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', dict=dictt, title=dictt['title'])


@app.route('/distribution')
def distribution():
    return render_template('distribution.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')