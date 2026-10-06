"""Formula book: topics of weeks 1-5 of the course + school basics. Text in EN and RU."""


def L(en, ru):
    return {"EN": en, "RU": ru}


PAGE_INFO = {
    "f_school": {
        "week": None,
        "topic": L(
            "School basics used everywhere in statistics: percent, averages, proportion, speed, straight line.",
            "Школьная база, которая нужна везде в статистике: проценты, средние, пропорции, скорость, прямая.",
        ),
    },
    "f_sets": {
        "week": 1,
        "topic": L(
            "Elements of set theory. Algebra of events. Discrete probability space. Elements of combinatorics.",
            "Элементы теории множеств. Алгебра событий. Дискретное вероятностное пространство. Элементы комбинаторики.",
        ),
    },
    "f_prob": {
        "week": 2,
        "topic": L("General probability space.", "Общее вероятностное пространство."),
    },
    "f_cond": {
        "week": 3,
        "topic": L(
            "Conditional probabilities. Total probability formula.",
            "Условные вероятности. Формула полной вероятности.",
        ),
    },
    "f_indep": {
        "week": 4,
        "topic": L("Independent events.", "Независимые события."),
    },
    "f_data": {
        "week": 5,
        "topic": L(
            "Frequency distributions and graphs. Data description. Data collection and preparation.",
            "Частотные распределения и графики. Описание данных. Сбор и подготовка данных.",
        ),
    },
}

# BLOCKS[page] = [ (block title, [ (label, latex, note), ... ]), ... ]
BLOCKS = {
    # ------------------------------------------------------------------ school
    "f_school": [
        (
            L("Percent", "Проценты"),
            [
                (
                    L("Share in percent", "Доля в процентах"),
                    r"p=\frac{a}{b}\cdot 100\%",
                    L(
                        "a is a part, b is the whole. Attendance (%) = attended classes ÷ all classes × 100.",
                        "a — часть, b — целое. Посещаемость (%) = посещённые занятия ÷ все занятия × 100.",
                    ),
                ),
                (
                    L("Part from a percent", "Часть по проценту"),
                    r"a=b\cdot\frac{p}{100}",
                    L(
                        "How many classes are 90% of 40? a = 40 · 0.9 = 36.",
                        "Сколько занятий составляют 90% от 40? a = 40 · 0.9 = 36.",
                    ),
                ),
                (
                    L("Change in percent", "Изменение в процентах"),
                    r"\Delta\%=\frac{x_1-x_0}{x_0}\cdot 100\%",
                    L("x₀ is the old value, x₁ is the new value.", "x₀ — старое значение, x₁ — новое."),
                ),
            ],
        ),
        (
            L("Averages", "Средние значения"),
            [
                (
                    L("Arithmetic mean", "Среднее арифметическое"),
                    r"\bar{x}=\frac{x_1+x_2+\dots+x_n}{n}=\frac{1}{n}\sum_{i=1}^{n}x_i",
                    L(
                        "Add all numbers and divide by how many there are.",
                        "Сложить все числа и разделить на их количество.",
                    ),
                ),
                (
                    L("Weighted mean", "Среднее взвешенное"),
                    r"\bar{x}_w=\frac{\sum_{i=1}^{n}w_i x_i}{\sum_{i=1}^{n}w_i}",
                    L(
                        "Used when values have different weights, like grades with different credits.",
                        "Когда у значений разный вес, например оценки с разным числом кредитов.",
                    ),
                ),
                (
                    L("Midpoint of a range", "Середина диапазона"),
                    r"m=\frac{a+b}{2}",
                    L(
                        "Used in data cleaning: 10–15 min → 12.5 min.",
                        "Используется при очистке данных: 10–15 мин → 12.5 мин.",
                    ),
                ),
            ],
        ),
        (
            L("Proportion, speed, units", "Пропорция, скорость, единицы"),
            [
                (
                    L("Proportion", "Пропорция"),
                    r"\frac{a}{b}=\frac{c}{d}\ \Rightarrow\ a\,d=b\,c",
                    L("Cross-multiply to find the unknown.", "Крест-накрест находим неизвестное."),
                ),
                (
                    L("Speed, distance, time", "Скорость, расстояние, время"),
                    r"v=\frac{s}{t},\qquad t=\frac{s}{v},\qquad s=v\,t",
                    L(
                        "Travel time = distance ÷ speed. This is where the X variable of the project comes from.",
                        "Время в пути = расстояние ÷ скорость. Так получается переменная X нашего проекта.",
                    ),
                ),
                (
                    L("Hours to minutes", "Часы в минуты"),
                    r"t_{\min}=60\cdot t_{h}",
                    L("1.5 hours = 90 minutes.", "1.5 часа = 90 минут."),
                ),
            ],
        ),
        (
            L("Sum and straight line", "Сумма и прямая"),
            [
                (
                    L("Sigma notation", "Знак суммы"),
                    r"\sum_{i=1}^{n}x_i=x_1+x_2+\dots+x_n",
                    L("Σ simply means “add up”.", "Σ просто означает «сложить»."),
                ),
                (
                    L("Straight line", "Прямая"),
                    r"y=kx+b,\qquad k=\frac{y_2-y_1}{x_2-x_1}",
                    L(
                        "k is the slope, b is where the line crosses the y-axis.",
                        "k — наклон, b — точка пересечения с осью y.",
                    ),
                ),
            ],
        ),
    ],
    # ------------------------------------------------------------------ week 1
    "f_sets": [
        (
            L("Sets and events", "Множества и события"),
            [
                (
                    L("Operations", "Операции"),
                    r"A\cup B,\qquad A\cap B,\qquad A\setminus B,\qquad \overline{A}=\Omega\setminus A",
                    L(
                        "Union: at least one happens. Intersection: both happen. Difference: A but not B. "
                        "Complement: A does not happen.",
                        "Объединение: произошло хотя бы одно. Пересечение: произошли оба. Разность: A, но не B. "
                        "Дополнение: A не произошло.",
                    ),
                ),
                (
                    L("Sure, impossible, incompatible", "Достоверное, невозможное, несовместные"),
                    r"A\cup\overline{A}=\Omega,\qquad A\cap\overline{A}=\varnothing,\qquad A\cap B=\varnothing",
                    L(
                        "Ω is the sure event, ∅ the impossible one. If A ∩ B = ∅, the events are incompatible.",
                        "Ω — достоверное событие, ∅ — невозможное. Если A ∩ B = ∅, события несовместны.",
                    ),
                ),
                (
                    L("De Morgan laws", "Законы де Моргана"),
                    r"\overline{A\cup B}=\overline{A}\cap\overline{B},\qquad \overline{A\cap B}=\overline{A}\cup\overline{B}",
                    None,
                ),
                (
                    L("Distributive law", "Дистрибутивность"),
                    r"A\cap(B\cup C)=(A\cap B)\cup(A\cap C)",
                    None,
                ),
                (
                    L("Number of elements", "Число элементов"),
                    r"|A\cup B|=|A|+|B|-|A\cap B|",
                    L(
                        "Elements in both sets must not be counted twice.",
                        "Элементы, которые есть в обоих множествах, нельзя считать дважды.",
                    ),
                ),
                (
                    L("Complete group of events", "Полная группа событий"),
                    r"B_i\cap B_j=\varnothing\ (i\ne j),\qquad \bigcup_{i=1}^{n}B_i=\Omega",
                    L(
                        "Events that do not overlap and together cover everything. Used in week 3.",
                        "События не пересекаются и вместе покрывают всё. Понадобится на неделе 3.",
                    ),
                ),
            ],
        ),
        (
            L("Discrete probability space", "Дискретное вероятностное пространство"),
            [
                (
                    L("Outcomes and their probabilities", "Исходы и их вероятности"),
                    r"\Omega=\{\omega_1,\dots,\omega_n\},\qquad p_i=P(\omega_i)\ge 0,\qquad \sum_{i=1}^{n}p_i=1",
                    None,
                ),
                (
                    L("Probability of an event", "Вероятность события"),
                    r"P(A)=\sum_{\omega_i\in A}p_i",
                    None,
                ),
                (
                    L("Classical definition", "Классическое определение"),
                    r"P(A)=\frac{|A|}{|\Omega|}=\frac{m}{n}",
                    L(
                        "Only for equally likely outcomes: m favourable outcomes out of n possible.",
                        "Только для равновозможных исходов: m благоприятных из n возможных.",
                    ),
                ),
            ],
        ),
        (
            L("Combinatorics", "Комбинаторика"),
            [
                (
                    L("Product rule", "Правило произведения"),
                    r"N=n_1\cdot n_2\cdots n_k",
                    L(
                        "If a choice is made in k steps with n₁, n₂, …, n_k options.",
                        "Если выбор делается за k шагов, где в шагах n₁, n₂, …, n_k вариантов.",
                    ),
                ),
                (
                    L("Factorial and permutations", "Факториал и перестановки"),
                    r"n!=1\cdot 2\cdots n,\qquad 0!=1,\qquad P_n=n!",
                    L("Ways to order n different objects.", "Число способов упорядочить n различных объектов."),
                ),
                (
                    L("Arrangements", "Размещения"),
                    r"A_n^k=\frac{n!}{(n-k)!}",
                    L("Choose k of n and the order matters.", "Выбираем k из n, порядок важен."),
                ),
                (
                    L("Combinations", "Сочетания"),
                    r"C_n^k=\binom{n}{k}=\frac{n!}{k!\,(n-k)!}",
                    L("Choose k of n and the order does not matter.", "Выбираем k из n, порядок не важен."),
                ),
                (
                    L("Properties of combinations", "Свойства сочетаний"),
                    r"C_n^k=C_n^{n-k},\qquad C_n^k=C_{n-1}^{k-1}+C_{n-1}^{k}",
                    None,
                ),
                (
                    L("With repetitions", "С повторениями"),
                    r"\tilde{A}_n^k=n^k,\qquad P(n_1,\dots,n_m)=\frac{n!}{n_1!\,n_2!\cdots n_m!}",
                    L(
                        "Arrangements with repetition and permutations of a multiset.",
                        "Размещения с повторениями и перестановки с повторяющимися элементами.",
                    ),
                ),
            ],
        ),
    ],
    # ------------------------------------------------------------------ week 2
    "f_prob": [
        (
            L("Probability space", "Вероятностное пространство"),
            [
                (
                    L("Triple", "Тройка"),
                    r"(\Omega,\ \mathcal{F},\ P)",
                    L(
                        "Ω — all outcomes, 𝓕 — the events we can measure, P — probability.",
                        "Ω — все исходы, 𝓕 — события, которые можно измерить, P — вероятность.",
                    ),
                ),
                (
                    L("σ-algebra of events", "σ-алгебра событий"),
                    r"\Omega\in\mathcal{F};\qquad A\in\mathcal{F}\Rightarrow\overline{A}\in\mathcal{F};\qquad A_1,A_2,\dots\in\mathcal{F}\Rightarrow\bigcup_{i}A_i\in\mathcal{F}",
                    None,
                ),
            ],
        ),
        (
            L("Kolmogorov axioms", "Аксиомы Колмогорова"),
            [
                (L("1. Non-negativity", "1. Неотрицательность"), r"P(A)\ge 0", None),
                (L("2. Normalisation", "2. Нормировка"), r"P(\Omega)=1", None),
                (
                    L("3. Additivity", "3. Аддитивность"),
                    r"A_i\cap A_j=\varnothing\ (i\ne j)\ \Rightarrow\ P\Big(\bigcup_{i=1}^{\infty}A_i\Big)=\sum_{i=1}^{\infty}P(A_i)",
                    L(
                        "For pairwise incompatible events probabilities add up.",
                        "Для попарно несовместных событий вероятности складываются.",
                    ),
                ),
            ],
        ),
        (
            L("Consequences", "Следствия"),
            [
                (
                    L("Basic properties", "Основные свойства"),
                    r"P(\varnothing)=0,\qquad P(\overline{A})=1-P(A),\qquad 0\le P(A)\le 1",
                    None,
                ),
                (
                    L("Monotonicity", "Монотонность"),
                    r"A\subset B\ \Rightarrow\ P(A)\le P(B),\qquad P(B\setminus A)=P(B)-P(A)",
                    None,
                ),
                (
                    L("Addition rule", "Теорема сложения"),
                    r"P(A\cup B)=P(A)+P(B)-P(A\cap B)",
                    None,
                ),
                (
                    L("Three events", "Три события"),
                    r"P(A\cup B\cup C)=P(A)+P(B)+P(C)-P(A\cap B)-P(A\cap C)-P(B\cap C)+P(A\cap B\cap C)",
                    None,
                ),
                (
                    L("Boole inequality", "Неравенство Буля"),
                    r"P\Big(\bigcup_{i=1}^{n}A_i\Big)\le\sum_{i=1}^{n}P(A_i)",
                    None,
                ),
            ],
        ),
        (
            L("Geometric probability", "Геометрическая вероятность"),
            [
                (
                    L("Length, area, volume", "Длина, площадь, объём"),
                    r"P(A)=\frac{\mu(A)}{\mu(\Omega)}",
                    L(
                        "μ is the length, area or volume. A point is thrown at random into Ω.",
                        "μ — длина, площадь или объём. Точка бросается в Ω наугад.",
                    ),
                ),
            ],
        ),
    ],
    # ------------------------------------------------------------------ week 3
    "f_cond": [
        (
            L("Conditional probability", "Условная вероятность"),
            [
                (
                    L("Definition", "Определение"),
                    r"P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(B)>0",
                    L(
                        "Probability of A when we already know that B happened.",
                        "Вероятность A, когда уже известно, что B произошло.",
                    ),
                ),
                (
                    L("Complement", "Дополнение"),
                    r"P(\overline{A}\mid B)=1-P(A\mid B)",
                    None,
                ),
                (
                    L("Multiplication rule", "Теорема умножения"),
                    r"P(A\cap B)=P(B)\,P(A\mid B)=P(A)\,P(B\mid A)",
                    None,
                ),
                (
                    L("Chain of events", "Цепочка событий"),
                    r"P(A_1\cap\dots\cap A_n)=P(A_1)\,P(A_2\mid A_1)\cdots P(A_n\mid A_1\cap\dots\cap A_{n-1})",
                    None,
                ),
            ],
        ),
        (
            L("Total probability", "Полная вероятность"),
            [
                (
                    L("Total probability formula", "Формула полной вероятности"),
                    r"P(A)=\sum_{i=1}^{n}P(B_i)\,P(A\mid B_i)",
                    L(
                        "B₁, …, B_n is a complete group of events (see week 1) and P(B_i) > 0.",
                        "B₁, …, B_n — полная группа событий (см. неделю 1), P(B_i) > 0.",
                    ),
                ),
                (
                    L("Two hypotheses", "Две гипотезы"),
                    r"P(A)=P(B)\,P(A\mid B)+P(\overline{B})\,P(A\mid\overline{B})",
                    None,
                ),
            ],
        ),
    ],
    # ------------------------------------------------------------------ week 4
    "f_indep": [
        (
            L("Two independent events", "Два независимых события"),
            [
                (
                    L("Definition", "Определение"),
                    r"P(A\cap B)=P(A)\,P(B)",
                    L(
                        "Knowing that B happened does not change the chance of A.",
                        "Если известно, что B произошло, шанс A не меняется.",
                    ),
                ),
                (
                    L("Equivalent form", "Равносильная форма"),
                    r"P(A\mid B)=P(A)\quad (P(B)>0)",
                    None,
                ),
                (
                    L("Complements", "Дополнения"),
                    r"P(A\cap\overline{B})=P(A)\,P(\overline{B}),\qquad P(\overline{A}\cap\overline{B})=P(\overline{A})\,P(\overline{B})",
                    L(
                        "If A and B are independent, so are A and B^c, A^c and B, A^c and B^c.",
                        "Если A и B независимы, то независимы и пары A и B^c, A^c и B, A^c и B^c.",
                    ),
                ),
            ],
        ),
        (
            L("Several events", "Несколько событий"),
            [
                (
                    L("Mutual independence", "Независимость в совокупности"),
                    r"P(A_{i_1}\cap\dots\cap A_{i_k})=P(A_{i_1})\cdots P(A_{i_k}),\qquad 1\le i_1<\dots<i_k\le n",
                    L(
                        "The equality must hold for every group of events. Pairwise independence is weaker: it checks only pairs.",
                        "Равенство должно выполняться для любой группы событий. Попарная независимость слабее: она проверяет только пары.",
                    ),
                ),
                (
                    L("At least one happens", "Хотя бы одно произойдёт"),
                    r"P\Big(\bigcup_{i=1}^{n}A_i\Big)=1-\prod_{i=1}^{n}\big(1-P(A_i)\big)",
                    L(
                        "For independent events. With equal p: 1 − (1 − p)ⁿ.",
                        "Для независимых событий. При одинаковом p: 1 − (1 − p)ⁿ.",
                    ),
                ),
            ],
        ),
        (
            L("Do not mix up", "Не путать"),
            [
                (
                    L("Independent is not incompatible", "Независимые ≠ несовместные"),
                    r"A\cap B=\varnothing,\ P(A)P(B)>0\ \Rightarrow\ P(A\cap B)=0\ne P(A)P(B)",
                    L(
                        "Incompatible events with positive probabilities are always dependent.",
                        "Несовместные события с ненулевыми вероятностями всегда зависимы.",
                    ),
                ),
            ],
        ),
    ],
    # ------------------------------------------------------------------ week 5
    "f_data": [
        (
            L("Data collection and preparation", "Сбор и подготовка данных"),
            [
                (
                    L("Sample size and percent", "Объём выборки и проценты"),
                    r"n,\qquad p=\frac{a}{b}\cdot 100",
                    L(
                        "n is the number of observations: each row of the survey is one observation. p is a percent.",
                        "n — число наблюдений: каждая строка опроса — одно наблюдение. p — процент.",
                    ),
                ),
                (
                    L("Cleaning answers", "Очистка ответов"),
                    r"x=\frac{a+b}{2},\qquad t_{\min}=60\cdot t_h",
                    L(
                        "A range becomes its midpoint (“10–15 min” → 12.5), hours become minutes (“1.5 hours” → 90).",
                        "Диапазон заменяется серединой («10–15 мин» → 12.5), часы переводятся в минуты («1.5 часа» → 90).",
                    ),
                ),
                (
                    L("Outlier fences", "Границы выбросов"),
                    r"\big[\,Q_1-1.5\,IQR,\ \ Q_3+1.5\,IQR\,\big]",
                    L(
                        "Values outside this interval are possible outliers.",
                        "Значения вне этого интервала — возможные выбросы.",
                    ),
                ),
            ],
        ),
        (
            L("Frequency distribution", "Частотное распределение"),
            [
                (
                    L("Frequencies", "Частоты"),
                    r"\sum_i n_i=n,\qquad w_i=\frac{n_i}{n},\qquad \sum_i w_i=1,\qquad F_i=\sum_{j\le i}w_j",
                    L(
                        "n_i — count in class i, w_i — relative frequency, F_i — cumulative frequency.",
                        "n_i — число в классе i, w_i — относительная частота, F_i — накопленная частота.",
                    ),
                ),
                (
                    L("Number and width of classes", "Число и ширина классов"),
                    r"k\approx 1+3.322\,\lg n,\qquad h=\frac{x_{\max}-x_{\min}}{k}",
                    L("Sturges' rule for k.", "Правило Стёрджеса для k."),
                ),
                (
                    L("Midpoint and density", "Середина класса и плотность"),
                    r"x_i'=\frac{a_i+b_i}{2},\qquad f_i=\frac{n_i}{n\,h}",
                    L(
                        "The histogram bar height can be n_i or the density f_i.",
                        "Высота столбца гистограммы — это n_i или плотность f_i.",
                    ),
                ),
            ],
        ),
        (
            L("Data description", "Описание данных"),
            [
                (
                    L("Mean", "Среднее"),
                    r"\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i,\qquad \bar{x}\approx\frac{1}{n}\sum_{i=1}^{k}n_i\,x_i'",
                    L("The second form is for grouped data.", "Вторая форма — для сгруппированных данных."),
                ),
                (
                    L("Median and mode", "Медиана и мода"),
                    r"\mathrm{Me}=\begin{cases}x_{(m+1)}, & n=2m+1\\[2pt] \dfrac{x_{(m)}+x_{(m+1)}}{2}, & n=2m\end{cases}",
                    L(
                        "x(i) is the i-th value of the sorted data. Median: the middle of the sorted data. Mode: the most frequent value.",
                        "x(i) — i-е значение упорядоченных данных. Медиана: середина упорядоченных данных. Мода: самое частое значение.",
                    ),
                ),
                (
                    L("Spread", "Разброс"),
                    r"R=x_{\max}-x_{\min},\qquad s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2,\qquad s=\sqrt{s^2}",
                    None,
                ),
                (
                    L("Quartiles and variation", "Квартили и вариация"),
                    r"IQR=Q_3-Q_1,\qquad CV=\frac{s}{\bar{x}}\cdot 100\%",
                    None,
                ),
            ],
        ),
    ],
}

# Short texts for the "Try it" tabs (calculators)
UI = {
    "EN": {
        "week": "WEEK",
        "school": "SCHOOL",
        "tab_formulas": "Formulas",
        "tab_try": "Try it",
        # school
        "pct_title": "Percent",
        "attended": "Attended classes",
        "total": "All classes",
        "a_gt_b": "Attended cannot exceed the total.",
        "speed_title": "Travel time",
        "distance": "Distance (km)",
        "speed": "Speed (km/h)",
        "mid_title": "Range midpoint",
        "from": "From",
        "to": "To",
        # sets
        "event_lab": "Event lab",
        "event_lab_note": "Ω = {1, …, 12}: a group of 12 students, one is picked at random (all outcomes are equally likely). Choose events A and B.",
        "col_event": "Event",
        "col_set": "Set",
        "de_morgan": "De Morgan: (A ∪ B)^c = A^c ∩ B^c",
        "incompatible": "A and B are incompatible: A ∩ B = ∅.",
        "comb_calc": "Combinatorics calculator",
        "k_gt_n": "k must not exceed n.",
        "guess": "Chance to guess one exact group of k out of n",
        # prob
        "pa_calc": "Probabilities of A and B",
        "pab_range": "For these P(A) and P(B), the value P(A ∩ B) must be between {lo:.2f} and {hi:.2f}.",
        "col_formula": "Formula",
        "col_value": "Value",
        "geo_calc": "Geometric probability: waiting for a bus",
        "geo_note": "A bus comes every T minutes. You arrive at a random moment, so the waiting time is uniform on [0, T].",
        "bus_period": "Bus interval T (min)",
        "bus_wait": "Maximum wait w (min)",
        # cond
        "cond_calc": "Conditional probability",
        "pb_zero": "P(B) must be greater than 0.",
        "ab_gt_b": "P(A ∩ B) cannot exceed P(B).",
        "tp_survey": "Total probability on the survey data",
        "tp_survey_note": "Event A: attendance at or above a threshold. Hypotheses B_i: transport types (they split the students into non-overlapping groups).",
        "att_thr": "Attendance threshold (%)",
        "col_hyp": "Hypothesis B_i",
        "col_k": "Count of A",
        "direct": "Direct count of A: k / n",
        "tp_manual": "Your own numbers",
        "sum_not_one": "P(B1) + P(B2) + P(B3) must equal 1 (now {s:.2f}).",
        # indep
        "ind_calc": "Two independent events",
        "atleast": "At least one of n independent events",
        "atleast_note": "Each event has probability p. Example: n servers, each fails with probability p. How likely is at least one failure?",
        "atleast_chart": "P(at least one) depending on n",
        "ind_survey": "Are travel time and attendance independent? (survey data)",
        "ind_survey_note": "A: travel time at or above a threshold. B: attendance at or above a threshold. For independent events P(A ∩ B) would be close to P(A)·P(B). This is only a descriptive check, not a hypothesis test.",
        "travel_thr": "Travel time threshold (min)",
        "close_indep": "The numbers are close: A and B look independent in this sample.",
        "far_indep": "The numbers differ: A and B look dependent in this sample.",
        "cond_vs": "P(B | A) compared with P(B)",
        # data
        "freq_title": "Frequency table builder (survey data)",
        "variable": "Variable",
        "classes": "Number of classes k",
        "sturges_hint": "Sturges' rule suggests k ≈ {k}.",
        "col_class": "Class",
        "col_mid": "Midpoint",
        "freq_chart": "Histogram and frequency polygon",
        "bars": "Histogram",
        "polygon": "Polygon",
        "grouped_mean": "Grouped mean vs exact mean",
        "desc_title2": "Data description",
        "col_stat": "Statistic",
        "mode": "Mode",
        "range": "Range",
        "cv": "Coefficient of variation (%)",
        "fences": "Outlier fences",
        "no_outliers": "No outliers found.",
        "outliers_found": "Possible outliers (outside the fences):",
        "constant": "All values are equal, so classes cannot be built.",
    },
    "RU": {
        "week": "НЕДЕЛЯ",
        "school": "ШКОЛА",
        "tab_formulas": "Формулы",
        "tab_try": "Попробуй",
        # school
        "pct_title": "Проценты",
        "attended": "Посещено занятий",
        "total": "Всего занятий",
        "a_gt_b": "Посещено не может быть больше, чем всего.",
        "speed_title": "Время в пути",
        "distance": "Расстояние (км)",
        "speed": "Скорость (км/ч)",
        "mid_title": "Середина диапазона",
        "from": "От",
        "to": "До",
        # sets
        "event_lab": "Лаборатория событий",
        "event_lab_note": "Ω = {1, …, 12}: группа из 12 студентов, наугад выбирают одного (исходы равновозможны). Выберите события A и B.",
        "col_event": "Событие",
        "col_set": "Множество",
        "de_morgan": "Де Морган: (A ∪ B)^c = A^c ∩ B^c",
        "incompatible": "A и B несовместны: A ∩ B = ∅.",
        "comb_calc": "Калькулятор комбинаторики",
        "k_gt_n": "k не должно превышать n.",
        "guess": "Шанс угадать одну конкретную группу из k элементов из n",
        # prob
        "pa_calc": "Вероятности A и B",
        "pab_range": "Для таких P(A) и P(B) значение P(A ∩ B) должно быть от {lo:.2f} до {hi:.2f}.",
        "col_formula": "Формула",
        "col_value": "Значение",
        "geo_calc": "Геометрическая вероятность: ожидание автобуса",
        "geo_note": "Автобус приходит каждые T минут. Вы приходите в случайный момент, поэтому время ожидания равномерно распределено на [0, T].",
        "bus_period": "Интервал автобуса T (мин)",
        "bus_wait": "Максимальное ожидание w (мин)",
        # cond
        "cond_calc": "Условная вероятность",
        "pb_zero": "P(B) должна быть больше 0.",
        "ab_gt_b": "P(A ∩ B) не может быть больше P(B).",
        "tp_survey": "Полная вероятность на данных опроса",
        "tp_survey_note": "Событие A: посещаемость не ниже порога. Гипотезы B_i: виды транспорта (они делят студентов на непересекающиеся группы).",
        "att_thr": "Порог посещаемости (%)",
        "col_hyp": "Гипотеза B_i",
        "col_k": "Число A",
        "direct": "Прямой подсчёт A: k / n",
        "tp_manual": "Ваши числа",
        "sum_not_one": "P(B1) + P(B2) + P(B3) должно равняться 1 (сейчас {s:.2f}).",
        # indep
        "ind_calc": "Два независимых события",
        "atleast": "Хотя бы одно из n независимых событий",
        "atleast_note": "У каждого события вероятность p. Пример: n серверов, каждый ломается с вероятностью p. Какова вероятность, что сломается хотя бы один?",
        "atleast_chart": "P(хотя бы одно) в зависимости от n",
        "ind_survey": "Независимы ли время в пути и посещаемость? (данные опроса)",
        "ind_survey_note": "A: время в пути не меньше порога. B: посещаемость не ниже порога. Для независимых событий P(A ∩ B) было бы близко к P(A)·P(B). Это лишь описательная проверка, а не статистический тест.",
        "travel_thr": "Порог времени в пути (мин)",
        "close_indep": "Числа близки: в этой выборке A и B выглядят независимыми.",
        "far_indep": "Числа различаются: в этой выборке A и B выглядят зависимыми.",
        "cond_vs": "P(B | A) в сравнении с P(B)",
        # data
        "freq_title": "Построитель таблицы частот (данные опроса)",
        "variable": "Переменная",
        "classes": "Число классов k",
        "sturges_hint": "Правило Стёрджеса даёт k ≈ {k}.",
        "col_class": "Класс",
        "col_mid": "Середина",
        "freq_chart": "Гистограмма и полигон частот",
        "bars": "Гистограмма",
        "polygon": "Полигон",
        "grouped_mean": "Среднее по группам и точное среднее",
        "desc_title2": "Описание данных",
        "col_stat": "Показатель",
        "mode": "Мода",
        "range": "Размах",
        "cv": "Коэффициент вариации (%)",
        "fences": "Границы выбросов",
        "no_outliers": "Выбросов не найдено.",
        "outliers_found": "Возможные выбросы (за пределами границ):",
        "constant": "Все значения равны, классы построить нельзя.",
    },
}
