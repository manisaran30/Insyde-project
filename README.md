# Layout Optimizer

This project is a basic AI model that generates a structured 2D layout based on predefined constraints. It uses FastAPI for the backend and Streamlit for visualization.

## Features
- AI-based layout optimization
- FastAPI server for API-based access
- Streamlit-based UI for visualization
- Uses Matplotlib for graphical representation

---

## Installation and Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/manisaran30/Insyde-project.git
cd Insyde-project
```

### **2. Set Up a Virtual Environment (Recommended)**
```bash
python -m venv venv
```
#### **Activate the Virtual Environment:**
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## Running the Project

### **Option 1: Run FastAPI Server**
```bash
uvicorn layout_optimizer:app --host 0.0.0.0 --port 5000 --reload
```
- API available at: [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)

### **Option 2: Run Streamlit UI for Visualization**
```bash
streamlit run layout_optimizer.py
```
- UI available at: [http://localhost:8501](http://localhost:8501)

---

## API Usage (FastAPI)

### **1. Check API Status**
```bash
curl -X 'GET' 'http://127.0.0.1:5000/' -H 'accept: application/json'
```

### **2. Generate Layout (Example Request)**
```bash
curl -X 'POST' 'http://127.0.0.1:5000/generate' \
  -H 'Content-Type: application/json' \
  -d '{ "room_width": 10, "room_height": 8, "furniture": [{"name": "table", "width": 2, "height": 2}] }'
```

---

## Troubleshooting

### **1. Matplotlib ImportError**
If you see:
```bash
ImportError: DLL load failed while importing _path
```
Run:
```bash
pip uninstall -y matplotlib
pip cache purge
pip install --no-cache-dir matplotlib
```

### **2. Port Already in Use**
If you get an error like:
```bash
[Errno 10048] error while attempting to bind on address ('0.0.0.0', 5000)
```
Kill any existing processes using that port:
```bash
taskkill /F /IM python.exe
```
Then restart the server.

### **3. Python Version Issues**
Ensure you're using Python 3.9 or later:
```bash
python --version
```
If not, upgrade Python from [python.org](https://www.python.org/downloads/).

---

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Open a pull request.

---

## License
This project is licensed under the MIT License.

---

## Contact
For any issues, contact [manisaran30](https://github.com/manisaran30).
