from app import create_app, db
from sqlalchemy import text
from app.models import Article

app = create_app()
with app.app_context():
    # Add missing columns to articles table
    db.session.execute(text('ALTER TABLE articles ADD COLUMN file_type VARCHAR(10)'))
    db.session.execute(text('ALTER TABLE articles ADD COLUMN file_path VARCHAR(256)'))
    db.session.commit()
    print('Database migration completed successfully!')