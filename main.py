from website import create_app
#run app from here
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)