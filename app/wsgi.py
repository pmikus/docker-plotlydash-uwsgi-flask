from pal import app


if __name__ == "__main__":
    # Main entry point.
    app.debug = True
    app.run(host="0.0.0.0")
