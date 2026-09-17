from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
OUTPUT_DIR = BASE_DIR / "output"

SCHOOL_NAME = "AL MUSLEH FOUNDATION SCHOOL"
EXAM_NAME = "Mid-Term Examination 2026-27"
ISSUE_DATE = "19-09-2026"

# Change these if your actual school details are different.
SCHOOL_SUBTITLE = ""
SCHOOL_ADDRESS = "Muslehuddin Campus"

# 2 admit cards per A4 page.
CARDS_PER_PAGE = 2

# Placeholder photo size in points.
PHOTO_WIDTH = 70
PHOTO_HEIGHT = 82

LOGO_PATH = ASSETS_DIR / "amfs_logo.png"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
