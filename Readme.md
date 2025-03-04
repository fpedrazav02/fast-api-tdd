<h1 align="center">
	🚀 fast-api-tdd
</h1>

<p align="center">
	<b><i>FastAPI set up for Test-Driven Development</i></b>
</p>

<h3 align="center">
	<a href="#%EF%B8%8F-installation">Installation</a>
	<span> · </span>
	<a href="#-running-app">Running the server</a>
	<span> · </span>
	<a href="#-setup">Setup</a>
</h3>

<li>
  <strong>Links</strong>:
  <a href="#-dependencies">Dependencies</a>
  <a href="#-docker">Docker</a>
</li>

---

## 🛠️ Installation

> _Instructions on how to install all required dependencies._

1. **Clone the repository**:
   ```sh
   git clone https://github.com/fpedrazav02/fast-api-tdd.git
   ```

2. **Move into the project directory:**
    ```sh
    cd fast-api-tdd
    ```

3. **Create a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate    # On Linux/Mac
    .\venv\Scripts\activate     # On Windows
    ```

4. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## 🚀 Running App

```sh
uvicorn main:app --reload --port 3000
```

<h2 id="-dependencies"> 🔗 Dependencies</h2>
<h3> adminer</h3>
<h3> sqlalchemy</h3>
<h3> alembic</h3>

<h2 id="-docker"> 🐳 Docker</h2>
<h3> Start services</h3>

```sh
docker-compose up --build --force-recreate -d
```


## 📝 Setup
> Explanation and details about how the setup works.
