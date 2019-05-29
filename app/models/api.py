from app.models.application import Labs, db

def add():
    lab1 = Labs(lab_type="A", capacity=8,course="COMP9101")

    db.session.add(lab1)
    db.session.commit()

def search_by_course(course):
    return Labs.query.filter_by(course=course).all()