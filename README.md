## A great beginning!!!

## Setup

**Requirements:** Python 3.10+, Node.js ^20.19.0 or >=22.12.0

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1      # Windows
source .venv/bin/activate        # macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver       # http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev                      # http://localhost:5173
```
