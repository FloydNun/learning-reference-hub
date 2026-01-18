# Data Formats - What, Why, How

## Overview

Different formats for storing and sharing data.  Each has strengths and use cases.

| Format | Best For | Human Readable?  | Size |
|--------|----------|----------------|------|
| JSON | APIs, configs, web apps | ✅ Yes | Medium |
| YAML | Configs, Docker, K8s | ✅ Yes | Medium |
| XML | Legacy systems, enterprise | ✅ Yes | Large |
| CSV | Spreadsheets, simple data | ✅ Yes | Small |
| SQLite (. db) | Local databases, apps | ❌ No (binary) | Variable |
| Binary | Performance-critical | ❌ No | Smallest |

---

## 1. JSON (JavaScript Object Notation)

### What It Is
```json
{
  "name":  "Floyd",
  "age": 30,
  "skills": ["JavaScript", "Python", "Git"],
  "active": true,
  "address":  {
    "city": "Somewhere",
    "state": "CA"
  }
}
```

### Why Use It
- **Universal**: Every language can read/write JSON
- **Web-friendly**: Native to JavaScript
- **APIs**: 95% of modern APIs use JSON
- **Simple**: Easy to read and write

### Common Uses
```
✅ API responses
✅ Configuration files (package.json, tsconfig.json)
✅ Saving app state
✅ Data exchange between systems
✅ NoSQL databases (MongoDB)
```

### Working with JSON

#### JavaScript
```javascript
// Parse JSON string to object
const jsonString = '{"name":"Floyd","age":30}';
const obj = JSON.parse(jsonString);
console.log(obj.name); // "Floyd"

// Convert object to JSON string
const person = { name: "Floyd", age: 30 };
const json = JSON.stringify(person);
console.log(json); // '{"name":"Floyd","age":30}'

// Pretty print (indented)
const prettyJson = JSON.stringify(person, null, 2);
```

#### Python
```python
import json

# Parse JSON string
json_string = '{"name":"Floyd","age":30}'
obj = json.loads(json_string)
print(obj['name'])  # "Floyd"

# Convert dict to JSON
person = {"name": "Floyd", "age":  30}
json_str = json.dumps(person)

# Pretty print
pretty = json.dumps(person, indent=2)

# Read from file
with open('data. json', 'r') as f:
    data = json.load(f)

# Write to file
with open('data. json', 'w') as f:
    json.dump(person, f, indent=2)
```

#### Command Line
```bash
# Pretty print JSON file
cat data.json | python -m json.tool

# Or with jq (better tool)
cat data.json | jq '.'

# Filter with jq
cat data.json | jq '.name'
```

---

## 2. YAML (YAML Ain't Markup Language)

### What It Is
```yaml
name: Floyd
age:  30
skills:
  - JavaScript
  - Python
  - Git
active: true
address: 
  city: Somewhere
  state: CA
```

### Why Use It
- **More readable**: Less punctuation than JSON
- **Comments allowed**: `# This is a comment`
- **Popular in DevOps**: Docker, Kubernetes, CI/CD

### Common Uses
```
✅ Docker Compose files
✅ Kubernetes configs
✅ GitHub Actions workflows
✅ Ansible playbooks
✅ Configuration files
```

### Working with YAML

#### Python
```python
import yaml

# Read YAML file
with open('config.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Write YAML file
data = {
    'name': 'Floyd',
    'age': 30,
    'skills': ['Python', 'Git']
}

with open('config.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
```

#### JavaScript
```javascript
// npm install js-yaml
const yaml = require('js-yaml');
const fs = require('fs');

// Read YAML
const data = yaml.load(fs.readFileSync('config.yaml', 'utf8'));

// Write YAML
const obj = { name: 'Floyd', age:  30 };
const yamlStr = yaml.dump(obj);
fs.writeFileSync('config. yaml', yamlStr);
```

### Example: Docker Compose
```yaml
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes: 
      - ./html:/usr/share/nginx/html
    environment:
      - NGINX_HOST=localhost
      - NGINX_PORT=80
```

---

## 3. XML (eXtensible Markup Language)

### What It Is
```xml
<?xml version="1.0" encoding="UTF-8"?>
<person>
  <name>Floyd</name>
  <age>30</age>
  <skills>
    <skill>JavaScript</skill>
    <skill>Python</skill>
    <skill>Git</skill>
  </skills>
  <active>true</active>
  <address>
    <city>Somewhere</city>
    <state>CA</state>
  </address>
</person>
```

### Why Use It
- **Established**: Been around since 1998
- **Schemas**: Can validate structure (XSD)
- **Enterprise**: Banking, healthcare, SOAP APIs
- **Attributes**: Can add metadata to tags

### Common Uses
```
✅ Legacy enterprise systems
✅ SOAP web services
✅ Android layouts
✅ Microsoft Office files (. docx, .xlsx)
✅ SVG graphics
✅ RSS feeds
```

### Working with XML

#### Python
```python
import xml.etree.ElementTree as ET

# Parse XML
tree = ET.parse('data.xml')
root = tree.getroot()

# Read data
for person in root.findall('person'):
    name = person.find('name').text
    age = person.find('age').text
    print(f"{name}, {age}")

# Create XML
root = ET.Element('person')
name = ET.SubElement(root, 'name')
name.text = 'Floyd'
age = ET.SubElement(root, 'age')
age.text = '30'

tree = ET.ElementTree(root)
tree.write('output.xml', encoding='utf-8', xml_declaration=True)
```

#### JavaScript (Browser)
```javascript
// Parse XML string
const parser = new DOMParser();
const xmlDoc = parser.parseFromString(xmlString, "text/xml");

// Read data
const name = xmlDoc.getElementsByTagName("name")[0].textContent;

// Create XML
const doc = document.implementation.createDocument("", "", null);
const person = doc.createElement("person");
const nameEl = doc.createElement("name");
nameEl.textContent = "Floyd";
person.appendChild(nameEl);
```

---

## 4. CSV (Comma-Separated Values)

### What It Is
```csv
name,age,city,active
Floyd,30,Somewhere,true
Alice,25,Elsewhere,true
Bob,35,Anywhere,false
```

### Why Use It
- **Simple**: Just commas and lines
- **Excel-friendly**: Opens in spreadsheets
- **Lightweight**:  Smallest text format
- **Universal**: Every tool supports it

### Common Uses
```
✅ Excel/Google Sheets data
✅ Data exports
✅ Simple databases
✅ Log files
✅ Data analysis (pandas)
```

### Working with CSV

#### Python
```python
import csv

# Read CSV
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])

# Write CSV
data = [
    {'name': 'Floyd', 'age': 30, 'city': 'Somewhere'},
    {'name': 'Alice', 'age': 25, 'city': 'Elsewhere'}
]

with open('output.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# With Pandas (better for large data)
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())

df.to_csv('output.csv', index=False)
```

#### JavaScript
```javascript
// Parse CSV (simple)
const csv = `name,age,city
Floyd,30,Somewhere
Alice,25,Elsewhere`;

const lines = csv.split('\n');
const headers = lines[0].split(',');
const data = lines.slice(1).map(line => {
    const values = line.split(',');
    return headers.reduce((obj, header, i) => {
        obj[header] = values[i];
        return obj;
    }, {});
});

console.log(data);

// Better:  use a library
// npm install papaparse
const Papa = require('papaparse');

Papa.parse(csv, {
    header: true,
    complete: (results) => {
        console.log(results.data);
    }
});
```

---

## 5. SQLite (. db files)

### What It Is
A complete SQL database in a single file.  Binary format, not human-readable.

```
mydata.db  (contains tables, indexes, everything)
```

### Why Use It
- **Full database**: SQL queries, indexes, transactions
- **No server**: Just a file
- **Fast**: C-based, very efficient
- **Portable**: Copy file = copy database

### Common Uses
```
✅ Mobile apps (Android, iOS)
✅ Desktop apps (Electron, etc.)
✅ Embedded systems
✅ Development/testing
✅ Small to medium web apps
✅ Browser storage (Web SQL - deprecated but still used)
```

### Working with SQLite

#### Python
```python
import sqlite3

# Connect (creates file if doesn't exist)
conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
''')

# Insert data
cursor.execute('INSERT INTO users (name, age, email) VALUES (?, ?, ?)',
               ('Floyd', 30, 'floyd@example.com'))

# Query data
cursor.execute('SELECT * FROM users WHERE age > ?', (25,))
rows = cursor.fetchall()
for row in rows:
    print(row)

# Commit and close
conn.commit()
conn.close()
```

#### Command Line
```bash
# Open database
sqlite3 mydata. db

# SQL commands
. tables              # List tables
.schema users        # Show table structure
SELECT * FROM users; # Query
. quit                # Exit

# Dump to SQL file
sqlite3 mydata. db . dump > backup.sql

# Restore from SQL
sqlite3 newdata.db < backup.sql
```

#### JavaScript (Node.js)
```javascript
// npm install better-sqlite3
const Database = require('better-sqlite3');

const db = new Database('mydata.db');

// Create table
db.exec(`
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
`);

// Insert
const insert = db.prepare('INSERT INTO users (name, age) VALUES (?, ?)');
insert.run('Floyd', 30);

// Query
const users = db.prepare('SELECT * FROM users').all();
console.log(users);

db.close();
```

---

## 6. Comparison: When to Use Each

### JSON vs YAML vs XML

```javascript
// Same data in different formats: 

// JSON - Best for APIs, web apps
{"name":"Floyd","age":30,"skills": ["Python","Git"]}

// YAML - Best for configs (more readable)
name: Floyd
age: 30
skills:
  - Python
  - Git

// XML - Best for enterprise/legacy
<person>
  <name>Floyd</name>
  <age>30</age>
  <skills>
    <skill>Python</skill>
    <skill>Git</skill>
  </skills>
</person>
```

### Decision Tree

```
Need a database?
  ├─ Yes → Use SQLite (. db)
  └─ No, just storing data
      │
      Need relationships/complex queries?
      ├─ Yes → Use SQLite
      └─ No, simple storage
          │
          For APIs/JavaScript? 
          ├─ Yes → Use JSON
          └─ No
              │
              Configuration file?
              ├─ Yes → Use YAML (easier to read)
              └─ No
                  │
                  Spreadsheet data?
                  ├─ Yes → Use CSV
                  └─ Legacy/Enterprise system?
                      ├─ Yes → Use XML
                      └─ No → Use JSON (most flexible)
```

### Size Comparison

Same data, different formats: 

```
JSON:   123 bytes
YAML:   98 bytes   (smallest text format)
XML:    186 bytes  (largest)
CSV:    85 bytes   (if tabular data)
SQLite: 8192 bytes (min file size, but efficient for lots of data)
```

---

## 🤔 Your Question: JSON in HTML - Why Same Size?

### The Answer: 

When you embed JSON in HTML, the file contains BOTH: 

```html
<!-- This HTML file contains:  -->

1. HTML structure (tags, styling, scripts)     ~10KB
2. JSON data embedded in <script> tag          ~5KB
3. JavaScript code to process the JSON         ~3KB
                                        Total: ~18KB

Even if JSON has "all the data", the HTML still needs:
- Display logic
- Styling
- User interface
- Event handlers
```

### Example: 

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        /* This CSS is NOT in the JSON */
        .card { padding: 20px; }
    </style>
</head>
<body>
    <!-- This HTML structure is NOT in the JSON -->
    <div id="app"></div>

    <script>
        // This is your JSON data
        const data = {
            "users": [
                {"name": "Floyd", "age":  30}
            ]
        };

        // This JavaScript code is NOT in the JSON
        // It's needed to display the data
        function displayData() {
            const app = document.getElementById('app');
            data.users.forEach(user => {
                app.innerHTML += `<div class="card">${user.name}</div>`;
            });
        }
        displayData();
    </script>
</body>
</html>
```

**File sizes:**
- `data.json` alone: 50 bytes
- `index.html` with embedded JSON: 500 bytes
- Why? HTML includes presentation + logic + data

### If JSON Has "Everything":

If your JSON truly contains all styling/logic: 

```json
{
  "html": "<div class='card'>Floyd</div>",
  "css": ". card { padding: 20px; }",
  "js": "console.log('hi');"
}
```

You still need HTML to: 
1. Load the JSON file
2. Parse it
3. Inject the HTML/CSS/JS
4. Execute it

**That loader code takes space! **

---

**Notes Section**:
- JSON = data interchange
- YAML = human-friendly configs
- XML = enterprise/legacy
- CSV = simple tables
- SQLite = when you need a database
- 
```