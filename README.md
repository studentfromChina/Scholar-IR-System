```markdown
# Scholar Information Retrieval System

This project is a Scholar Information Retrieval System that allows you to index and search scholarly papers. It consists of three main components: extracting metadata and text from PDFs using Grobid, building an inverted index using Lucene, and implementing a simple web search interface using Flask.

## Requirements

- Python 3.9
- Flask
- Flask-Login
- pyLucene (Python wrapper for Lucene)

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/scholar-information-retrieval.git
```

2. Install the required Python packages:

```bash
pip install Flask Flask-Login pyLucene
```

3. Download and install [Grobid](https://grobid.readthedocs.io/) for PDF processing.

## Usage

### Step 1: Extract Metadata and Text from PDFs using Grobid

1. Place your PDFs in the `pdf` folder.
2. Start Grobid service.
3. Run the Python script to extract metadata and text:

```bash
python Grobid.py
```

### Step 2: Build an Inverted Index using Lucene

1. Set up the index directory in `app.py`.
2. Run the Python script to build the index:

```bash
python Lucene.py
```

### Step 3: Implement a Simple Web Search Interface

1. Customize the Flask app in `web_search.py` according to your needs.
2. Create HTML templates in the `templates` folder for search, results, login, and dashboard pages.

### Running the Application

```bash
python web_search.py
```

Visit [http://localhost:5000](http://localhost:5000) in your web browser to use the application.

## Features

- Extracts metadata and text from PDFs using Grobid.
- Builds an inverted index using Lucene for efficient search.
- Provides a simple web interface for users to search scholarly papers.

## Error Handling

The application includes basic error handling for 404 pages and utilizes Flask's `flash` feature for displaying success and error messages.

## User Authentication

User authentication is implemented using Flask-Login. It includes a basic login page where users can enter their credentials.

## Contributors

- [studentfromChina](https://github.com/studentfromChina)

## License

This project is licensed under the [MIT License](LICENSE).
```
