from testservice.app import create_app
from testservice import config

app = create_app(config=config.Configuration)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
