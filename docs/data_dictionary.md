# Data Dictionary — F1 Race Strategy Intelligence

## master_fact.csv

| Column Name | Dtype | Description | Example Value | Null Count |
| :--- | :--- | :--- | :--- | :--- |
| resultId | int64 | Unique internal identifier for each race entry | 1 | 0 |
| raceId | int64 | Foreign key identifying the specific race event | 18 | 0 |
| driverId | int64 | Unique identifier for the driver | 1 | 0 |
| constructorId | int64 | Unique identifier for the car manufacturer | 1 | 0 |
| number | float64 | TBD | 22.0 | 6 |
| grid | int64 | Starting position on the race grid (1=Pole, 0=Pit Lane) | 1 | 0 |
| position | float64 | TBD | 1.0 | 10953 |
| positionText | str | TBD | 1 | 0 |
| positionOrder | int64 | Final finishing classification order (1-max) | 1 | 0 |
| points | float64 | Championship points awarded for the race | 10.0 | 0 |
| laps | int64 | TBD | 58 | 0 |
| time | str | TBD | 1:34:50.616 | 19252 |
| milliseconds | float64 | TBD | 5690616.0 | 19252 |
| fastestLap | float64 | TBD | 39.0 | 18535 |
| rank | float64 | TBD | 2.0 | 18277 |
| fastestLapTime | str | TBD | 1:27.452 | 18535 |
| fastestLapSpeed | float64 | TBD | 218.3 | 19052 |
| statusId | int64 | TBD | 1 | 0 |
| is_finisher | int64 | Binary flag: 1 if driver completed race distance, 0 otherwise | 1 | 0 |
| is_dnf | int64 | Binary flag: 1 if driver did not finish, 0 otherwise | 0 | 0 |
| is_pitlane_start | int64 | TBD | 0 | 0 |
| is_podium | int64 | TBD | 1 | 0 |
| is_win | int64 | Binary flag: 1 if driver finished 1st, 0 otherwise | 1 | 0 |
| is_pole | int64 | Binary flag: 1 if driver started from pole position, 0 otherwise | 1 | 0 |
| year | int64 | Calendar year of the race season | 2008 | 0 |
| round | int64 | TBD | 1 | 0 |
| circuitId | int64 | TBD | 1 | 0 |
| race_name | str | TBD | Australian Grand Prix | 0 |
| circuit_name | str | Official name of the race track | Albert Park Grand Prix Circuit | 0 |
| location | str | TBD | Melbourne | 0 |
| country | str | TBD | Australia | 0 |
| lat | float64 | TBD | -37.8497 | 0 |
| lng | float64 | TBD | 144.968 | 0 |
| constructor_name | str | Commercial name of the F1 team | McLaren | 0 |
| constructor_nationality | str | TBD | British | 0 |
| forename | str | TBD | Lewis | 0 |
| surname | str | TBD | Hamilton | 0 |
| driver_nationality | str | TBD | British | 0 |
| stop_count | float64 | TBD | 2.0 | 15997 |
| avg_pit_ms | float64 | Average time spent in pit stops (milliseconds) | 24525.5 | 15999 |
| total_pit_ms | float64 | TBD | 49051.0 | 15997 |
| fastest_pit_ms | float64 | TBD | 24254.0 | 15999 |
| best_q_ms | float64 | TBD | 86714.0 | 16430 |
| qualifying_gap_ms | float64 | Time gap between driver's best qualifying lap and pole time | 0.0 | 16430 |
| q1_ms | float64 | TBD | 86572.0 | 16432 |
| q2_ms | float64 | TBD | 85187.0 | 21056 |
| q3_ms | float64 | TBD | 86714.0 | 23411 |
| fastest_lap_ms | float64 | TBD | nan | 20537 |
| lap_count | float64 | TBD | nan | 20537 |
| lap_time_std | float64 | TBD | nan | 20599 |
| status | str | TBD | Finished | 0 |
| dnf_category | str | Classification of DNF reason (Mechanical, Accident, etc.) | Finished | 0 |
| grid_to_finish_delta | float64 | Net positions gained (Grid - PositionOrder) | 0.0 | 11882 |
| driver_name | str | TBD | Lewis Hamilton | 0 |
| era | str | TBD | V10/V8 | 0 |
| driver_name_display | str | Formatted driver name for labels (Surname, Forename) | Hamilton, Lewis | 0 |
| constructor_short | str | Abbreviated constructor name for tight visualization layouts | MCL | 0 |