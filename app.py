from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    emails = []
    with open('email.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if "@" in word:
                    if word not in emails:
                        emails.append(word)

    f = open('filtered-emails.txt', "w+")
    for mail in emails:
        f.write(mail+'\r')
    return render_template('index.html', emails=emails)

if __name__ == '__main__':
    app.run(Debug=True)