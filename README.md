# Air Quality Flask

A small Flask web application that serves air-quality analysis over a global pollution dataset —
the analysis from [project-air-quality-analysis](https://github.com/apkirana/project-air-quality-analysis)
wrapped in a web front end so the plots can be read without opening a notebook.

## Screenshot

![The application showing air-quality metrics and a generated plot](https://raw.githubusercontent.com/apkirana/project-air_quality_flask/main/view%20app.png)

## Features

- Serves air-quality metrics from `data/global_air_pollution_data.csv`
- Generates a Matplotlib plot rendered into the page (`static/plot.png`)
- Single-file Flask app, easy to read end to end

## Repository structure

```text
flask_air_quality.py   - the Flask application
air_quality.ipynb      - exploratory notebook the app is based on
data/                  - global pollution dataset and a filtered subset
templates/index.html   - page template
static/plot.png        - generated figure
```

## Running it

```bash
git clone https://github.com/apkirana/project-air_quality_flask.git
cd project-air_quality_flask

python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

python flask_air_quality.py
```

Then open <http://127.0.0.1:5000>.

## Related work

- [project-air-quality-analysis](https://github.com/apkirana/project-air-quality-analysis) — the underlying PM2.5 / AQI analysis
- [project_polusikalimantan](https://github.com/apkirana/project_polusikalimantan) — spatio-temporal PM2.5 study across Kalimantan
- [project_eucairpollution](https://github.com/apkirana/project_eucairpollution) — agentic multi-agent AQI forecasting system

## Contributing

Issues and pull requests are welcome.

## Licence

MIT — see [LICENSE](LICENSE).

---

## Author

**Annisa Puspa Kirana** — PhD researcher, Faculty of Geo-Information Science and Earth Observation (ITC),
University of Twente. Research on agentic AI and LLM-driven workflows for Earth observation.

[Google Scholar](https://scholar.google.com/citations?user=BQl6KOsAAAAJ&hl=en) ·
[ORCID](https://orcid.org/0000-0002-4622-1445) ·
[LinkedIn](https://www.linkedin.com/in/annisapuspakirana) ·
[GitHub](https://github.com/apkirana)
