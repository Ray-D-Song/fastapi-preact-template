#!/usr/bin/env python
"""
Script to initialize SQLite database with some basic data.
"""
import os
import sys
import sqlite3
from pathlib import Path

# Add the parent directory to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from app.core.config import settings
from app.core.security import get_password_hash


def init_db() -> None:
    """Initialize the database with some basic data using direct SQLite connection."""
    # Get the absolute path to the SQLite database file
    base_dir = Path(__file__).parent.parent
    db_path = base_dir / "sqlite.db"
    
    # Connect to the SQLite database
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Check if the superuser already exists
    cursor.execute("SELECT * FROM user WHERE email = ?", (settings.FIRST_SUPERUSER,))
    user = cursor.fetchone()
    
    if not user:
        # Create a superuser if it doesn't exist
        hashed_password = get_password_hash(settings.FIRST_SUPERUSER_PASSWORD)
        cursor.execute(
            "INSERT INTO user (email, is_active, is_superuser, full_name, hashed_password) "
            "VALUES (?, ?, ?, ?, ?)",
            (settings.FIRST_SUPERUSER, True, True, "Admin", hashed_password)
        )
        conn.commit()
        print(f"Created superuser: {settings.FIRST_SUPERUSER}")
    else:
        print(f"Superuser already exists: {settings.FIRST_SUPERUSER}")
    
    # Close the connection
    conn.close()


if __name__ == "__main__":
    print("Initializing SQLite database...")
    init_db()
    print("Database initialization completed.")
