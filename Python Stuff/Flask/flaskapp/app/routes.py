from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

    
@app.route('/about')
def about():
  return render_template('about.html')
if __name__ == '__main__':
  app.run(debug=True)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Welcome User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
