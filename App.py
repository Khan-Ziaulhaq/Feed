from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Cloud Feed!"

@app.route('/feed')
def feed():
    return """
    <rss version="2.0">
      <channel>
        <title>My Simple Cloud Feed</title>
        <link>http://example.com</link>
        <description>This is a sample RSS feed from the cloud.</description>

        <item>
          <title>Post 1</title>
          <link>http://example.com/post1</link>
          <description>This is the first post in the feed.</description>
        </item>

        <item>
          <title>Post 2</title>
          <link>http://example.com/post2</link>
          <description>This is the second post in the feed.</description>
        </item>

      </channel>
    </rss>

"""


if __name__ == '__main__':
    app.run()
