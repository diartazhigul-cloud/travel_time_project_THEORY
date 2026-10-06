# Travel Time vs University Attendance

Python Streamlit website for a mathematical statistics project.

Research question: is there a statistical relationship between travel time to university (minutes) and class attendance (%)?

## How to open in PyCharm

1. Unzip `travel_time_attendance_project.zip`.
2. In PyCharm: **File → Open** and select the unzipped folder `travel_time_attendance_project`.
3. Create a virtual environment if PyCharm asks.
4. Open the Terminal in PyCharm and install packages:

```bash
pip install -r requirements.txt
```

5. Run the website:

```bash
streamlit run app.py
```

6. Open the address shown by Streamlit, usually:

http://localhost:8501

## Как открыть в PyCharm

1. Распакуйте `travel_time_attendance_project.zip`.
2. В PyCharm: **File → Open** и выберите папку `travel_time_attendance_project`.
3. Если PyCharm предложит, создайте виртуальное окружение.
4. В терминале PyCharm:

```bash
pip install -r requirements.txt
```

5. Запуск:

```bash
streamlit run app.py
```

6. Откройте адрес, который покажет Streamlit, обычно http://localhost:8501

## What is inside

- `app.py` — the website (navigation, pages)
- `style.py` — retro-game CSS and Plotly theme
- `ui.py` — shared UI helpers
- `analysis.py` — statistics helpers (summary, Fisher CI, correlation + regression)
- `formulas.py` — formula book texts (EN/RU)
- `formula_pages.py` — formula pages and mini calculators
- `sandbox.py` — page where players add their own data
- `storage.py` — saves player data to `player_data.csv`
- `.streamlit/config.toml` — dark theme settings
- `data.py` — 34 survey responses
- `cleaning.py` — parsing hours, ranges, percents
- `i18n.py` — English / Russian text
- `requirements.txt` — Python packages

The dashboard includes: about, research question, hypotheses, survey table, data cleaning, descriptive statistics, histograms, scatter plot, box plots, Pearson correlation, linear regression, hypothesis test, year and transport breakdowns, travel-time categories, interpretation, limitations, and conclusion.

Language can be switched in the sidebar (EN / RU).

## Site structure (retro-game layout)

The 24 pages are grouped into 7 "worlds":

1. **Briefing** — Home, About, Research Question, Hypotheses
2. **Formulas** — School Toolkit, then the topics of weeks 1-5: Sets & Combinatorics, General Probability, Conditional Probability, Independence, Data Description. Every page has a *Formulas* tab and a *Try it* tab with calculators (some use the survey data).
3. **Data** — Survey Data, Data Cleaning
4. **Analysis** — Descriptive, Visualization, Correlation, Regression, Hypothesis Testing
5. **Bonus levels** — by Year, by Transport, Travel Time Categories
6. **Sandbox** — Add Your Data: players enter their travel time, transport and attendance; correlation, regression and the test are recalculated for "survey + players", "players only" or "my entries only".
7. **Finale** — Interpretation, Limitations, Conclusion

Every page has a progress bar and BACK / NEXT buttons.

### Player data

Entries from the Sandbox page are saved in `player_data.csv` next to `app.py` (created automatically, shared by everyone who opens the site). The main analysis pages always use the fixed survey, so the project results do not change. To reset the player data, stop the app and delete `player_data.csv`.

## Структура сайта

24 страницы собраны в 7 «миров»: Брифинг → Формулы → Данные → Анализ → Бонус-уровни → Песочница → Финал.

- **Формулы**: школьная база и темы недель 1–5 (множества и комбинаторика, общая вероятность, условная вероятность, независимость, описание данных). На каждой странице две вкладки: «Формулы» и «Попробуй» (калькуляторы, часть работает на данных опроса).
- **Песочница**: игрок вводит время в пути, транспорт и посещаемость, а сайт пересчитывает корреляцию, регрессию и проверку гипотезы.
- Данные игроков хранятся в файле `player_data.csv` рядом с `app.py`. Чтобы сбросить, остановите сайт и удалите этот файл. Основной анализ всегда использует фиксированный опрос.
