from . import app, api, db, ma

api.add_resource()

db.init_app(app)
ma.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)       