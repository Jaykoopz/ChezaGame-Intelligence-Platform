# Database Design

## Phase 1

SQLite

---

# Users

| Field | Type |
|--------|------|
| id | INTEGER |
| username | TEXT |
| email | TEXT |
| password_hash | TEXT |
| subscription | TEXT |
| created_at | DATETIME |

---

# Bets

| Field | Type |
|--------|------|
| id | INTEGER |
| user_id | INTEGER |
| date | DATE |
| bookmaker | TEXT |
| league | TEXT |
| home_team | TEXT |
| away_team | TEXT |
| market | TEXT |
| stake | REAL |
| odds | REAL |
| result | TEXT |
| returns | REAL |
| profit | REAL |

---

# Selections

| Field | Type |
|--------|------|
| id | INTEGER |
| bet_id | INTEGER |
| selection | TEXT |
| odds | REAL |

---

# AI Insights

| Field | Type |
|--------|------|
| id | INTEGER |
| user_id | INTEGER |
| generated_at | DATETIME |
| recommendation | TEXT |
| confidence | REAL |

---

# Reports

| Field | Type |
|--------|------|
| id | INTEGER |
| user_id | INTEGER |
| report_type | TEXT |
| created_at | DATETIME |
| file_path | TEXT |

---

# Relationships

Users
  ↓
Bets
  ↓
Selections

Users
  ↓
Reports

Users
  ↓
AI Insights