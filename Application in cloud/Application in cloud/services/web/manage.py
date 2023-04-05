#Project created by:
#           Serhii Burenkov
#           Dmytro Tvedovskyi
#           Rostyslav Pyrozhenko
# for class: Interned applications created in cloud 



from flask.cli import FlaskGroup

from project import app, db


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
