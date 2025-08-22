from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

# In-memory storage of reviews (use DB in real app)
reviews = []

@app.route('/')
def home():
    models = [
        {"name": "Silver", "image": "model-silver.jpg"},
        {"name": "Gold", "image": "model-gold.jpg"},
        {"name": "Diamond", "image": "model-diamond.jpg"}
    ]
    return render_template('index.html', models=models)

@app.route('/inquiry', methods=['GET', 'POST'])
def inquiry():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')
        if not (name and phone and address):
            flash('Please fill all fields', 'error')
            return redirect(url_for('inquiry'))
        # Process data: here you could save or send a notification
        flash('Thank you for your inquiry! Our team will contact you soon.', 'success')
        return redirect(url_for('home'))
    return render_template('inquiry.html')

@app.route('/reviews', methods=['GET', 'POST'])
def reviews_page():
    if request.method == 'POST':
        stars = int(request.form.get('stars', 0))
        comment = request.form.get('comment', '').strip()
        if stars < 1 or stars > 5:
            flash('Please select a star rating between 1 and 5', 'error')
        else:
            reviews.append({'stars': stars, 'comment': comment})
            flash('Thank you for your review!', 'success')
        return redirect(url_for('reviews_page'))
    return render_template('reviews.html', reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True)
