# 🏎️ F1 Race Strategy Intelligence — Complete Tableau Dashboard Guide
### NST DVA Capstone 2 | Section A, Group 4
### Zero-to-Dashboard: A Complete Step-by-Step Guide for Absolute Beginners

---

> **READ THIS FIRST — What You Are Building**
>
> You are building **4 interactive dashboards** in Tableau Public (free software) that tell the story of Formula 1 race strategy from 1950 to 2026. The audience is a **Race Strategist** who needs to decide — before race day — whether to prioritize qualifying pace, pit stop speed, or circuit-specific tactics.
>
> Your 3 data files:
> - `master_fact.csv` — **27,304 rows** — one row per driver per race (every F1 race entry ever)
> - `constructor_season_kpis.csv` — **1,132 rows** — one row per constructor per year
> - `circuit_strategy_profile.csv` — **78 rows** — one row per circuit with strategy profile

---

## 📋 TABLE OF CONTENTS

1. [Install Tableau Public](#part-0-install-tableau-public)
2. [Connect Your Data Files](#part-1-connect-your-data-files)
3. [Create All Calculated Fields](#part-2-create-all-calculated-fields)
4. [Dashboard 1 — Constructor Championship Intelligence](#dashboard-1-constructor-championship-intelligence)
5. [Dashboard 2 — Pit Stop Strategy Analysis](#dashboard-2-pit-stop-strategy-analysis)
6. [Dashboard 3 — Race Craft & Grid Delta Analysis](#dashboard-3-race-craft--grid-delta-analysis)
7. [Dashboard 4 — Circuit Intelligence World Map ⭐](#dashboard-4-circuit-intelligence-world-map-)
8. [Publish to Tableau Public](#part-8-publish-to-tableau-public)
9. [Final Screenshots for GitHub](#part-9-final-screenshots-for-github)
10. [What Each Dashboard Looks Like (Visual Layout)](#part-10-visual-layout-reference)

---

## PART 0: Install Tableau Public

### Step 0.1 — Download
1. Go to: **https://public.tableau.com/en/software/public**
2. Click the big **"Download Tableau Public"** button
3. Enter your email address → Click **"Download the App"**
4. The file downloads (about 500MB — it is a big software)

### Step 0.2 — Install
- **Windows:** Double-click the `.exe` file → click Next → Next → Install
- **Mac:** Double-click the `.dmg` file → drag Tableau to Applications folder
- Launch Tableau Public from your Start Menu or Applications folder

### Step 0.3 — Create Free Account
1. When Tableau opens, it asks you to sign in
2. Click **"Create one for free"**
3. Use your university email → create a password
4. **Save these login details** — you will need them at the end to publish

---

## PART 1: Connect Your Data Files

> **Where to find your files:** They should be in your project folder at `data/processed/`. The three files are `master_fact.csv`, `constructor_season_kpis.csv`, and `circuit_strategy_profile.csv`.

### Step 1.1 — Connect the First File (master_fact.csv)

When Tableau opens, you see a blue panel on the left called **"Connect"**:

```
┌──────────────────────────────────────────┐
│  Connect                                 │
│  ─────────────────────────────────────   │
│  To a File                               │
│    ▶ Microsoft Excel                     │
│    ▶ Text File           ← CLICK THIS    │
│    ▶ JSON File                           │
│    ▶ PDF File                            │
│  ─────────────────────────────────────   │
│  To a Server                             │
└──────────────────────────────────────────┘
```

1. Click **"Text File"**
2. A file browser opens — navigate to your `data/processed/` folder
3. Select **`master_fact.csv`** → click **Open**
4. Tableau shows a preview of your data at the bottom of the screen
5. You will see column names like `resultId`, `year`, `constructor_name`, `grid`, `points`, etc.
6. At the bottom of the screen, click the orange tab that says **"Sheet 1"** — this opens your first worksheet

### Step 1.2 — Add the Second Data Source (constructor_season_kpis.csv)

You are now inside a worksheet. Now you will add the second file:

1. In the top menu bar, click **Data** → **New Data Source**
2. Click **"Text File"**
3. Select **`constructor_season_kpis.csv`** → click Open
4. Tableau adds this as a second data source — you will see it appear in the **Data** panel on the left side

### Step 1.3 — Add the Third Data Source (circuit_strategy_profile.csv)

Repeat the same steps:
1. Top menu → **Data** → **New Data Source**
2. Click **"Text File"**
3. Select **`circuit_strategy_profile.csv`** → click Open

### Step 1.4 — Verify You Have 3 Data Sources

Look at the **left panel** (Data pane). You should see 3 items:

```
Data                    Analytics
─────────────────────────────────
📊 master_fact (Text)
📊 constructor_season_kpis (Text)
📊 circuit_strategy_profile (Text)
```

✅ You are ready. Keep this window open.

### Step 1.5 — Set Geographic Roles (IMPORTANT for the World Map)

This step tells Tableau that lat/lng columns are map coordinates:

1. In the Data pane, click **circuit_strategy_profile** to make it active
2. Find the column called **`lng`** in the list
3. **Right-click** on `lng` → hover over **"Geographic Role"** → select **"Longitude"**
4. Find the column called **`lat`** in the list
5. **Right-click** on `lat` → hover over **"Geographic Role"** → select **"Latitude"**
6. **Right-click** on `country` → hover over **"Geographic Role"** → select **"Country/Region"**

> A small globe icon (🌐) should now appear next to lat, lng, and country in the Data pane.

---

## PART 2: Create All Calculated Fields

> **What is a Calculated Field?** It is a custom formula you write once. Tableau saves it and you can use it in any chart, just like a regular column. Think of it like writing a formula in Excel — except you write it once and reuse it everywhere.

### How to Create a Calculated Field (Do This for ALL 7 Fields Below)

1. Make sure **master_fact** is selected in the Data pane
2. Go to top menu → **Analysis** → **Create Calculated Field...**
3. A small window appears with two boxes: **Name** (top) and **Formula** (bottom)
4. Type the Name, then click in the formula box and type the formula exactly
5. Click **OK**

---

### Calculated Field 1 — Points Efficiency

| Field | Value |
|-------|-------|
| **Name** | `Points Efficiency` |
| **Formula** | `SUM([points]) / COUNTD([raceId])` |
| **What it means** | Average points earned per race — a fair way to compare teams that ran different numbers of races |

---

### Calculated Field 2 — DNF Rate

| Field | Value |
|-------|-------|
| **Name** | `DNF Rate` |
| **Formula** | `SUM([is_dnf]) / COUNT([resultId])` |
| **What it means** | Fraction of races where the car retired (Did Not Finish). 0.15 = 15% of races ended in retirement |

---

### Calculated Field 3 — Podium Rate

| Field | Value |
|-------|-------|
| **Name** | `Podium Rate` |
| **Formula** | `SUM([is_podium]) / COUNT([resultId])` |
| **What it means** | Fraction of races where the car finished in Top 3 |

---

### Calculated Field 4 — Win Rate

| Field | Value |
|-------|-------|
| **Name** | `Win Rate` |
| **Formula** | `SUM([is_win]) / COUNT([resultId])` |
| **What it means** | Fraction of races won |

---

### Calculated Field 5 — Avg Pit Seconds

| Field | Value |
|-------|-------|
| **Name** | `Avg Pit Seconds` |
| **Formula** | `AVG([avg_pit_ms]) / 1000` |
| **What it means** | Average pit stop duration in seconds (more readable than milliseconds) |

---

### Calculated Field 6 — Stop Count Bucket

| Field | Value |
|-------|-------|
| **Name** | `Stop Count Bucket` |
| **Formula** | `IF [stop_count] >= 3 THEN '3-stop' ELSEIF [stop_count] = 2 THEN '2-stop' ELSE '1-stop' END` |
| **What it means** | Groups races into 1-stop, 2-stop, or 3-stop strategy — used for stacked bar charts |

---

### Calculated Field 7 — High DNF Flag

| Field | Value |
|-------|-------|
| **Name** | `High DNF Flag` |
| **Formula** | `[DNF Rate] > 0.15` |
| **What it means** | TRUE if a constructor retires more than 15% of their races — used to color bar charts red |

---

✅ **Checkpoint:** You should now have 7 new calculated fields visible in the Data pane (they appear with a small **=** icon next to them).

---

## DASHBOARD 1: Constructor Championship Intelligence

> **Who is this for?** The **Team Principal** — the CEO of the F1 team. They want to see: are we getting better over time vs our rivals? Where are we losing points?
>
> **What it answers:** "Which mid-field constructors are improving their points-per-race efficiency, and which are losing points to reliability problems?"

---

### Visual Layout of Dashboard 1

```
┌─────────────────────────────────────────────────────────────────────┐
│         CONSTRUCTOR CHAMPIONSHIP INTELLIGENCE                        │
│         Season Performance Overview                                  │
├───────────┬───────────┬───────────┬────────────────────────────────-│
│ 📊 TOTAL  │ ⚡ POINTS  │ 💀 DNF    │ 🏆 PODIUM                      │
│  POINTS   │ EFFICIENCY │  RATE     │   RATE                         │
│   [BAN]   │  [BAN]    │  [BAN]    │   [BAN]                        │
├───────────┴───────────┴───────────┴────────────────────────────────-┤
│                                     │                               │
│   📈 POINTS EFFICIENCY TREND        │  📊 DNF RATE BAR CHART        │
│   (Line chart, 2010–2024)           │  (Which teams fail most?)     │
│   One colored line per constructor  │  Red = above 15% failure      │
│                                     │  rate. Avg reference line.    │
│                                     │                               │
├─────────────────────────────────────┴───────────────────────────────┤
│  Filters: [Constructor ▼ Multi-select]  [Year: 2010 ──────── 2024]  │
└─────────────────────────────────────────────────────────────────────┘
SIZE: 1200 x 700 pixels
```

---

### Worksheet 1A — Points Efficiency Trend Line

**What it shows:** A colored line for each constructor showing their average points-per-race from 2010 to 2024. Rising lines = improving teams. You want to spot which mid-field teams climbed.

#### Steps:

1. At the bottom of Tableau, **right-click** the "Sheet 1" tab → click **Rename** → type `1A - Points Efficiency Trend`
2. In the **Data** pane on the left, make sure **master_fact** is selected
3. Find the column **`year`** in the list. **Drag it** to the **Columns** shelf (the horizontal bar at the top of the white canvas area)
4. Find **`Points Efficiency`** (your calculated field — it has an = sign). **Drag it** to the **Rows** shelf
5. Find **`constructor_name`** column. **Drag it** to the **Color** box on the **Marks card** (the card in the middle-left area)
6. In the **Show Me** panel on the right side of the screen, click **"Lines (continuous)"** — this changes the chart to a line chart

**Set the Year Filter (2010–2024 only):**
7. In the Data pane, find `year`. **Drag it** to the **Filters** shelf (the card above Marks)
8. A dialog box appears → click **"Range of Values"** → set **Minimum: 2010**, **Maximum: 2024** → click OK
9. Right-click the filter in the Filters shelf → **"Show Filter"** — this adds a slider to your chart

**Edit the Title:**
10. Double-click the chart title at the top → delete the default text → type:
    > **Mid-Field Constructor Points Efficiency 2010–2024**

**Format the Chart:**
11. Right-click the Y-axis → **Edit Axis** → change title to `Points Per Race`
12. Right-click the X-axis → **Edit Axis** → change title to `Season Year`

---

### Worksheet 1B — DNF Rate Bar Chart (Who Keeps Breaking Down?)

**What it shows:** A horizontal bar chart ranking constructors by how often their cars retire. Red bars = teams with serious reliability problems. A dotted average line shows the benchmark.

#### Steps:

1. Click the **+** icon at the bottom of Tableau to create a **New Sheet** → rename it `1B - DNF Rate Bar`
2. Make sure **master_fact** data source is active
3. Drag **`constructor_name`** → **Columns** shelf
4. Drag **`DNF Rate`** (your calculated field) → **Rows** shelf
5. The chart shows as a bar chart by default. If not: in **Show Me** → click **"Bar Charts"**

**Sort the bars (highest DNF at top):**
6. Click the Y-axis label → a small sort icon appears → click the **descending sort** arrow

**Add a Reference Line (Average DNF Line):**
7. Click the **"Analytics"** tab (next to Data tab at the top of the left panel)
8. Find **"Reference Line"** in the list → **drag it** onto the chart canvas
9. A dialog appears → set:
   - Value: **Average** → select `DNF Rate`
   - Label: **Custom** → type `League Avg`
   - Line style: **Dashed**
   - Color: **Dark Gray**
10. Click **OK**

**Color: Red for High DNF Teams:**
11. Drag **`High DNF Flag`** (your calculated field) → **Color** box on the Marks card
12. Click the **Color** box → **Edit Colors**:
    - TRUE → set to **Red (#E53935)**
    - FALSE → set to **Green (#43A047)**

**Edit Title:**
13. Double-click title → type: **Constructors Losing Points to Reliability Failures**

---

### Worksheet 1C — KPI Summary BAN Cards (Big Numbers)

**What it shows:** 4 giant numbers at the top of the dashboard — like a sports scoreboard. When the user selects a constructor using the filter, these numbers update instantly.

#### Steps:

**Card 1 — Total Points:**
1. New Sheet → rename `1C - KPI Total Points`
2. Drag **`points`** → **Text** box on the Marks card (NOT to Rows or Columns)
3. In the Marks dropdown (top of Marks card), change from "Automatic" to **"Text"**
4. Click the **Text** box → click **...** (three dots) → format the number: font size **48**, bold, color **White**
5. Double-click the title → type: `🏆 Total Points`

**Card 2 — Points Efficiency:**
6. New Sheet → rename `1C - KPI Points Efficiency`
7. Drag **`Points Efficiency`** → **Text** on Marks card → change mark type to Text
8. Format: font **48**, bold, white → title: `⚡ Points Per Race`

**Card 3 — DNF Rate:**
9. New Sheet → rename `1C - KPI DNF Rate`
10. Drag **`DNF Rate`** → Text on Marks → mark type: Text
11. Right-click the pill in the Marks card → **Format** → Number → Percentage, 1 decimal place
12. Font **48**, bold, color **Red** → title: `💀 DNF Rate`

**Card 4 — Podium Rate:**
13. New Sheet → rename `1C - KPI Podium Rate`
14. Drag **`Podium Rate`** → Text → mark type: Text → format as Percentage
15. Font **48**, bold, **Gold (#FFC107)** → title: `🏅 Podium Rate`

---

### Assemble Dashboard 1

1. At the bottom of Tableau, click the **dashboard icon** (grid with + symbol) to create a **New Dashboard**
2. Rename the dashboard tab to `Dashboard 1 - Constructor Intel`

**Set Dashboard Size:**
3. On the left panel under **Dashboard**, find **"Size"**
4. Click the dropdown → select **"Fixed Size"** → set **Width: 1200**, **Height: 700**

**Add a Dark Background:**
5. From the left panel, drag **"Blank"** onto the canvas → it fills the whole area
6. From the left panel, find **"Layout"** → set **Background color** to **#1A1A2E** (very dark navy — F1 themed)

**Place the Sheets:**
7. From the left panel under **Sheets**, drag **`1C - KPI Total Points`** to the top-left of the canvas
8. Drag **`1C - KPI Points Efficiency`** next to it (top, second position)
9. Drag **`1C - KPI DNF Rate`** next (top, third)
10. Drag **`1C - KPI Podium Rate`** (top, fourth)
11. Resize all 4 cards to be the same width and about **100px tall** (drag the borders)
12. Drag **`1A - Points Efficiency Trend`** to the **left 60%** of the remaining space below the cards
13. Drag **`1B - DNF Rate Bar`** to the **right 40%** of the remaining space

**Add Dashboard Title:**
14. From left panel, drag **"Text"** to the very top of the canvas
15. Type: `🏎️ CONSTRUCTOR CHAMPIONSHIP INTELLIGENCE — Season Performance Overview`
16. Set font: **Arial, 18pt, Bold, White**

**Add Filters (Interactive Controls):**
17. Click on the trend line chart (1A) to select it
18. Click the small **dropdown arrow** at the top-right of the chart → **"Filters"** → select **`constructor_name`**
19. A filter control appears on the right side of the dashboard → click its dropdown → select **"Multiple Values (List)"**
20. Repeat for the `year` filter → change to **"Range Slider"**
21. Right-click the `constructor_name` filter → **"Apply to Worksheets"** → **"All Using This Data Source"**
    - This makes the filter update ALL 4 charts simultaneously

---

## DASHBOARD 2: Pit Stop Strategy Analysis

> **Who is this for?** The **Strategy Director** — the person who plans pit stop timing.
>
> **What it answers:** "Does investing in faster pit stops actually improve our finishing position? What stop strategy do top-10 finishers use at different circuits?"

---

### Visual Layout of Dashboard 2

```
┌─────────────────────────────────────────────────────────────────────┐
│         PIT STOP STRATEGY ANALYSIS                                  │
│         Does Pit Speed Actually Win Races?                          │
├─────────────────────────────────────────┬───────────────────────────┤
│                                         │                           │
│  📉 PIT DURATION vs FINAL POSITION      │  📊 STOP COUNT STACKED    │
│  SCATTER PLOT                           │  BAR CHART                │
│                                         │                           │
│  X = Avg pit stop speed (seconds)       │  X = Constructor name     │
│  Y = Average final finishing position   │  Y = Number of races      │
│  Color = Constructor team               │  Color = 1/2/3 stops      │
│  Size = Number of stops                 │  (Top 10 finishers only)  │
│  Trend line shows correlation           │                           │
│                                         │                           │
├─────────────────────────────────────────┴───────────────────────────┤
│  Filters: [Year: ────────]  [Constructor ▼]  [Cluster ▼]           │
└─────────────────────────────────────────────────────────────────────┘
SIZE: 1200 x 700 pixels
```

---

### Worksheet 2A — Pit Duration vs Final Position Scatter Plot

**What it shows:** Each dot is one constructor in one year. Dots on the left = fast pit crews. Dots at the top = bad finishing positions. A downward-sloping trend line proves faster pit stops = better results.

#### Steps:

1. New Sheet → rename `2A - Pit Duration Scatter`
2. Data source: **master_fact**
3. Drag **`Avg Pit Seconds`** (calculated field) → **Columns**
4. Drag **`positionOrder`** → **Rows** → right-click the pill → **"Measure"** → **"Average"**
5. Drag **`constructor_short`** → **Color** on Marks card
6. Drag **`stop_count`** → **Size** on Marks card

**Add the Trend Line:**
7. Click **Analytics** tab (left panel)
8. Find **"Trend Line"** → drag it onto the canvas
9. A popup asks what type → select **"Linear"**
10. Right-click the trend line → **Edit Trend Line** → check **"Show Confidence Bands"** → color: **White, 50% transparent**

**Edit Axes:**
11. Right-click X-axis → **Edit Axis** → title: `Avg Pit Stop Duration (seconds)` → range: set min to 18, max to 35
12. Right-click Y-axis → **Edit Axis** → title: `Average Finishing Position` → check **"Reversed"** (P1 at top)

**Add Tooltip Text:**
13. Click **Tooltip** on the Marks card
14. Type:
```
Constructor: <constructor_short>
Avg Pit Stop: <Avg Pit Seconds> seconds
Avg Finish: P<AVG(positionOrder)>
```

**Title:** `⏱️ Faster Pit Stops Correlate With Better Finishing Position`

---

### Worksheet 2B — Stop Count Strategy Stacked Bar (Top-10 Finishers Only)

**What it shows:** For each constructor, how often do their top-10 finishes involve 1 stop, 2 stops, or 3 stops? This reveals each team's preferred race strategy.

#### Steps:

1. New Sheet → rename `2B - Stop Count Stacked Bar`
2. Data source: **master_fact**
3. Drag **`constructor_name`** → **Rows**
4. Drag **`resultId`** → **Columns** → right-click → **"Measure"** → **"Count"**
5. Drag **`stop_count_bucket`** → **Color** on Marks card

**Filter for Top 10 Finishers Only:**
6. Drag **`positionOrder`** → **Filters** shelf
7. Dialog appears → **"Range of Values"** → set **Max: 10** → click OK

**Set Colors:**
8. Click **Color** box → **Edit Colors**:
   - `1 stop` → **Blue (#1565C0)**
   - `2 stops` → **Orange (#E65100)**
   - `3+ stops` → **Red (#B71C1C)**

**Sort bars:**
9. Right-click the Y-axis (constructor names) → **Sort** → by field → **Count(resultId)** → Descending

**Title:** `🔧 How Top-10 Finishers Distribute Their Stop Strategy by Constructor`

---

### Worksheet 2C — Pit Duration Improvement Over Time

**What it shows:** Are pit crews getting faster year by year? One line per constructor showing their average fastest pit stop duration across seasons.

#### Steps:

1. New Sheet → rename `2C - Pit Improvement Trend`
2. Data source: **master_fact**
3. Drag **`year`** → **Columns**
4. Drag **`fastest_pit_ms`** → **Rows** → right-click → **Average** → then right-click again → **"Dual Axis"** idea: divide by 1000 by using `fastest_pit_seconds` if available, OR use `Avg Pit Seconds` calculated field
5. Actually: Drag **`Avg Pit Seconds`** → **Rows**
6. Drag **`constructor_name`** → **Color**
7. Filter **`year`** to 2010–2024

**Title:** `📉 Pit Crew Speed Improvement Trajectory 2010–2024`

---

### Assemble Dashboard 2

1. New Dashboard → rename `Dashboard 2 - Pit Stop Analysis`
2. Size: **Fixed: 1200 x 700**
3. Dark background: **#0D0D1A**
4. Place **2A** on left (60% width)
5. Place **2B** on right (40% width)
6. Place **2C** below both (full width, shorter height ~200px)
7. Add dashboard title text: `🔧 PIT STOP STRATEGY ANALYSIS — Does Pit Speed Win Races?`
8. Add filters: `year` (Range Slider), `constructor_name` (Multi-select list), `cluster_label` (Dropdown)
9. Apply all filters to all worksheets → right-click filter → Apply to Worksheets → All Using This Data Source

---

## DASHBOARD 3: Race Craft & Grid Delta Analysis

> **Who is this for?** The **Race Strategist** — the person making calls during the race itself.
>
> **What it answers:** "Which constructors consistently out-race their qualifying position? Does starting P5 vs P10 actually make a huge difference?"
>
> **Hero metric: `grid_to_finish_delta`** — positive = gained positions on race day, negative = lost positions. This isolates race strategy from car pace.

---

### Visual Layout of Dashboard 3

```
┌─────────────────────────────────────────────────────────────────────┐
│         RACE CRAFT ANALYSIS — Grid-to-Finish Delta                  │
│         Which Teams Win More Positions Than They Start?             │
├─────────────────────────────────────────┬───────────────────────────┤
│                                         │                           │
│  📦 GRID DELTA BOX PLOT                 │  🔥 GRID vs FINISH        │
│  by Constructor                         │  POSITION HEATMAP         │
│                                         │                           │
│  X = Constructor (short code)           │  X = Starting grid (1–20) │
│  Y = grid_to_finish_delta               │  Y = Finishing position   │
│  Above 0 = gained positions             │  Color = How often this   │
│  Red line at Y=0                        │  (grid,finish) pair occurs│
│  Box shows spread of performance        │                           │
├─────────────────────────────────────────┴───────────────────────────┤
│  📊 ERA COMPARISON: V10/V8 Era vs Turbo Hybrid Era (Avg Delta)      │
├─────────────────────────────────────────────────────────────────────┤
│  Filters: [Constructor ▼]  [Year: ────────]  [Era ▼]               │
└─────────────────────────────────────────────────────────────────────┘
SIZE: 1200 x 750 pixels
```

---

### Worksheet 3A — Grid Delta Box Plot by Constructor

**What it shows:** A box-and-whisker chart for each constructor. The box shows the typical range of positions gained/lost. The line in the middle is the median. Above the red 0-line = team usually gains positions. This is the most powerful chart in your project.

#### Steps:

1. New Sheet → rename `3A - Grid Delta Box Plot`
2. Data source: **master_fact**
3. Drag **`constructor_short`** → **Columns**
4. Drag **`grid_to_finish_delta`** → **Rows**
5. In the **Marks** dropdown, change from "Automatic" to **"Circle"** (this is necessary for box plots)
6. In the **Show Me** panel on the right → click **"Box-and-Whisker Plot"**
   - If you don't see this option, first drag constructor_short to Columns and grid_to_finish_delta to Rows, then click the box plot icon in Show Me

**Add the Zero Reference Line (most important!):**
7. Click **Analytics** tab
8. Find **"Reference Line"** → drag it to the chart
9. Set:
   - Value: **Constant** → type `0`
   - Label: **Custom** → type `Zero = No Change`
   - Line style: **Solid**
   - Color: **Red (#F44336)**
   - Thickness: **2px**
10. Click OK

**Sort constructors by median delta (best on left):**
11. Right-click X-axis → **Sort** → by field → **Median** of `grid_to_finish_delta` → Descending

**Filter to 2010–2024:**
12. Drag `year` → Filters → Range: 2010 to 2024

**Color the boxes:**
13. Drag **`grid_delta_category`** → **Color**:
    - `Gained 3+` → **Dark Green (#1B5E20)**
    - `Gained 1-2` → **Light Green (#81C784)**
    - `Held Position` → **Gray (#9E9E9E)**
    - `Lost Positions` → **Red (#C62828)**

**Title:** `📦 Which Constructors Consistently Beat Their Qualifying Grid Position?`

---

### Worksheet 3B — Grid vs Final Position Heatmap

**What it shows:** A 20x20 grid. Each cell = one combination of (starting position, finishing position). Darker color = this combination happened more often in the dataset. You instantly see a diagonal bright line (most people finish near where they start) and outliers where strategy made a huge difference.

#### Steps:

1. New Sheet → rename `3B - Grid Finish Heatmap`
2. Data source: **master_fact**
3. Drag **`grid`** → **Columns** → right-click the pill → **Dimension** (make sure it's not treated as a measure)
4. Drag **`positionOrder`** → **Rows** → right-click → **Dimension**
5. In the **Marks** dropdown → select **"Square"**
6. Drag **`resultId`** → **Color** → right-click → **Measure** → **Count**

**Set the Color Palette:**
7. Click the **Color** box → **Edit Colors**
8. Select palette: **"Red-Blue Diverging"** → check **"Reversed"** (so dark = more common)
9. Click **Advanced** → set **Center**: 0

**Filter to realistic range:**
10. Drag `grid` → Filters → Range: 1 to 20
11. Drag `positionOrder` → Filters → Range: 1 to 20
12. Drag `year` → Filters → Range: 2010 to 2024

**Title:** `🔥 Qualifying P1–5 Drivers Rarely Fall More Than 3 Places on Race Day`

---

### Worksheet 3C — Era Comparison Bar Chart

**What it shows:** Simple comparison: Did the V8/V10 era have more overtaking than the Turbo Hybrid era? Uses the `era` column.

#### Steps:

1. New Sheet → rename `3C - Era Comparison`
2. Data source: **master_fact**
3. Drag **`era`** → **Columns**
4. Drag **`grid_to_finish_delta`** → **Rows** → right-click → **Average**
5. Mark type: **Bar**
6. Drag **`era`** → **Color**:
   - `V10 Era` → **Gold (#FFC107)**
   - `V8 Era` → **Orange (#FF5722)**
   - `Turbo Hybrid Era` → **Cyan (#00BCD4)**
7. Add Reference Line at 0 (same as above)

**Title:** `⚡ Are Modern Hybrid-Era Races Less Exciting? Average Position Gain by Era`

---

### Assemble Dashboard 3

1. New Dashboard → `Dashboard 3 - Race Craft`
2. Size: **1200 x 750**, Background: **#0A0A1A**
3. Place **3A** (box plot) on left 55%
4. Place **3B** (heatmap) on right 45%
5. Place **3C** (era comparison) along the bottom full width at ~150px height
6. Title: `🏎️ RACE CRAFT ANALYSIS — Who Races Better Than They Qualify?`
7. Add filters: `constructor_name`, `year` (slider), `era` (dropdown)
8. Apply all filters to all worksheets

---

## DASHBOARD 4: Circuit Intelligence World Map ⭐

> **This is the STAR of your project.** No one else will have a world map that lights up with F1 circuit strategy data.
>
> **Who is this for?** The **Race Engineer** preparing for a specific Grand Prix the following week.
>
> **What it answers:** "For THIS specific circuit I am going to this weekend — based on 15 years of history — should I prioritize qualifying or pit strategy? How many stops should we plan for?"

---

### Visual Layout of Dashboard 4

```
┌──────────────────────────────────────────────────────────────────────┐
│   CIRCUIT INTELLIGENCE — Race Strategy by Track Archetype            │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│   🌍 WORLD MAP OF ALL 78 F1 CIRCUITS                                 │
│   (Top 60% of dashboard height)                                       │
│                                                                       │
│   🔴 RED DOTS = Qualifying-Dominant (must qualify well)               │
│   🟢 GREEN DOTS = Strategy-Dominant (pit strategy wins)               │
│   🟠 ORANGE DOTS = Mixed (read the race)                              │
│   DOT SIZE = Qualifying Lock-In Score (bigger = harder to overtake)  │
│                                                                       │
│   [Click any circuit to filter the charts below]                      │
│                                                                       │
├────────────────────────────┬─────────────────────────────────────────┤
│ 📊 QUALIFYING LOCK-IN      │  🔢 OPTIMAL STOP COUNT                  │
│ SCORE BAR CHART            │  PER CIRCUIT BAR CHART                  │
│                            │                                          │
│ Monaco at top (hardest     │  Blue = 1-stop                          │
│ to overtake), Monza at     │  Orange = 2-stop                        │
│ bottom (most overtaking)   │  Red = 3-stop                           │
│                            │                                          │
├────────────────────────────┴─────────────────────────────────────────┤
│  Filter: [Cluster: All ▼ / Qualifying-Dominant / Strategy / Mixed]   │
└──────────────────────────────────────────────────────────────────────┘
SIZE: 1400 x 800 pixels
```

---

### Worksheet 4A — World Map of F1 Circuits ⭐

> This is the hardest but most impressive chart. Follow every step exactly.

#### Steps:

1. New Sheet → rename `4A - World Circuit Map`
2. In the **Data** pane, click **`circuit_strategy_profile`** to make it the active data source

**Build the Map:**
3. Find **`lng`** in the Data pane (it should have a 🌐 globe icon from Part 1.5)
4. **Drag `lng`** → **Columns** shelf
5. Find **`lat`** → **Drag `lat`** → **Rows** shelf
6. Tableau automatically switches to **Map view** — you see a world map with dots! 🎉

> **If the map doesn't appear:** In the top menu → **Show Me** → click the **Map** icon (globe shape)

**Make sure each dot = one circuit:**
7. Find **`circuit_name`** in the Data pane → drag it → **Detail** box on the Marks card
   - This ensures there is exactly one dot per circuit (78 dots total)

**Color the dots by circuit archetype:**
8. Find **`cluster_label`** → drag it → **Color** on the Marks card
9. Click the **Color** box → **Edit Colors**:
   - `Qualifying-Dominant` → **Red (#E53935)**
   - `Strategy-Dominant` → **Green (#43A047)**
   - `Mixed` → **Orange (#FB8C00)**
   - *(empty/blank)* → **Light Gray (#BDBDBD)**

**Size dots by Lock-In Score (bigger = harder to overtake):**
10. Find **`qualifying_lock_in_score`** → drag it → **Size** on Marks card
11. Click **Size** box → adjust slider to make dots visible but not overlapping (try 60–80% of max)

**Customize the Map Background:**
12. In top menu → **Map** → **Map Layers...**
13. A panel opens on the left — set:
    - Style: **Dark** (makes the map dark/F1-themed)
    - Uncheck: "Country/Region Names", "Region Labels" (too cluttered)
    - Keep: "Coastline", "Country Borders"

**Add Custom Tooltip (the popup when you hover over a circuit):**
14. Click **Tooltip** on the Marks card
15. Delete all existing text → type:
```
🏎️ CIRCUIT: <circuit_name>
🌍 COUNTRY: <country>

📊 STRATEGY ARCHETYPE: <cluster_label>
🔒 QUALIFYING LOCK-IN: <qualifying_lock_in_score>%
🛑 OPTIMAL PIT STOPS: <optimal_stop_count>
📈 AVG GRID DELTA: <avg_delta>
```

**Add Filter Control:**
16. Drag **`cluster_label`** → **Filters** shelf
17. Right-click in Filters shelf → **Show Filter** → change filter type to **Single Value (dropdown)**

**Edit Map Title:**
18. Double-click title → type: `🌍 Circuit Strategy Archetypes — Where Does Qualifying vs Pit Strategy Win Races?`

---

### Worksheet 4B — Qualifying Lock-In Score Bar Chart

**What it shows:** Ranked list of all circuits from "hardest to overtake" (Monaco at top, near 90) to "easiest to overtake" (Monza near 20). Red bars = must qualify well, green bars = strategy can save you.

#### Steps:

1. New Sheet → rename `4B - Lock-In Score Bar`
2. Data source: **circuit_strategy_profile**
3. Drag **`circuit_name`** → **Rows**
4. Drag **`qualifying_lock_in_score`** → **Columns**
5. Mark type: **Bar**

**Sort (highest lock-in at top):**
6. Right-click the X-axis → **Sort** → by field → **qualifying_lock_in_score** → Descending

**Color by cluster:**
7. Drag **`cluster_label`** → **Color** (same colors as map: Red/Green/Orange)

**Add value labels on bars:**
8. Drag **`qualifying_lock_in_score`** → **Label** on Marks card
9. Click **Label** box → check "Show mark labels" → alignment: **Right**

**Add Reference Line at 70 (danger threshold):**
10. Analytics tab → Reference Line → Constant → Value: 70 → Label: "High Lock-In Zone" → dashed red

**Title:** `🔒 Qualifying Lock-In Score by Circuit — Monaco Locks In 89% of Starting Order`

---

### Worksheet 4C — Optimal Stop Count Bar Chart

**What it shows:** For each circuit, what is the historically best number of pit stops among top-10 finishers? Blue = 1 stop (conservative), Orange = 2 stops (aggressive), Red = 3 stops (very aggressive).

#### Steps:

1. New Sheet → rename `4C - Optimal Stop Count`
2. Data source: **circuit_strategy_profile**
3. Drag **`circuit_name`** → **Rows**
4. Drag **`optimal_stop_count`** → **Columns**
5. Mark type: **Bar**

**Color by stop count value:**
6. Drag **`optimal_stop_count`** → **Color**
7. Click **Color** → **Edit Colors** → use sequential palette:
   - 1 → **Blue (#1565C0)**
   - 2 → **Orange (#E65100)**
   - 3 → **Red (#B71C1C)**

**Sort:**
8. Sort by `optimal_stop_count` → Ascending (1-stop circuits first)

**Filter by cluster:**
9. Drag `cluster_label` → Filters → Show Filter → Dropdown

**Title:** `🛑 Optimal Pit Stop Count Per Circuit — Strategy-Dominant Tracks Favour 2-Stop 68% of the Time`

---

### Worksheet 4D — Compound Bias vs Grid Delta Scatter

**What it shows:** Circuits with high tyre degradation (high compound_bias) tend to have bigger position swings. This tells teams whether to request Soft or Hard tyres from Pirelli.

#### Steps:

1. New Sheet → rename `4D - Compound Bias Scatter`
2. Data source: **circuit_strategy_profile**
3. Drag **`compound_bias`** → **Columns**
4. Drag **`avg_delta`** → **Rows**
5. Mark type: **Circle**
6. Drag **`cluster_label`** → **Color** (same colors as map)
7. Drag **`circuit_name`** → **Label** on Marks (so you can see which dot is which circuit)
8. Add trend line (Analytics tab → Trend Line → Linear)
9. Tooltip: include circuit_name, cluster_label, optimal_stop_count, qualifying_lock_in_score

**Title:** `🔥 Higher Tyre Degradation Circuits Have More Strategy-Driven Position Changes`

---

### Assemble Dashboard 4 ⭐

This is the most important dashboard to build carefully.

1. New Dashboard → rename `Dashboard 4 - Circuit Intelligence`
2. Size: **Fixed: 1400 x 800** (wider than the others to fit the map)
3. Background: **#0D1B2A** (deep dark blue)

**Layout:**
4. Drag **`4A - World Circuit Map`** → fill the top **60%** of the canvas (the map is the hero)
5. Drag **`4B - Lock-In Score Bar`** → bottom-left **50%** of remaining space
6. Drag **`4C - Optimal Stop Count`** → bottom-right **50%** of remaining space

**Add Dashboard Title:**
7. Drag "Text" from left panel → top of canvas
8. Type: `🌍 CIRCUIT INTELLIGENCE — Race Strategy by Track Archetype`
9. Font: **Arial, 20pt, Bold, White**

**Add Explanatory Subtitle:**
10. Below the title, add another Text box:
    > `Select a circuit cluster to see which tracks require qualifying pace vs pit strategy — and how many stops historically win here.`

**CRITICAL — Make the Cluster Filter Control All 4 Charts:**
11. Click the **`cluster_label`** filter in the Filters shelf of the map
12. Right-click → **"Apply to Worksheets"** → **"All Using Related Data Sources"**
13. This is the magic: click one cluster on the map → ALL 4 charts update simultaneously

**Add Legend Box:**
14. Drag "Text" from left panel to a corner
15. Type:
```
🔴 QUALIFYING-DOMINANT
   Must qualify well. 1-stop safe.
   Monaco, Hungary, Singapore

🟢 STRATEGY-DOMINANT
   Grid less important. 2-stop attack.
   Monza, Bahrain, Silverstone

🟠 MIXED
   Read the race. Safety car plays role.
   Most other circuits
```
16. Font: **12pt, White, italic**

---

## PART 8: Publish to Tableau Public

1. Top menu → **File** → **Save to Tableau Public As...**
2. It will ask you to sign in → use the account you created in Part 0
3. Name your workbook: `F1 Race Strategy Intelligence — NST DVA Capstone G4`
4. Click **Save**
5. Tableau uploads your workbook (takes 1–3 minutes)
6. When done, it opens your workbook in a web browser automatically
7. **IMMEDIATELY copy the URL from the browser address bar** — it looks like:
   ```
   https://public.tableau.com/app/profile/YOUR_NAME/viz/F1RaceStrategyIntelligence/Dashboard1
   ```
8. Paste this URL in:
   - `tableau/dashboard_links.md` in your GitHub repo
   - Cover page of your project report
   - Slide 7 of your PPT

---

## PART 9: Final Screenshots for GitHub

Take a screenshot of each dashboard at full size:

| Screenshot | How to Capture |
|------------|----------------|
| **Windows** | Press `Win + Shift + S` → select the full dashboard |
| **Mac** | Press `Cmd + Shift + 4` → drag to select full dashboard |

| Filename | Dashboard |
|----------|-----------|
| `dashboard1_executive.png` | Constructor Championship Intelligence |
| `dashboard2_pitstop.png` | Pit Stop Strategy Analysis |
| `dashboard3_racecraft.png` | Race Craft & Grid Delta |
| `dashboard4_circuit.png` | Circuit Intelligence World Map |

Save all 4 PNGs to: `tableau/screenshots/` in your GitHub repo

---

## PART 10: Visual Layout Reference

### Color Palette Used Across ALL Dashboards

| Element | Color | Hex Code |
|---------|-------|----------|
| Dashboard background | Dark Navy | `#0D0D1A` |
| Qualifying-Dominant circuits | Red | `#E53935` |
| Strategy-Dominant circuits | Green | `#43A047` |
| Mixed circuits | Orange | `#FB8C00` |
| Win / positive delta | Gold | `#FFC107` |
| DNF / negative delta | Red | `#C62828` |
| 1-stop strategy | Blue | `#1565C0` |
| 2-stop strategy | Orange | `#E65100` |
| 3-stop strategy | Dark Red | `#B71C1C` |
| Text headings | White | `#FFFFFF` |
| Reference lines | Dotted Gray | `#757575` |

---

### Summary: What Each Dashboard Proves

| Dashboard | Key Question | Star Chart | Insight |
|-----------|-------------|------------|---------|
| **1 — Constructor Intel** | Are we improving? | Points Efficiency Trend | Which mid-field teams are climbing vs declining |
| **2 — Pit Stop** | Does pit speed matter? | Scatter: Pit Time vs Position | Faster pit stops correlate with 1+ better finishing positions |
| **3 — Race Craft** | Who races best? | Box plot of grid delta | Some constructors consistently gain 2+ positions vs grid |
| **4 — Circuit Intel** | What strategy per track? | World Map with clusters | 78 circuits categorized into 3 strategy archetypes |

---

### Common Tableau Mistakes to Avoid

| Mistake | How to Fix |
|---------|-----------|
| Map shows as table instead of map | In Show Me → click the Map/Globe icon |
| Filters don't affect all charts | Right-click filter → Apply to All Worksheets |
| Numbers show as decimals (e.g., 0.1500) | Right-click pill → Format → Number → Percentage |
| Dashboard is too big for screen | Dashboard menu → Size → Fit → Entire View |
| Colors look wrong | Click Color in Marks card → Edit Colors → manually set |
| Text labels overlap on bar chart | Right-click axis → Format → rotate labels 45° |
| Trend line not showing | Analytics tab → drag Trend Line → Linear |
| Lat/lng not recognized as map | Right-click column → Geographic Role → set manually |

---

*Guide Version 1.0 | F1 Race Strategy Intelligence | NST DVA Capstone 2 | Section A, Group 4*
*Data: 27,304 race entries | 78 circuits | 1,132 constructor-season records | 1950–2026*
