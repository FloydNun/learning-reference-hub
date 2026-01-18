# React Project Template - Ready to Use

## Quick Start
```bash
# Create new React app
npx create-react-app my-app
cd my-app
npm start

# Or with TypeScript
npx create-react-app my-app --template typescript
```

## Basic React Wrapper Template

```jsx name=App.jsx
import React, { useState, useEffect } from 'react';
import './App.css';

/**
 * MAIN APP WRAPPER
 * This is your main component that wraps everything
 */
function App() {
  // STATE:  Data that can change
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // EFFECT: Runs when component loads
  useEffect(() => {
    fetchData();
  }, []); // Empty array = run once on load

  // FETCH DATA from API
  const fetchData = async () => {
    try {
      setLoading(true);
      const response = await fetch('https://api.example.com/data');
      const json = await response.json();
      setData(json);
    } catch (err) {
      setError(err. message);
    } finally {
      setLoading(false);
    }
  };

  // RENDER: What shows on screen
  return (
    <div className="App">
      <Header title="My React App" />
      
      <main className="main-content">
        {loading && <LoadingSpinner />}
        {error && <ErrorMessage message={error} />}
        {! loading && !error && <ContentArea data={data} />}
      </main>
      
      <Footer />
    </div>
  );
}

/**
 * HEADER COMPONENT
 * Reusable header with props
 */
function Header({ title }) {
  return (
    <header className="header">
      <h1>{title}</h1>
      <nav>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
      </nav>
    </header>
  );
}

/**
 * LOADING SPINNER
 * Shows while data is loading
 */
function LoadingSpinner() {
  return (
    <div className="loading">
      <div className="spinner"></div>
      <p>Loading...</p>
    </div>
  );
}

/**
 * ERROR MESSAGE
 * Shows if something goes wrong
 */
function ErrorMessage({ message }) {
  return (
    <div className="error">
      <h2>⚠️ Oops! </h2>
      <p>{message}</p>
      <button onClick={() => window.location.reload()}>
        Try Again
      </button>
    </div>
  );
}

/**
 * CONTENT AREA
 * Displays your main content
 */
function ContentArea({ data }) {
  return (
    <div className="content">
      <h2>My Content</h2>
      {data.length === 0 ? (
        <p>No data yet. </p>
      ) : (
        <div className="data-grid">
          {data.map((item, index) => (
            <Card key={index} item={item} />
          ))}
        </div>
      )}
    </div>
  );
}

/**
 * CARD COMPONENT
 * Individual item display
 */
function Card({ item }) {
  const [liked, setLiked] = useState(false);

  return (
    <div className="card">
      <h3>{item.title}</h3>
      <p>{item.description}</p>
      <button 
        onClick={() => setLiked(!liked)}
        className={liked ? 'liked' : ''}
      >
        {liked ? '❤️' : '🤍'} Like
      </button>
    </div>
  );
}

/**
 * FOOTER COMPONENT
 */
function Footer() {
  return (
    <footer className="footer">
      <p>&copy; 2026 My React App. Built while learning! </p>
    </footer>
  );
}

export default App;
```

```css name=App.css
/* GLOBAL STYLES */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
  line-height: 1.6;
  color: #333;
}

. App {
  min-height:  100vh;
  display:  flex;
  flex-direction:  column;
}

/* HEADER */
.header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.header h1 {
  margin-bottom: 15px;
}

.header nav a {
  color: white;
  text-decoration: none;
  margin-right: 20px;
  padding: 8px 15px;
  border-radius: 5px;
  transition: background 0.3s;
}

.header nav a:hover {
  background:  rgba(255,255,255,0.2);
}

/* MAIN CONTENT */
.main-content {
  flex: 1;
  padding: 40px 20px;
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
}

/* LOADING SPINNER */
.loading {
  text-align: center;
  padding: 50px;
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top:  4px solid #667eea;
  border-radius: 50%;
  width:  50px;
  height: 50px;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* ERROR MESSAGE */
.error {
  background: #fee;
  border: 2px solid #fcc;
  border-radius: 10px;
  padding: 30px;
  text-align: center;
  max-width: 500px;
  margin: 50px auto;
}

.error button {
  margin-top: 20px;
  padding: 10px 30px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.error button:hover {
  background: #5568d3;
}

/* CONTENT AREA */
.content h2 {
  margin-bottom: 30px;
  color: #667eea;
}

.data-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

/* CARD */
.card {
  background: white;
  border-radius:  10px;
  padding:  20px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0,0,0,0.15);
}

.card h3 {
  color: #667eea;
  margin-bottom: 10px;
}

.card p {
  color: #666;
  margin-bottom: 15px;
}

.card button {
  padding: 8px 20px;
  border: 2px solid #667eea;
  background: white;
  color: #667eea;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.3s;
}

.card button:hover {
  background: #667eea;
  color: white;
}

. card button.liked {
  background: #667eea;
  color: white;
}

/* FOOTER */
.footer {
  background: #333;
  color: white;
  text-align: center;
  padding: 20px;
  margin-top: auto;
}

/* RESPONSIVE */
@media (max-width:  768px) {
  .data-grid {
    grid-template-columns: 1fr;
  }
  
  .header nav a {
    display: block;
    margin: 5px 0;
  }
}
```

## React Hooks Cheat Sheet

```jsx
// USESTATE - Store data that can change
const [count, setCount] = useState(0);
const [name, setName] = useState('Floyd');
const [items, setItems] = useState([]);

// USEEFFECT - Run code when component loads or updates
useEffect(() => {
  // Runs on mount
  console.log('Component loaded');
  
  // Cleanup function
  return () => {
    console.log('Component unmounting');
  };
}, []); // Empty array = run once

useEffect(() => {
  // Runs when 'count' changes
  console. log('Count changed:', count);
}, [count]); // Dependency array

// USEREF - Reference DOM elements
const inputRef = useRef(null);
const focusInput = () => inputRef.current.focus();

// USECONTEXT - Share data without props
const ThemeContext = React.createContext();
const theme = useContext(ThemeContext);

// USEMEMO - Optimize expensive calculations
const expensiveValue = useMemo(() => {
  return computeExpensiveValue(a, b);
}, [a, b]);

// USECALLBACK - Optimize function references
const handleClick = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

## Common Patterns

```jsx
// CONDITIONAL RENDERING
{isLoggedIn ?  <Dashboard /> : <Login />}
{error && <ErrorMessage />}
{loading && <Spinner />}

// LISTS
{items.map(item => (
  <div key={item.id}>{item.name}</div>
))}

// FORMS
function MyForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target. name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="name"
        value={formData.name}
        onChange={handleChange}
        placeholder="Name"
      />
      <input
        name="email"
        value={formData.email}
        onChange={handleChange}
        placeholder="Email"
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```

---
**Notes Section**:
- useState = data that changes
- useEffect = run code on load/update
- Props = pass data to components
- map() = display lists
- 
```