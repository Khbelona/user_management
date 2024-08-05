# # from flask import Flask, render_template, request, redirect, url_for, flash, session
# # from flask_mail import Mail, Message
# # from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
# # import pandas as pd
# # import os

# # app = Flask(__name__)
# # app.secret_key = 'your_secret_key'

# # app.config.update(
# #     MAIL_SERVER='smtp.gmail.com',
# #     MAIL_PORT=587,
# #     MAIL_USE_TLS=True,
# #     MAIL_USERNAME='your_email@gmail.com',
# #     MAIL_PASSWORD='your_app_password'  # Use the app-specific password here
# # )

# # mail = Mail(app)
# # s = URLSafeTimedSerializer(app.secret_key)
# # excel_file = 'users.xlsx'

# # if not os.path.exists(excel_file):
# #     df = pd.DataFrame(columns=['username', 'email', 'password'])
# #     df.to_excel(excel_file, index=False)

# # @app.route('/')
# # def home():
# #     user = session.get('user')
# #     return render_template('home.html', user=user)

# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     message = None
# #     if request.method == 'POST':
# #         email = request.form['email']
# #         password = request.form['password']
# #         df = pd.read_excel(excel_file)
# #         user = df[(df['email'] == email) & (df['password'] == password)]
# #         if not user.empty:
# #             session['user'] = user.iloc[0].to_dict()
# #             flash('You were successfully logged in')
# #             return redirect(url_for('home'))
# #         else:
# #             message = 'Invalid credentials'
# #     return render_template('login.html', message=message)

# # @app.route('/logout')
# # def logout():
# #     session.pop('user', None)
# #     flash('You were successfully logged out')
# #     return redirect(url_for('home'))

# # @app.route('/register', methods=['GET', 'POST'])
# # def register():
# #     if request.method == 'POST':
# #         username = request.form['username']
# #         email = request.form['email']
# #         password = request.form['password']
# #         confirm_password = request.form['confirm_password']
# #         if password == confirm_password:
# #             df = pd.read_excel(excel_file)
# #             if email in df['email'].values:
# #                 flash('Email already registered')
# #             else:
# #                 new_user = pd.DataFrame([[username, email, password]], columns=['username', 'email', 'password'])
# #                 df = pd.concat([df, new_user], ignore_index=True)
# #                 df.to_excel(excel_file, index=False)
# #                 flash('You have successfully registered')
# #                 return redirect(url_for('login'))
# #         else:
# #             flash('Passwords do not match')
# #     return render_template('register.html')

# # @app.route('/users')
# # def user_list():
# #     df = pd.read_excel(excel_file)
# #     users = df.to_dict(orient='records')
# #     return render_template('user_list.html', users=users)

# # @app.route('/forgot_password', methods=['GET', 'POST'])
# # def forgot_password():
# #     if request.method == 'POST':
# #         email = request.form['email']
# #         df = pd.read_excel(excel_file)
# #         user = df[df['email'] == email]
# #         if not user.empty:
# #             token = s.dumps(email, salt='password-reset-salt')
# #             link = url_for('reset_password', token=token, _external=True)
# #             msg = Message('Password Reset Request', sender='your_email@gmail.com', recipients=[email])
# #             msg.body = f'Your link to reset your password is {link}'
# #             mail.send(msg)
# #             flash('A password reset link has been sent to your email.')
# #             return redirect(url_for('login'))
# #         else:
# #             flash('Email not found')
# #     return render_template('forgot_password.html')

# # @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# # def reset_password(token):
# #     try:
# #         email = s.loads(token, salt='password-reset-salt', max_age=3600)
# #     except (SignatureExpired, BadTimeSignature):
# #         flash('The password reset link is invalid or has expired.')
# #         return redirect(url_for('forgot_password'))

# #     if request.method == 'POST':
# #         new_password = request.form['new_password']
# #         confirm_password = request.form['confirm_password']
# #         if new_password == confirm_password:
# #             df = pd.read_excel(excel_file)
# #             user_index = df.index[df['email'] == email].tolist()[0]
# #             df.at[user_index, 'password'] = new_password
# #             df.to_excel(excel_file, index=False)
# #             flash('Your password has been reset successfully.')
# #             return redirect(url_for('login'))
# #         else:
# #             flash('Passwords do not match')
# #     return render_template('reset_password.html', token=token)

# # @app.route('/password_change', methods=['GET', 'POST'])
# # def password_change():
# #     message = None
# #     if request.method == 'POST':
# #         email = request.form['email']
# #         old_password = request.form['old_password']
# #         new_password = request.form['new_password']
# #         confirm_password = request.form['confirm_password']
# #         df = pd.read_excel(excel_file)
# #         user = df[(df['email'] == email) & (df['password'] == old_password)]
# #         if not user.empty:
# #             if new_password == confirm_password:
# #                 user_index = df.index[df['email'] == email].tolist()[0]
# #                 df.at[user_index, 'password'] = new_password
# #                 df.to_excel(excel_file, index=False)
# #                 flash('Password successfully changed')
# #                 return redirect(url_for('login'))
# #             else:
# #                 message = 'New passwords do not match'
# #         else:
# #             message = 'Invalid email or old password'
# #     return render_template('password_change.html', message=message)

# # if __name__ == '__main__':
# #     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for, flash, session
# from flask_mail import Mail, Message
# from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
# import pandas as pd
# import os

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # app.config.update(
# #     MAIL_SERVER='smtp.gmail.com',
# #     MAIL_PORT=587,
# #     MAIL_USE_TLS=True,
# #     MAIL_USERNAME='your_email@gmail.com',
# #     MAIL_PASSWORD='your_app_password'  # Use the app-specific password here
# # )

# mail = Mail(app)
# s = URLSafeTimedSerializer(app.secret_key)
# user_excel_file = 'users.xlsx'
# student_excel_file = 'students.xlsx'

# if not os.path.exists(user_excel_file):
#     df = pd.DataFrame(columns=['username', 'full_name','email', 'password','DOB','address'])
#     df.to_excel(user_excel_file, index=False)

# if not os.path.exists(student_excel_file):
#     student_df = pd.DataFrame(columns=['roll', 'name', 'email', 'dob', 'address', 'maths_marks', 'english_marks', 'science_marks'])
#     student_df.to_excel(student_excel_file, index=False)

# @app.route('/')
# def home():
#     user = session.get('user')
#     return render_template('home.html', user=user)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     message = None
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         df = pd.read_excel(user_excel_file)
#         user = df[(df['email'] == email) & (df['password'] == password)]
#         if not user.empty:
#             session['user'] = user.iloc[0].to_dict()
#             flash('You were successfully logged in')
#             return redirect(url_for('student_info'))
#         else:
#             message = 'Invalid credentials'
#     return render_template('login.html', message=message)

# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     flash('You were successfully logged out')
#     return redirect(url_for('home'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         confirm_password = request.form['confirm_password']
#         if password == confirm_password:
#             df = pd.read_excel(user_excel_file)
#             if email in df['email'].values:
#                 flash('Email already registered')
#             else:
#                 new_user = pd.DataFrame([[username, email, password]], columns=['username', 'email', 'password'])
#                 df = pd.concat([df, new_user], ignore_index=True)
#                 df.to_excel(user_excel_file, index=False)
#                 flash('You have successfully registered')
#                 return redirect(url_for('login'))
#         else:
#             flash('Passwords do not match')
#     return render_template('register.html')

# @app.route('/users')
# def user_list():
#     df = pd.read_excel(user_excel_file)
#     users = df.to_dict(orient='records')
#     return render_template('user_list.html', users=users)

# # @app.route('/forgot_password', methods=['GET', 'POST'])
# # def forgot_password():
# #     if request.method == 'POST':
# #         email = request.form['email']
# #         df = pd.read_excel(user_excel_file)
# #         user = df[df['email'] == email]
# #         if not user.empty:
# #             token = s.dumps(email, salt='password-reset-salt')
# #             link = url_for('reset_password', token=token, _external=True)
# #             msg = Message('Password Reset Request', sender='your_email@gmail.com', recipients=[email])
# #             msg.body = f'Your link to reset your password is {link}'
# #             mail.send(msg)
# #             flash('A password reset link has been sent to your email.')
# #             return redirect(url_for('login'))
# #         else:
# #             flash('Email not found')
# #     return render_template('forgot_password.html')

# @app.route('/forgot_password', methods=['GET', 'POST'])
# def forgot_password():
#     if request.method == 'POST':
#         email = request.form['email']
#         df = pd.read_excel(user_excel_file)
#         user = df[df['email'] == email]
#         if not user.empty:
#             token = s.dumps(email, salt='password-reset-salt')
#             link = url_for('reset_password', token=token, _external=True)
#             msg = Message('Password Reset Request', sender='your_email@gmail.com', recipients=[email])
#             msg.body = f'Your link to reset your password is {link}'
#             mail.send(msg)
#             flash('A password reset link has been sent to your email.')
#             return redirect(url_for('login'))
#         else:
#             flash('Email not found')
#     return render_template('forgot_password.html')

# @app.route('/new_password/<token>', methods=['GET', 'POST'])
# def new_password(token):
#     try:
#         email = s.loads(token, salt='password-reset-salt', max_age=3600)
#     except (SignatureExpired, BadTimeSignature):
#         flash('The password reset link is invalid or has expired.')
#         return redirect(url_for('forgot_password'))

#     if request.method == 'POST':
#         new_password = request.form['new_password']
#         confirm_password = request.form['confirm_password']
#         if new_password == confirm_password:
#             df = pd.read_excel(user_excel_file)
#             user_index = df.index[df['email'] == email].tolist()[0]
#             df.at[user_index, 'password'] = new_password
#             df.to_excel(user_excel_file, index=False)
#             flash('Your password has been reset successfully.')
#             return redirect(url_for('login'))
#         else:
#             flash('Passwords do not match')
#     return render_template('reset_password.html', token=token)

# @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     try:
#         email = s.loads(token, salt='password-reset-salt', max_age=3600)
#     except (SignatureExpired, BadTimeSignature):
#         flash('The password reset link is invalid or has expired.')
#         return redirect(url_for('forgot_password'))

#     if request.method == 'POST':
#         new_password = request.form['new_password']
#         confirm_password = request.form['confirm_password']
#         if new_password == confirm_password:
#             df = pd.read_excel(user_excel_file)
#             user_index = df.index[df['email'] == email].tolist()[0]
#             df.at[user_index, 'password'] = new_password
#             df.to_excel(user_excel_file, index=False)
#             flash('Your password has been reset successfully.')
#             return redirect(url_for('login'))
#         else:
#             flash('Passwords do not match')
#     return render_template('reset_password.html', token=token)

# @app.route('/password_change', methods=['GET', 'POST'])
# def password_change():
#     message = None
#     if request.method == 'POST':
#         email = request.form['email']
#         old_password = request.form['old_password']
#         new_password = request.form['new_password']
#         confirm_password = request.form['confirm_password']
#         df = pd.read_excel(user_excel_file)
#         user = df[(df['email'] == email) & (df['password'] == old_password)]
#         if not user.empty:
#             if new_password == confirm_password:
#                 user_index = df.index[df['email'] == email].tolist()[0]
#                 df.at[user_index, 'password'] = new_password
#                 df.to_excel(user_excel_file, index=False)
#                 flash('Password successfully changed')
#                 return redirect(url_for('login'))
#             else:
#                 message = 'New passwords do not match'
#         else:
#             message = 'Invalid email or old password'
#     return render_template('password_change.html', message=message)

# @app.route('/student_info')
# def student_info():
#     if 'user' in session:
#         email = session['user']['email']
#         student_df = pd.read_excel(student_excel_file)
#         student = student_df[student_df['email'] == email]
#         if not student.empty:
#             student_info = student.iloc[0].to_dict()
#             return render_template('student_info.html', student=student_info)
#         else:
#             flash('No student information found for this email.')
#             return redirect(url_for('login'))
#     else:
#         return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash, session
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

s = URLSafeTimedSerializer(app.secret_key)
user_excel_file = 'users.xlsx'
student_excel_file = 'students.xlsx'

if not os.path.exists(user_excel_file):
    df = pd.DataFrame(columns=['username', 'full_name', 'email', 'password', 'DOB', 'address'])
    df.to_excel(user_excel_file, index=False)

if not os.path.exists(student_excel_file):
    student_df = pd.DataFrame(columns=['roll', 'name', 'email', 'dob', 'address', 'maths_marks', 'english_marks', 'science_marks'])
    student_df.to_excel(student_excel_file, index=False)

@app.route('/')
def home():
    user = session.get('user')
    return render_template('home.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        df = pd.read_excel(user_excel_file)
        user = df[(df['email'] == email) & (df['password'] == password)]
        if not user.empty:
            session['user'] = user.iloc[0].to_dict()
            flash('You were successfully logged in')
            return redirect(url_for('student_info'))
        else:
            message = 'Invalid credentials'
    return render_template('login.html', message=message)

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You were successfully logged out')
    return redirect(url_for('home'))
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        dob = request.form['dob']
        address = request.form['address']

        if password == confirm_password:
            df = pd.read_excel(user_excel_file)
            if email in df['email'].values:
                flash('Email already registered')
            else:
                new_user = pd.DataFrame([[username, full_name, email, password, dob, address]], 
                                        columns=['username', 'full_name', 'email', 'password', 'DOB', 'address'])
                df = pd.concat([df, new_user], ignore_index=True)
                df.to_excel(user_excel_file, index=False)
                flash('You have successfully registered')
                return redirect(url_for('login'))
        else:
            flash('Passwords do not match')
    return render_template('register.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         confirm_password = request.form['confirm_password']
#         if password == confirm_password:
#             df = pd.read_excel(user_excel_file)
#             if email in df['email'].values:
#                 flash('Email already registered')
#             else:
#                 new_user = pd.DataFrame([[username, email, password]], columns=['username', 'email', 'password'])
#                 df = pd.concat([df, new_user], ignore_index=True)
#                 df.to_excel(user_excel_file, index=False)
#                 flash('You have successfully registered')
#                 return redirect(url_for('login'))
#         else:
#             flash('Passwords do not match')
#     return render_template('register.html')

@app.route('/users')
def user_list():
    df = pd.read_excel(user_excel_file)
    users = df.to_dict(orient='records')
    return render_template('user_list.html', users=users)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        df = pd.read_excel(user_excel_file)
        user = df[df['email'] == email]
        if not user.empty:
            token = s.dumps(email, salt='password-reset-salt')
            return redirect(url_for('new_password', token=token))
        else:
            flash('Email not found')
    return render_template('forgot_password.html')

@app.route('/new_password/<token>', methods=['GET', 'POST'])
def new_password(token):
    try:
        email = s.loads(token, salt='password-reset-salt', max_age=3600)
    except (SignatureExpired, BadTimeSignature):
        flash('The password reset link is invalid or has expired.')
        return redirect(url_for('forgot_password'))

    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        if new_password == confirm_password:
            df = pd.read_excel(user_excel_file)
            user_index = df.index[df['email'] == email].tolist()[0]
            df.at[user_index, 'password'] = new_password
            df.to_excel(user_excel_file, index=False)
            flash('Your password has been reset successfully.')
            return redirect(url_for('login'))
        else:
            flash('Passwords do not match')
    return render_template('new_password.html', token=token)

@app.route('/password_change', methods=['GET', 'POST'])
def password_change():
    message = None
    if request.method == 'POST':
        email = request.form['email']
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        df = pd.read_excel(user_excel_file)
        user = df[(df['email'] == email) & (df['password'] == old_password)]
        if not user.empty:
            if new_password == confirm_password:
                user_index = df.index[df['email'] == email].tolist()[0]
                df.at[user_index, 'password'] = new_password
                df.to_excel(user_excel_file, index=False)
                flash('Password successfully changed')
                return redirect(url_for('login'))
            else:
                message = 'New passwords do not match'
        else:
            message = 'Invalid email or old password'
    return render_template('password_change.html', message=message)

@app.route('/student_info')
def student_info():
    if 'user' in session:
        email = session['user']['email']
        student_df = pd.read_excel(student_excel_file)
        student = student_df[student_df['email'] == email]
        if not student.empty:
            student_info = student.iloc[0].to_dict()
            return render_template('student_info.html', student=student_info)
        else:
            flash('No student information found for this email.')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

