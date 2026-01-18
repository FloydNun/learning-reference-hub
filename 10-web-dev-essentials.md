# Web Development Essentials - JS, TS, CSS

## JavaScript Basics

### Variables & Data Types
```javascript
// Modern variable declaration
let name = "Floyd";              // Can be reassigned
const age = 30;                  // Cannot be reassigned
var oldWay = "avoid";            // Old style, avoid

// Data types
let string = "Hello";
let number = 42;
let float = 3.14;
let boolean = true;
let nothing = null;
let undefined_var;
let array = [1, 2, 3, "four"];
let object = { name: "Floyd", age: 30 };

// Template literals (string interpolation)
let greeting = `Hello, ${name}!  You are ${age} years old. `;
console.log(greeting);
```

### Functions
```javascript
// Function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

// Arrow function (modern)
const greet = (name) => `Hello, ${name}!`;

// Arrow function with multiple lines
const calculate = (a, b) => {
    const sum = a + b;
    return sum * 2;
};

// Default parameters
const greet = (name = "World") => `Hello, ${name}!`;

// Destructuring
const person = { name: "Floyd", age: 30 };
const { name, age } = person;

// Array destructuring
const [first, second, ... rest] = [1, 2, 3, 4, 5];
```

### Arrays
```javascript
const fruits = ["apple", "banana", "cherry"];

// Add/remove
fruits.push("date");             // Add to end
fruits.pop();                    // Remove from end
fruits.unshift("apricot");       // Add to start
fruits.shift();                  // Remove from start

// Iterate
fruits.forEach(fruit => console.log(fruit));

// Map (transform each element)
const upper = fruits.map(f => f.toUpperCase());

// Filter
const longNames = fruits.filter(f => f.length > 5);

// Find
const found = fruits.find(f => f. startsWith("b"));

// Reduce
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((total, num) => total + num, 0);

// Spread operator
const moreFruits = [... fruits, "elderberry"];
```

### Objects
```javascript
const person = {
    name: "Floyd",
    age: 30,
    greet() {
        return `Hi, I'm ${this.name}`;
    }
};

// Access properties
console.log(person. name);
console.log(person["age"]);

// Add property
person.location = "USA";

// Delete property
delete person.age;

// Object spread
const updatedPerson = { ... person, age: 31 };

// Object destructuring
const { name, age } = person;

// Object. keys, values, entries
Object.keys(person);             // ["name", "age"]
Object.values(person);           // ["Floyd", 30]
Object.entries(person);          // [["name", "Floyd"], ["age", 30]]
```

### Async/Await (Modern)
```javascript
// Fetch data from API
async function getUser(id) {
    try {
        const response = await fetch(`https://api.example.com/users/${id}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error:", error);
    }
}

// Using the function
const user = await getUser(1);

// Multiple await
async function getData() {
    const users = await fetch("/api/users").then(r => r.json());
    const posts = await fetch("/api/posts").then(r => r.json());
    return { users, posts };
}

// Promise. all (parallel)
const [users, posts] = await Promise.all([
    fetch("/api/users").then(r => r.json()),
    fetch("/api/posts").then(r => r.json())
]);
```

### DOM Manipulation
```javascript
// Select elements
const element = document.getElementById("myId");
const elements = document.getElementsByClassName("myClass");
const element = document.querySelector(".myClass");
const elements = document.querySelectorAll("div.item");

// Modify content
element.textContent = "New text";
element.innerHTML = "<strong>Bold text</strong>";

// Modify attributes
element.setAttribute("data-id", "123");
element.id = "newId";
element.classList.add("active");
element.classList.remove("inactive");
element.classList.toggle("visible");

// Modify styles
element.style.color = "red";
element.style.backgroundColor = "blue";

// Create elements
const newDiv = document.createElement("div");
newDiv.textContent = "Hello";
document.body.appendChild(newDiv);

// Event listeners
element.addEventListener("click", () => {
    console.log("Clicked!");
});

element.addEventListener("click", (event) => {
    event.preventDefault();    // Stop default behavior
    console.log(event.target); // Element that was clicked
});
```

## TypeScript Essentials

### Basic Types
```typescript
// Type annotations
let name: string = "Floyd";
let age: number = 30;
let isActive: boolean = true;
let items: string[] = ["a", "b", "c"];
let numbers: Array<number> = [1, 2, 3];

// Union types
let id: string | number = "abc123";
id = 123;  // Also valid

// Type aliases
type ID = string | number;
let userId: ID = "user_123";

// Interfaces
interface User {
    id: number;
    name: string;
    email?:  string;        // Optional property
    readonly created: Date; // Read-only
}

const user: User = {
    id: 1,
    name:  "Floyd",
    created: new Date()
};

// Functions with types
function greet(name: string): string {
    return `Hello, ${name}!`;
}

// Arrow function with types
const add = (a: number, b:  number): number => a + b;

// Optional parameters
function log(message: string, userId?: number): void {
    console.log(message, userId);
}

// Default parameters
function greet(name:  string = "World"): string {
    return `Hello, ${name}!`;
}
```

### Advanced Types
```typescript
// Generic types
function identity<T>(arg: T): T {
    return arg;
}

const result = identity<string>("hello");

// Generic interface
interface Response<T> {
    data:  T;
    status: number;
}

const response: Response<User> = {
    data: { id: 1, name: "Floyd", created: new Date() },
    status: 200
};

// Type guards
function isString(value: any): value is string {
    return typeof value === "string";
}

// Enums
enum Status {
    Active,
    Inactive,
    Pending
}

let userStatus: Status = Status.Active;

// String enums
enum Direction {
    Up = "UP",
    Down = "DOWN",
    Left = "LEFT",
    Right = "RIGHT"
}
```

### TypeScript with Classes
```typescript
class Person {
    private id: number;
    protected name: string;
    public age: number;

    constructor(id: number, name: string, age: number) {
        this.id = id;
        this. name = name;
        this. age = age;
    }

    greet(): string {
        return `Hi, I'm ${this.name}`;
    }
}

// Shorthand constructor
class User {
    constructor(
        private id: number,
        public name: string,
        protected email:  string
    ) {}
}

// Inheritance
class Admin extends User {
    constructor(id: number, name: string, email: string, public role: string) {
        super(id, name, email);
    }
}
```

## CSS Essentials

### Selectors
```css
/* Element selector */
p {
    color: blue;
}

/* Class selector */
.my-class {
    font-size: 16px;
}

/* ID selector */
#my-id {
    background-color: yellow;
}

/* Descendant selector */
div p {
    margin: 10px;
}

/* Child selector */
div > p {
    padding: 5px;
}

/* Adjacent sibling */
h1 + p {
    font-weight: bold;
}

/* Attribute selector */
input[type="text"] {
    border: 1px solid gray;
}

/* Pseudo-classes */
a:hover {
    color: red;
}

button:active {
    transform: scale(0.95);
}

li:first-child {
    font-weight: bold;
}

li:nth-child(odd) {
    background-color:  #f0f0f0;
}

/* Pseudo-elements */
p::first-line {
    font-weight: bold;
}

p::before {
    content: "→ ";
}
```

### Flexbox
```css
.container {
    display: flex;
    
    /* Direction */
    flex-direction: row;           /* row, column, row-reverse, column-reverse */
    
    /* Wrap */
    flex-wrap: wrap;               /* wrap, nowrap, wrap-reverse */
    
    /* Justify (main axis) */
    justify-content: center;       /* flex-start, flex-end, center, space-between, space-around */
    
    /* Align (cross axis) */
    align-items: center;           /* flex-start, flex-end, center, stretch, baseline */
    
    /* Gap */
    gap: 20px;
}

.item {
    flex: 1;                       /* Grow to fill space */
    flex-shrink: 0;                /* Don't shrink */
    flex-basis: 200px;             /* Base size */
}
```

### Grid
```css
.grid-container {
    display: grid;
    
    /* Columns and rows */
    grid-template-columns: 1fr 2fr 1fr;
    grid-template-columns: repeat(3, 1fr);
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    
    grid-template-rows: 100px auto 50px;
    
    /* Gap */
    gap: 20px;
    row-gap: 10px;
    column-gap:  15px;
    
    /* Areas */
    grid-template-areas: 
        "header header header"
        "sidebar content content"
        "footer footer footer";
}

.header {
    grid-area: header;
}

.item {
    grid-column: 1 / 3;           /* Span columns 1-3 */
    grid-row: 2 / 4;              /* Span rows 2-4 */
}
```

### Modern CSS Features
```css
/* CSS Variables */
:root {
    --primary-color: #3498db;
    --spacing: 20px;
}

. button {
    background-color: var(--primary-color);
    padding: var(--spacing);
}

/* Media queries */
@media (max-width: 768px) {
    .container {
        flex-direction: column;
    }
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
    body {
        background-color: #1a1a1a;
        color: #ffffff;
    }
}

/* Animations */
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

. element {
    animation: fadeIn 0.3s ease-in;
}

/* Transitions */
.button {
    transition: all 0.3s ease;
}

. button:hover {
    transform:  scale(1.1);
    background-color: #2980b9;
}
```

## Quick Reference

### JavaScript
| Concept | Example |
|---------|---------|
| Arrow function | `const fn = (x) => x * 2` |
| Template literal | `` `Hello ${name}` `` |
| Destructuring | `const {name, age} = person` |
| Spread operator | `[...array, newItem]` |
| Async/await | `const data = await fetch(url)` |

### TypeScript
| Concept | Example |
|---------|---------|
| Type annotation | `let name: string = "Floyd"` |
| Interface | `interface User { name: string }` |
| Union type | `let id: string \| number` |
| Generic | `function fn<T>(arg: T): T` |

### CSS
| Concept | Example |
|---------|---------|
| Flexbox | `display: flex; justify-content: center` |
| Grid | `display: grid; grid-template-columns:  1fr 1fr` |
| Variable | `var(--primary-color)` |
| Media query | `@media (max-width: 768px) { }` |

---
**Notes Section**:
- 
- 
```