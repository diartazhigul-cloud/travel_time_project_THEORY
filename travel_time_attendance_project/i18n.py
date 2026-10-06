PAGES = {
    "EN": [
        ("home", "Home"),
        ("about", "About the Project"),
        ("research", "Research Question"),
        ("hypotheses", "Objectives & Hypotheses"),
        ("survey", "Survey Data"),
        ("cleaning", "Data Cleaning"),
        ("descriptive", "Descriptive Statistics"),
        ("visualization", "Data Visualization"),
        ("correlation", "Correlation Analysis"),
        ("regression", "Linear Regression"),
        ("testing", "Hypothesis Testing"),
        ("year", "Analysis by Year of Study"),
        ("transport", "Analysis by Transport Type"),
        ("bins", "Travel Time Categories"),
        ("interpretation", "Interpretation"),
        ("limitations", "Limitations"),
        ("conclusion", "Conclusion"),
    ],
    "RU": [
        ("home", "Главная"),
        ("about", "О проекте"),
        ("research", "Исследовательский вопрос"),
        ("hypotheses", "Цели и гипотезы"),
        ("survey", "Данные опроса"),
        ("cleaning", "Очистка данных"),
        ("descriptive", "Описательная статистика"),
        ("visualization", "Визуализация"),
        ("correlation", "Корреляционный анализ"),
        ("regression", "Линейная регрессия"),
        ("testing", "Проверка гипотез"),
        ("year", "Анализ по курсу"),
        ("transport", "Анализ по транспорту"),
        ("bins", "Категории времени в пути"),
        ("interpretation", "Интерпретация"),
        ("limitations", "Ограничения"),
        ("conclusion", "Заключение"),
    ],
}

TRANSPORT_LABELS = {
    "EN": {
        "walk": "Walking",
        "bus": "Bus",
        "car": "Personal car / taxi",
        "walk_bus": "Walk + bus",
        "plane": "Plane",
        "other": "Other",
    },
    "RU": {
        "walk": "Пешком",
        "bus": "Автобус",
        "car": "Личное авто / такси",
        "walk_bus": "Пешком + автобус",
        "plane": "Самолёт",
        "other": "Другое",
    },
}

TEXTS = {
    "EN": {
        "app_title": "Travel Time & Attendance",
        "hero_title": "Travel Time and University Attendance",
        "hero_lead": (
            "This project investigates whether the amount of time students spend "
            "travelling to university is statistically related to their attendance rate."
        ),
        "lang": "Language",
        "settings": "Analysis settings",
        "show_raw": "Show raw data",
        "show_clean": "Show cleaned data",
        "nav": "Pages",
        "analysis_jump": "Select analysis",
        "jump_overview": "Overview",
        "jump_corr": "Correlation",
        "jump_reg": "Regression",
        "jump_transport": "Transport",
        "jump_year": "Year of study",
        "metric_n": "Students surveyed",
        "metric_time": "Average travel time",
        "metric_att": "Average attendance",
        "metric_r": "Pearson correlation",
        "about_title": "About the Project",
        "about_body": (
            "Many students spend a substantial amount of time travelling to campus. "
            "This project uses real survey data and the workflow from the course example: "
            "real-world problem → research question → data collection → descriptive statistics → "
            "visualization → correlation → regression → hypothesis testing → interpretation → conclusion."
        ),
        "methods_title": "Statistical methods",
        "methods_list": (
            "- Descriptive statistics (mean, median, min, max, standard deviation, quartiles, IQR, variance)\n"
            "- Histograms, scatter plot and box plots\n"
            "- Pearson correlation coefficient r\n"
            "- Simple linear regression\n"
            "- Two-sided hypothesis test for ρ = 0 at α = 0.05"
        ),
        "rq_title": "Research Question",
        "rq_text": (
            "Is there a statistical relationship between the time students spend travelling "
            "to university and the percentage of classes they attend?"
        ),
        "variables": "Variables",
        "x_title": "Independent variable (X)",
        "x_text": "Travel time to university, measured in minutes (one way).",
        "y_title": "Dependent variable (Y)",
        "y_text": "Percentage of classes attended during the last month.",
        "obj_title": "Objective",
        "obj_text": "To determine whether travel time is statistically associated with university attendance.",
        "hyp_title": "Hypotheses",
        "h0": "H₀: There is no linear relationship between travel time and attendance (ρ = 0).",
        "h1": "H₁: There is a linear relationship between travel time and attendance (ρ ≠ 0).",
        "alpha": "Significance level: α = 0.05",
        "survey_title": "Survey Data",
        "survey_note": "Anonymous Google Form responses. Personal identifiers were not collected.",
        "col_student": "Student",
        "col_year": "Year",
        "col_travel_raw": "Travel time (raw)",
        "col_travel": "Travel time (min)",
        "col_transport": "Transport",
        "col_att_raw": "Attendance (raw)",
        "col_att": "Attendance (%)",
        "col_action": "Action",
        "col_note": "Cleaning note",
        "clean_title": "Data Cleaning",
        "clean_intro": (
            "Some responses were entered as ranges or hours instead of a single number. "
            "For statistical analysis, ranges were converted to their midpoint and hours were converted to minutes."
        ),
        "clean_examples": "Examples",
        "ex1": "`1 сағат` / `1 час` / `Час` → 60 minutes",
        "ex2": "`1.5 сағат` → 90 minutes",
        "ex3": "`2сағат` → 120 minutes",
        "ex4": "`10–15 minutes` → 12.5 minutes",
        "ex5": "`20–30 minutes` → 25 minutes",
        "ex6": "`90–100%` → 95%",
        "ex7": "`99,90%` → 99.9%",
        "ex8": "`1 мин` + plane, or `1 жыл` → excluded",
        "desc_title": "Descriptive Statistics",
        "var_time": "Travel time (min)",
        "var_att": "Attendance (%)",
        "mean": "Mean",
        "median": "Median",
        "minimum": "Minimum",
        "maximum": "Maximum",
        "std": "Std. deviation",
        "var": "Variance",
        "q1": "Q1",
        "q3": "Q3",
        "iqr": "IQR",
        "viz_title": "Data Visualization",
        "hist_time": "Distribution of travel time",
        "hist_att": "Distribution of attendance",
        "scatter_title": "Travel time vs attendance",
        "box_title": "Box plots",
        "x_axis": "Travel time (minutes)",
        "y_axis": "Attendance (%)",
        "count": "Number of students",
        "corr_title": "Correlation Analysis",
        "pearson": "Pearson correlation",
        "pvalue": "p-value",
        "reject": "Reject H₀",
        "fail": "Fail to reject H₀",
        "because_lt": "p < α → statistically significant linear association in this sample.",
        "because_gt": "p > α → no statistically significant linear association in this sample.",
        "reg_title": "Linear Regression",
        "equation": "Regression equation",
        "slope": "Slope",
        "intercept": "Intercept",
        "r2": "R²",
        "test_title": "Hypothesis Testing",
        "test_h0": "H₀: ρ = 0",
        "test_h1": "H₁: ρ ≠ 0",
        "year_title": "Analysis by Year of Study",
        "year_note": (
            "This comparison is descriptive only because the number of students in each year "
            "is small and uneven. It is not the main hypothesis of the project."
        ),
        "year_mean": "Average attendance by year",
        "n_group": "n",
        "transport_title": "Analysis by Transport Type",
        "transport_note": (
            "This is additional descriptive analysis, not the main hypothesis. "
            "The plane response was excluded as unrealistic."
        ),
        "bins_title": "Travel Time Categories",
        "bins_note": "Students are grouped by travel time. Average attendance is shown for each group.",
        "interp_title": "Interpretation",
        "interp_r": (
            "The correlation coefficient indicates the direction and strength of the linear "
            "association between travel time and attendance."
        ),
        "causation": "Correlation does not imply causation.",
        "interp_extra": (
            "Even if a relationship is statistically significant, this would not prove that "
            "long travel time itself causes missed classes. Other factors may also affect attendance."
        ),
        "lim_title": "Limitations",
        "lim_list": (
            "- Small sample size\n"
            "- Self-reported attendance\n"
            "- Approximate travel times\n"
            "- Some responses required data cleaning\n"
            "- Survey participants may not represent all university students\n"
            "- Other factors may affect attendance: schedule, motivation, workload, health, transport reliability"
        ),
        "lim_cause": (
            "Therefore we cannot say: “Long travel time causes low attendance.” "
            "We can only say that we investigated whether there is a statistical association."
        ),
        "conc_title": "Conclusion",
        "sample_size": "Sample size",
        "result": "Result",
        "conc_yes": (
            "Based on the collected sample, there is sufficient statistical evidence of a linear "
            "relationship between travel time and attendance."
        ),
        "conc_no": (
            "Based on the collected sample, there is not sufficient statistical evidence of a linear "
            "relationship between travel time and attendance."
        ),
        "footer": "Mathematical statistics project: descriptive statistics, visualization, correlation, regression, hypothesis testing.",
        "strength_negligible": "negligible",
        "strength_weak": "weak",
        "strength_moderate": "moderate",
        "strength_strong": "strong",
        "strength_very_strong": "very strong",
        "dir_pos": "positive",
        "dir_neg": "negative",
        "dir_zero": "no",
        "corr_phrase": "{strength} {direction} correlation",
        "kept": "Valid observations used in the main analysis",
        "excluded": "Excluded responses",
        "raw_table": "Raw data",
        "clean_table": "Cleaned data",
        "examples_table": "Cleaning examples",
        "raw_in": "Raw answer",
        "cleaned_to": "Cleaned value",
        "rule": "Rule",
    },
    "RU": {
        "app_title": "Время в пути и посещаемость",
        "hero_title": "Время в пути и посещаемость университета",
        "hero_lead": (
            "Проект проверяет, связана ли статистически длительность дороги студентов "
            "до университета с процентом посещённых занятий."
        ),
        "lang": "Язык",
        "settings": "Настройки анализа",
        "show_raw": "Показать сырые данные",
        "show_clean": "Показать очищенные данные",
        "nav": "Страницы",
        "analysis_jump": "Выбрать анализ",
        "jump_overview": "Обзор",
        "jump_corr": "Корреляция",
        "jump_reg": "Регрессия",
        "jump_transport": "Транспорт",
        "jump_year": "Курс обучения",
        "metric_n": "Опрошено студентов",
        "metric_time": "Среднее время в пути",
        "metric_att": "Средняя посещаемость",
        "metric_r": "Корреляция Пирсона",
        "about_title": "О проекте",
        "about_body": (
            "Многие студенты тратят много времени на дорогу до кампуса. "
            "Проект использует реальные данные опроса и схему из учебного примера: "
            "практическая задача → вопрос исследования → сбор данных → описательная статистика → "
            "визуализация → корреляция → регрессия → проверка гипотез → интерпретация → вывод."
        ),
        "methods_title": "Статистические методы",
        "methods_list": (
            "- Описательная статистика (среднее, медиана, минимум, максимум, стандартное отклонение, квартили, IQR, дисперсия)\n"
            "- Гистограммы, диаграмма рассеяния и box plot\n"
            "- Коэффициент корреляции Пирсона r\n"
            "- Простая линейная регрессия\n"
            "- Двусторонняя проверка гипотезы ρ = 0 при α = 0.05"
        ),
        "rq_title": "Исследовательский вопрос",
        "rq_text": (
            "Есть ли статистическая связь между временем в пути до университета "
            "и процентом посещённых занятий за последний месяц?"
        ),
        "variables": "Переменные",
        "x_title": "Независимая переменная (X)",
        "x_text": "Время в пути до университета в минутах (в одну сторону).",
        "y_title": "Зависимая переменная (Y)",
        "y_text": "Процент посещённых занятий за последний месяц.",
        "obj_title": "Цель",
        "obj_text": "Определить, связана ли статистически длительность дороги с посещаемостью университета.",
        "hyp_title": "Гипотезы",
        "h0": "H₀: Линейной связи между временем в пути и посещаемостью нет (ρ = 0).",
        "h1": "H₁: Линейная связь между временем в пути и посещаемостью есть (ρ ≠ 0).",
        "alpha": "Уровень значимости: α = 0.05",
        "survey_title": "Данные опроса",
        "survey_note": "Анонимные ответы Google Form. Персональные данные не собирались.",
        "col_student": "Студент",
        "col_year": "Курс",
        "col_travel_raw": "Время в пути (сырое)",
        "col_travel": "Время в пути (мин)",
        "col_transport": "Транспорт",
        "col_att_raw": "Посещаемость (сырая)",
        "col_att": "Посещаемость (%)",
        "col_action": "Действие",
        "col_note": "Комментарий очистки",
        "clean_title": "Очистка данных",
        "clean_intro": (
            "Часть ответов была записана как диапазон или в часах, а не одним числом. "
            "Для анализа диапазоны заменены серединой, часы переведены в минуты."
        ),
        "clean_examples": "Примеры",
        "ex1": "`1 сағат` / `1 час` / `Час` → 60 минут",
        "ex2": "`1.5 сағат` → 90 минут",
        "ex3": "`2сағат` → 120 минут",
        "ex4": "`10–15 minutes` → 12.5 минут",
        "ex5": "`20–30 minutes` → 25 минут",
        "ex6": "`90–100%` → 95%",
        "ex7": "`99,90%` → 99.9%",
        "ex8": "`1 мин` + самолёт или `1 жыл` → исключено",
        "desc_title": "Описательная статистика",
        "var_time": "Время в пути (мин)",
        "var_att": "Посещаемость (%)",
        "mean": "Среднее",
        "median": "Медиана",
        "minimum": "Минимум",
        "maximum": "Максимум",
        "std": "Ст. отклонение",
        "var": "Дисперсия",
        "q1": "Q1",
        "q3": "Q3",
        "iqr": "IQR",
        "viz_title": "Визуализация данных",
        "hist_time": "Распределение времени в пути",
        "hist_att": "Распределение посещаемости",
        "scatter_title": "Время в пути и посещаемость",
        "box_title": "Box plot",
        "x_axis": "Время в пути (минуты)",
        "y_axis": "Посещаемость (%)",
        "count": "Число студентов",
        "corr_title": "Корреляционный анализ",
        "pearson": "Корреляция Пирсона",
        "pvalue": "p-значение",
        "reject": "Отклоняем H₀",
        "fail": "Не отклоняем H₀",
        "because_lt": "p < α → в этой выборке линейная связь статистически значима.",
        "because_gt": "p > α → в этой выборке статистически значимой линейной связи нет.",
        "reg_title": "Линейная регрессия",
        "equation": "Уравнение регрессии",
        "slope": "Наклон",
        "intercept": "Свободный член",
        "r2": "R²",
        "test_title": "Проверка гипотез",
        "test_h0": "H₀: ρ = 0",
        "test_h1": "H₁: ρ ≠ 0",
        "year_title": "Анализ по курсу обучения",
        "year_note": (
            "Это только описательное сравнение: в каждой группе мало студентов, "
            "и размеры групп неравны. Это не основная гипотеза проекта."
        ),
        "year_mean": "Средняя посещаемость по курсам",
        "n_group": "n",
        "transport_title": "Анализ по типу транспорта",
        "transport_note": (
            "Это дополнительный описательный анализ, а не основная гипотеза. "
            "Ответ «самолёт» исключён как нереалистичный."
        ),
        "bins_title": "Категории времени в пути",
        "bins_note": "Студенты сгруппированы по времени в пути. Для каждой группы показана средняя посещаемость.",
        "interp_title": "Интерпретация",
        "interp_r": (
            "Коэффициент корреляции показывает направление и силу линейной связи "
            "между временем в пути и посещаемостью."
        ),
        "causation": "Корреляция не означает причинность.",
        "interp_extra": (
            "Даже если связь окажется статистически значимой, это не доказывает, "
            "что длинная дорога сама вызывает пропуски. На посещаемость могут влиять и другие факторы."
        ),
        "lim_title": "Ограничения",
        "lim_list": (
            "- Небольшая выборка\n"
            "- Посещаемость указана самими студентами\n"
            "- Время в пути приблизительное\n"
            "- Часть ответов потребовала очистки\n"
            "- Участники опроса могут не представлять всех студентов университета\n"
            "- На посещаемость могут влиять расписание, мотивация, нагрузка, здоровье, надёжность транспорта"
        ),
        "lim_cause": (
            "Поэтому нельзя сказать: «Долгая дорога вызывает низкую посещаемость». "
            "Можно сказать только, что проверялась статистическая ассоциация."
        ),
        "conc_title": "Заключение",
        "sample_size": "Объём выборки",
        "result": "Результат",
        "conc_yes": (
            "По собранной выборке есть достаточные статистические основания говорить "
            "о линейной связи между временем в пути и посещаемостью."
        ),
        "conc_no": (
            "По собранной выборке нет достаточных статистических оснований говорить "
            "о линейной связи между временем в пути и посещаемостью."
        ),
        "footer": "Проект по математической статистике: описательная статистика, визуализация, корреляция, регрессия, проверка гипотез.",
        "strength_negligible": "пренебрежимо слабая",
        "strength_weak": "слабая",
        "strength_moderate": "умеренная",
        "strength_strong": "сильная",
        "strength_very_strong": "очень сильная",
        "dir_pos": "положительная",
        "dir_neg": "отрицательная",
        "dir_zero": "нулевая",
        "corr_phrase": "{strength} {direction} корреляция",
        "kept": "Валидные наблюдения в основном анализе",
        "excluded": "Исключённые ответы",
        "raw_table": "Сырые данные",
        "clean_table": "Очищенные данные",
        "examples_table": "Примеры очистки",
        "raw_in": "Исходный ответ",
        "cleaned_to": "После очистки",
        "rule": "Правило",
    },
}


def describe_r(r, lang):
    t = TEXTS[lang]
    a = abs(r)
    if a < 0.10:
        strength = t["strength_negligible"]
    elif a < 0.30:
        strength = t["strength_weak"]
    elif a < 0.50:
        strength = t["strength_moderate"]
    elif a < 0.70:
        strength = t["strength_strong"]
    else:
        strength = t["strength_very_strong"]
    if r > 0:
        direction = t["dir_pos"]
    elif r < 0:
        direction = t["dir_neg"]
    else:
        direction = t["dir_zero"]
    return t["corr_phrase"].format(strength=strength, direction=direction)


# ---------------------------------------------------------------------------
# Navigation groups ("worlds") and extra UI texts for the retro-game layout
# ---------------------------------------------------------------------------
PAGES["EN"] += [
    ("f_school", "School Toolkit"),
    ("f_sets", "Sets & Combinatorics"),
    ("f_prob", "General Probability"),
    ("f_cond", "Conditional Probability"),
    ("f_indep", "Independence"),
    ("f_data", "Data Description"),
    ("user_data", "Add Your Data"),
]
PAGES["RU"] += [
    ("f_school", "Школьная база"),
    ("f_sets", "Множества и комбинаторика"),
    ("f_prob", "Общая вероятность"),
    ("f_cond", "Условная вероятность"),
    ("f_indep", "Независимость"),
    ("f_data", "Описание данных"),
    ("user_data", "Свои данные"),
]

GROUPS = [
    {
        "id": "briefing",
        "icon": "🏰",
        "name": {"EN": "Briefing", "RU": "Брифинг"},
        "desc": {"EN": "What we study and why", "RU": "Что изучаем и зачем"},
        "pages": ["home", "about", "research", "hypotheses"],
    },
    {
        "id": "formulas",
        "icon": "📜",
        "name": {"EN": "Formulas", "RU": "Формулы"},
        "desc": {
            "EN": "School basics + weeks 1-5 with mini calculators",
            "RU": "Школьная база + недели 1-5 с мини-калькуляторами",
        },
        "pages": ["f_school", "f_sets", "f_prob", "f_cond", "f_indep", "f_data"],
    },
    {
        "id": "data",
        "icon": "💾",
        "name": {"EN": "Data", "RU": "Данные"},
        "desc": {"EN": "Survey answers and how we cleaned them", "RU": "Ответы опроса и их очистка"},
        "pages": ["survey", "cleaning"],
    },
    {
        "id": "analysis",
        "icon": "⚔️",
        "name": {"EN": "Analysis", "RU": "Анализ"},
        "desc": {
            "EN": "Statistics, charts, correlation, regression, test",
            "RU": "Статистика, графики, корреляция, регрессия, тест",
        },
        "pages": ["descriptive", "visualization", "correlation", "regression", "testing"],
    },
    {
        "id": "bonus",
        "icon": "⭐",
        "name": {"EN": "Bonus levels", "RU": "Бонус-уровни"},
        "desc": {
            "EN": "Extra look by year, transport and time groups",
            "RU": "Доп. срезы: курс, транспорт, группы времени",
        },
        "pages": ["year", "transport", "bins"],
    },
    {
        "id": "sandbox",
        "icon": "🎮",
        "name": {"EN": "Sandbox", "RU": "Песочница"},
        "desc": {
            "EN": "Add your own data and watch everything update",
            "RU": "Добавь свои данные и смотри пересчёт",
        },
        "pages": ["user_data"],
    },
    {
        "id": "finale",
        "icon": "🏆",
        "name": {"EN": "Finale", "RU": "Финал"},
        "desc": {"EN": "Meaning, limits and the final answer", "RU": "Смысл, ограничения и итоговый ответ"},
        "pages": ["interpretation", "limitations", "conclusion"],
    },
]

TEXTS["EN"].update(
    {
        "logo": "TRAVEL & ATTENDANCE",
        "world": "WORLD",
        "stage": "STAGE",
        "score": "SCORE",
        "btn_start": "PRESS START",
        "btn_next": "NEXT",
        "btn_prev": "BACK",
        "btn_restart": "PLAY AGAIN",
        "btn_enter": "ENTER",
        "next_up": "Next level",
        "home_map": "Game map",
        "key_result": "Key result",
        "key_sentence_sig": "In this sample, {phrase} was found (r = {r:.3f}, p = {p:.3f}). The link is statistically significant.",
        "key_sentence_ns": "In this sample, {phrase} was found (r = {r:.3f}, p = {p:.3f}). The link is NOT statistically significant.",
        "tab_all": "All responses",
        "tab_clean": "Cleaned data",
        "tab_hist": "Histograms",
        "tab_scatter": "Scatter plot",
        "tab_box": "Box plots",
        "t_stat": "t-statistic",
        "df": "Degrees of freedom",
        "ci95": "95% CI for r (Fisher z)",
        "rule_hours": "hours → minutes",
        "rule_range": "range midpoint",
        "rule_comma": "comma decimal",
        "rule_unreal": "unrealistic commute",
        "excluded_word": "excluded",
        "lang_short": "LANG",
        # sandbox
        "ud_title": "Add Your Data",
        "ud_intro": (
            "Become a player: add your own travel time and attendance. The site recalculates everything "
            "with your numbers: descriptive statistics, correlation, regression and the hypothesis test."
        ),
        "ud_privacy": (
            "Entries are saved in player_data.csv on the server and are visible to everyone who uses this site. "
            "No personal data is collected."
        ),
        "ud_step1": "1 · Add a player",
        "ud_step2": "2 · Choose the data",
        "ud_step3": "3 · Results",
        "ud_year": "Year of study",
        "ud_travel": "Travel time (one way)",
        "ud_unit": "Unit",
        "ud_unit_min": "minutes",
        "ud_unit_h": "hours",
        "ud_transport": "Transport",
        "ud_att": "Attendance over the last month (%)",
        "ud_submit": "ADD TO GAME",
        "ud_added": "★ +1 player added! Everything below is recalculated.",
        "ud_bad_travel": "Travel time must be between 1 and 300 minutes.",
        "ud_limit": "Limit reached: at most {n} entries per player.",
        "ud_full": "The storage is full. Ask the teacher to clear player_data.csv.",
        "ud_players_count": "Players added so far: {n}",
        "ud_scope": "Which data to analyse?",
        "ud_scope_survey_players": "Survey + all players",
        "ud_scope_players": "All players only",
        "ud_scope_mine": "Only my entries",
        "ud_src_survey": "Survey",
        "ud_src_players": "Players",
        "ud_src_me": "Me",
        "ud_col_source": "Source",
        "ud_mine": "My entries",
        "ud_none_mine": "You have not added anything yet.",
        "ud_delete_pick": "Pick entries to delete",
        "ud_delete": "Delete selected",
        "ud_clear": "Clear all my entries",
        "ud_empty": "There is no data in this selection yet. Add a player above.",
        "ud_need_more": "Need at least 3 points with different values to calculate correlation and regression.",
        "ud_small": "Small sample: treat the result as a game, not as a scientific conclusion.",
        "ud_compare": "Survey only vs selected data",
        "ud_col_metric": "Indicator",
        "ud_col_survey": "Survey only",
        "ud_col_sel": "Selected data",
        "ud_download": "Download CSV",
    }
)

TEXTS["RU"].update(
    {
        "logo": "ДОРОГА И ПОСЕЩАЕМОСТЬ",
        "world": "МИР",
        "stage": "УРОВЕНЬ",
        "score": "СЧЁТ",
        "btn_start": "НАЖМИ START",
        "btn_next": "ДАЛЕЕ",
        "btn_prev": "НАЗАД",
        "btn_restart": "ИГРАТЬ СНОВА",
        "btn_enter": "ВОЙТИ",
        "next_up": "Следующий уровень",
        "home_map": "Карта игры",
        "key_result": "Главный результат",
        "key_sentence_sig": "В этой выборке найдена {phrase} (r = {r:.3f}, p = {p:.3f}). Связь статистически значима.",
        "key_sentence_ns": "В этой выборке найдена {phrase} (r = {r:.3f}, p = {p:.3f}). Связь статистически НЕ значима.",
        "tab_all": "Все ответы",
        "tab_clean": "Очищенные данные",
        "tab_hist": "Гистограммы",
        "tab_scatter": "Диаграмма рассеяния",
        "tab_box": "Box plot",
        "t_stat": "t-статистика",
        "df": "Степени свободы",
        "ci95": "95% ДИ для r (z-преобразование Фишера)",
        "rule_hours": "часы → минуты",
        "rule_range": "середина диапазона",
        "rule_comma": "запятая как десятичный разделитель",
        "rule_unreal": "нереалистичная дорога",
        "excluded_word": "исключено",
        "lang_short": "ЯЗЫК",
        # sandbox
        "ud_title": "Добавь свои данные",
        "ud_intro": (
            "Станьте игроком: добавьте своё время в пути и посещаемость. Сайт пересчитает всё с вашими числами: "
            "описательную статистику, корреляцию, регрессию и проверку гипотезы."
        ),
        "ud_privacy": (
            "Записи сохраняются в файле player_data.csv на сервере и видны всем, кто пользуется сайтом. "
            "Персональные данные не собираются."
        ),
        "ud_step1": "1 · Добавить игрока",
        "ud_step2": "2 · Выбрать данные",
        "ud_step3": "3 · Результаты",
        "ud_year": "Курс",
        "ud_travel": "Время в пути (в одну сторону)",
        "ud_unit": "Единица",
        "ud_unit_min": "минуты",
        "ud_unit_h": "часы",
        "ud_transport": "Транспорт",
        "ud_att": "Посещаемость за последний месяц (%)",
        "ud_submit": "ДОБАВИТЬ В ИГРУ",
        "ud_added": "★ +1 игрок добавлен! Всё ниже пересчитано.",
        "ud_bad_travel": "Время в пути должно быть от 1 до 300 минут.",
        "ud_limit": "Лимит: не более {n} записей на игрока.",
        "ud_full": "Хранилище заполнено. Попросите преподавателя очистить player_data.csv.",
        "ud_players_count": "Игроков добавлено: {n}",
        "ud_scope": "Какие данные анализировать?",
        "ud_scope_survey_players": "Опрос + все игроки",
        "ud_scope_players": "Только все игроки",
        "ud_scope_mine": "Только мои записи",
        "ud_src_survey": "Опрос",
        "ud_src_players": "Игроки",
        "ud_src_me": "Я",
        "ud_col_source": "Источник",
        "ud_mine": "Мои записи",
        "ud_none_mine": "Вы пока ничего не добавили.",
        "ud_delete_pick": "Выберите записи для удаления",
        "ud_delete": "Удалить выбранные",
        "ud_clear": "Удалить все мои записи",
        "ud_empty": "В этой выборке пока нет данных. Добавьте игрока выше.",
        "ud_need_more": "Нужно минимум 3 точки с разными значениями, чтобы посчитать корреляцию и регрессию.",
        "ud_small": "Выборка маленькая: относитесь к результату как к игре, а не как к научному выводу.",
        "ud_compare": "Только опрос и выбранные данные",
        "ud_col_metric": "Показатель",
        "ud_col_survey": "Только опрос",
        "ud_col_sel": "Выбранные данные",
        "ud_download": "Скачать CSV",
    }
)
