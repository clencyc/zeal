# Backend Development
zeal tickets backend


## Getting started## Prerequisites

Make sure you have the following installed:
- Python (preferably 3.6+)
- pip (Python package installer)
### Setting up the project

1. **Clone the reposiroty(Or folk the repository):**

```bash
    git clone https://github.com/Zeal-tickets/Zealtickets-Backend.git
```

2. Navigate to the project directory:
```bash
cd backend
```

3. Create a virtual environment (optional but recommended):
```bash
python -m venv myenv
```

4. Activate the virtual environment:
- On windows
    ```bash
    myenv\Scripts\activate
    ```
- On Linux/macos
```bash
source myenv/bin/activate
```

5. Install the project dependencies:
```bash
pip install -r requirements.txt
```

6. Set up the database:
```bash
python manage.py migrate
```

### Running the project

To run the project locally for development or testing;

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the project in your web browser:

Open your web browser and go to <http://localhost:8000/>

3. To stop the server, press `CTRL + C` in the terminal


## Have fun coding! :smile:
