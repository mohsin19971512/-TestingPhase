## Installation

## Clone the repository:

```
 git clone https://github.com/mohsin19971512/-TestingPhase.git
```

## Navigate to the project directory:

```
 cd TestingPhase
```

## Create a virtual environment (optional but recommended):

```
 python -m venv venv

```

## Activate the virtual environment:
- On Windows:
```
 venv\Scripts\activate

```
- On macOS/Linux:
```
source venv/bin/activate
```

## Install the required packages:

```
pip install -r requirements.txt

```

## Usage
### Start the FastAPI server:
```
uvicorn core.main:app --reload

```
## Open swagger  
### After the server running open swagger by access this link
```
http://127.0.0.1:8000/docs

```