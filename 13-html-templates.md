# HTML Wrapper Templates - Ready to Use

## 1. React App Wrapper

```html name=react-wrapper.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>React App Wrapper</title>
    
    <!-- React CDN (for quick prototyping) -->
    <script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min. js"></script>
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background:  #f5f5f5;
        }

        #root {
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        . header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px 20px;
            text-align:  center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background: #5568d3;
        }
    </style>
</head>
<body>
    <!-- React mounts here -->
    <div id="root"></div>

    <!-- Your React Code -->
    <script type="text/babel">
        const { useState, useEffect } = React;

        // MAIN APP COMPONENT
        function App() {
            const [count, setCount] = useState(0);
            const [data, setData] = useState([]);

            useEffect(() => {
                // Fetch data on mount
                fetchData();
            }, []);

            const fetchData = async () => {
                // Example API call
                try {
                    const response = await fetch('https://jsonplaceholder.typicode.com/posts? _limit=5');
                    const json = await response.json();
                    setData(json);
                } catch (error) {
                    console.error('Error:', error);
                }
            };

            return (
                <div>
                    <div className="header">
                        <h1>My React App</h1>
                        <p>Learning by doing! </p>
                    </div>

                    <div className="container">
                        <div className="card">
                            <h2>Counter Example</h2>
                            <p>Count: {count}</p>
                            <button onClick={() => setCount(count + 1)}>
                                Increment
                            </button>
                            <button onClick={() => setCount(0)} style={{marginLeft: '10px'}}>
                                Reset
                            </button>
                        </div>

                        <div className="card">
                            <h2>API Data</h2>
                            {data.length === 0 ? (
                                <p>Loading...</p>
                            ) : (
                                <ul>
                                    {data.map(item => (
                                        <li key={item.id}>
                                            <strong>{item.title}</strong>
                                            <p>{item. body. substring(0, 100)}...</p>
                                        </li>
                                    ))}
                                </ul>
                            )}
                        </div>
                    </div>
                </div>
            );
        }

        // RENDER APP
        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>
```

## 2. Firebase Integration Template

```html name=firebase-template.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Firebase App</title>
    
    <!-- Firebase SDK -->
    <script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-auth-compat. js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore-compat.js"></script>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f0f0f0;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }

        input, button {
            padding: 10px;
            margin: 5px 0;
            width: 100%;
            font-size: 16px;
        }

        button {
            background: #4285f4;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background: #357ae8;
        }

        .hidden {
            display: none;
        }

        #dataList {
            margin-top:  20px;
        }

        .item {
            background: #f9f9f9;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            border-left: 4px solid #4285f4;
        }
    </style>
</head>
<body>
    <h1>🔥 Firebase App</h1>

    <!-- AUTH SECTION -->
    <div id="authSection" class="card">
        <h2>Authentication</h2>
        <div id="loginForm">
            <input type="email" id="email" placeholder="Email">
            <input type="password" id="password" placeholder="Password">
            <button onclick="login()">Login</button>
            <button onclick="signup()">Sign Up</button>
        </div>
        <div id="userInfo" class="hidden">
            <p>Logged in as: <span id="userEmail"></span></p>
            <button onclick="logout()">Logout</button>
        </div>
    </div>

    <!-- DATA SECTION -->
    <div id="dataSection" class="card hidden">
        <h2>Firestore Data</h2>
        <input type="text" id="itemName" placeholder="Item name">
        <button onclick="addItem()">Add Item</button>
        <div id="dataList"></div>
    </div>

    <script>
        // FIREBASE CONFIG
        // Replace with your config from Firebase Console
        const firebaseConfig = {
            apiKey: "YOUR_API_KEY",
            authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
            projectId: "YOUR_PROJECT_ID",
            storageBucket:  "YOUR_PROJECT_ID.appspot.com",
            messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
            appId: "YOUR_APP_ID"
        };

        // Initialize Firebase
        firebase.initializeApp(firebaseConfig);
        const auth = firebase.auth();
        const db = firebase.firestore();

        // AUTH STATE LISTENER
        auth.onAuthStateChanged(user => {
            if (user) {
                // User is logged in
                document. getElementById('loginForm').classList.add('hidden');
                document.getElementById('userInfo').classList.remove('hidden');
                document.getElementById('dataSection').classList.remove('hidden');
                document.getElementById('userEmail').textContent = user.email;
                loadData();
            } else {
                // User is logged out
                document.getElementById('loginForm').classList.remove('hidden');
                document.getElementById('userInfo').classList.add('hidden');
                document. getElementById('dataSection').classList.add('hidden');
            }
        });

        // AUTHENTICATION FUNCTIONS
        async function signup() {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            try {
                await auth.createUserWithEmailAndPassword(email, password);
                alert('Account created! ');
            } catch (error) {
                alert('Error: ' + error.message);
            }
        }

        async function login() {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            try {
                await auth.signInWithEmailAndPassword(email, password);
            } catch (error) {
                alert('Error: ' + error. message);
            }
        }

        function logout() {
            auth.signOut();
        }

        // FIRESTORE FUNCTIONS
        async function addItem() {
            const name = document.getElementById('itemName').value;
            if (!name) return;

            try {
                await db.collection('items').add({
                    name: name,
                    createdBy: auth.currentUser.uid,
                    createdAt:  firebase.firestore.FieldValue.serverTimestamp()
                });
                document.getElementById('itemName').value = '';
                loadData();
            } catch (error) {
                alert('Error:  ' + error.message);
            }
        }

        function loadData() {
            db.collection('items')
                .where('createdBy', '==', auth.currentUser.uid)
                .orderBy('createdAt', 'desc')
                .onSnapshot(snapshot => {
                    const list = document.getElementById('dataList');
                    list.innerHTML = '';

                    snapshot.forEach(doc => {
                        const item = doc.data();
                        const div = document.createElement('div');
                        div.className = 'item';
                        div.innerHTML = `
                            <strong>${item.name}</strong>
                            <button onclick="deleteItem('${doc.id}')" style="width: auto; float: right;">Delete</button>
                        `;
                        list.appendChild(div);
                    });
                });
        }

        async function deleteItem(id) {
            try {
                await db.collection('items').doc(id).delete();
            } catch (error) {
                alert('Error: ' + error. message);
            }
        }
    </script>
</body>
</html>
```

## 3. TypeScript + React Template

```html name=typescript-react-template. html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TypeScript React App</title>
    
    <!-- React & TypeScript -->
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min. js"></script>
    <script src="https://unpkg.com/typescript@latest/lib/typescript.js"></script>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background: #282c34;
            color: white;
        }

        .app {
            max-width: 800px;
            margin: 50px auto;
            padding:  20px;
        }

        .card {
            background: #3a3f47;
            padding: 20px;
            border-radius:  10px;
            margin:  20px 0;
        }

        input {
            padding: 10px;
            width: 100%;
            margin:  10px 0;
            border-radius: 5px;
            border: none;
            font-size: 16px;
        }

        button {
            padding: 10px 20px;
            background: #61dafb;
            color: #282c34;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }

        button:hover {
            background: #4fa8c5;
        }

        .user-card {
            background: #4a5058;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div id="root"></div>

    <script type="text/babel" data-type="module">
        const { useState } = React;

        // TYPESCRIPT INTERFACES (simulated with JSDoc for browser)
        /**
         * @typedef {Object} User
         * @property {number} id
         * @property {string} name
         * @property {string} email
         */

        /**
         * @typedef {Object} FormData
         * @property {string} name
         * @property {string} email
         */

        // MAIN APP
        function App() {
            const [users, setUsers] = useState([]);
            const [formData, setFormData] = useState({ name: '', email: '' });

            const handleInputChange = (e) => {
                const { name, value } = e.target;
                setFormData(prev => ({
                    ...prev,
                    [name]: value
                }));
            };

            const handleSubmit = (e) => {
                e.preventDefault();
                
                if (! formData.name || !formData.email) {
                    alert('Please fill all fields');
                    return;
                }

                const newUser = {
                    id: Date.now(),
                    name: formData.name,
                    email: formData.email
                };

                setUsers(prev => [...prev, newUser]);
                setFormData({ name: '', email: '' });
            };

            const deleteUser = (id) => {
                setUsers(prev => prev.filter(user => user.id !== id));
            };

            return (
                <div className="app">
                    <h1>⚛️ TypeScript + React</h1>
                    
                    <div className="card">
                        <h2>Add User</h2>
                        <form onSubmit={handleSubmit}>
                            <input
                                type="text"
                                name="name"
                                placeholder="Name"
                                value={formData.name}
                                onChange={handleInputChange}
                            />
                            <input
                                type="email"
                                name="email"
                                placeholder="Email"
                                value={formData.email}
                                onChange={handleInputChange}
                            />
                            <button type="submit">Add User</button>
                        </form>
                    </div>

                    <div className="card">
                        <h2>Users ({users.length})</h2>
                        {users.length === 0 ? (
                            <p>No users yet.  Add one above!</p>
                        ) : (
                            users.map(user => (
                                <UserCard 
                                    key={user. id}
                                    user={user}
                                    onDelete={deleteUser}
                                />
                            ))
                        )}
                    </div>
                </div>
            );
        }

        // USER CARD COMPONENT
        function UserCard({ user, onDelete }) {
            return (
                <div className="user-card">
                    <h3>{user.name}</h3>
                    <p>{user.email}</p>
                    <button onClick={() => onDelete(user.id)}>Delete</button>
                </div>
            );
        }

        // RENDER
        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<App />);
    </script>
</body>
</html>
```

## 4. Google Colab HTML Wrapper

```html name=colab-wrapper.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colab Output Viewer</title>
    <style>
        body {
            font-family: 'Roboto', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f8f9fa;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            background: linear-gradient(135deg, #f59842 0%, #f7b731 100%);
            color:  white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom:  20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .notebook-cell {
            background: white;
            padding: 20px;
            margin: 15px 0;
            border-radius: 8px;
            border-left: 4px solid #f59842;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        .code-block {
            background: #f5f5f5;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 14px;
        }

        .output {
            background: #e8f5e9;
            padding: 15px;
            margin-top: 10px;
            border-radius:  5px;
            border-left: 3px solid #4caf50;
        }

        .chart-container {
            margin: 20px 0;
            padding: 20px;
            background: white;
            border-radius: 8px;
        }

        button {
            background: #f59842;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background: #e8883a;
        }
    </style>
    
    <!-- Chart.js for visualizations -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Colab Notebook Output</h1>
            <p>Interactive Python Results</p>
        </div>

        <!-- Cell 1: Code Example -->
        <div class="notebook-cell">
            <h3>Cell [1]:  Data Processing</h3>
            <div class="code-block">
import pandas as pd<br>
import numpy as np<br>
<br>
# Sample data<br>
data = pd.DataFrame({<br>
&nbsp;&nbsp;'name': ['Alice', 'Bob', 'Charlie'],<br>
&nbsp;&nbsp;'age': [25, 30, 35],<br>
&nbsp;&nbsp;'score': [85, 92, 78]<br>
})<br>
<br>
print(data)
            </div>
            <div class="output">
                <pre>
     name  age  score
0   Alice   25     85
1     Bob   30     92
2 Charlie   35     78
                </pre>
            </div>
        </div>

        <!-- Cell 2: Visualization -->
        <div class="notebook-cell">
            <h3>Cell [2]: Data Visualization</h3>
            <div class="chart-container">
                <canvas id="myChart"></canvas>
            </div>
            <button onclick="updateChart()">Refresh Chart</button>
        </div>

        <!-- Cell 3: Interactive Input -->
        <div class="notebook-cell">
            <h3>Cell [3]: Interactive Calculation</h3>
            <input type="number" id="inputValue" placeholder="Enter a number" style="padding: 10px; width: 200px;">
            <button onclick="calculate()">Calculate Square</button>
            <div id="result" class="output" style="margin-top: 10px; display: none;"></div>
        </div>
    </div>

    <script>
        // Initialize Chart
        const ctx = document.getElementById('myChart').getContext('2d');
        let myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Alice', 'Bob', 'Charlie'],
                datasets: [{
                    label: 'Scores',
                    data: [85, 92, 78],
                    backgroundColor: [
                        'rgba(245, 152, 66, 0.7)',
                        'rgba(247, 183, 49, 0.7)',
                        'rgba(255, 195, 113, 0.7)'
                    ],
                    borderColor: [
                        'rgba(245, 152, 66, 1)',
                        'rgba(247, 183, 49, 1)',
                        'rgba(255, 195, 113, 1)'
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive:  true,
                scales: {
                    y: {
                        beginAtZero:  true
                    }
                }
            }
        });

        function updateChart() {
            // Generate random data
            myChart.data.datasets[0]. data = [
                Math.floor(Math.random() * 100),
                Math.floor(Math.random() * 100),
                Math.floor(Math.random() * 100)
            ];
            myChart.update();
        }

        function calculate() {
            const input = document.getElementById('inputValue').value;
            const result = document.getElementById('result');
            
            if (input) {
                const square = Math.pow(input, 2);
                result.innerHTML = `<strong>Result:</strong> ${input}² = ${square}`;
                result.style.display = 'block';
            } else {
                alert('Please enter a number');
            }
        }
    </script>
</body>
</html>
```

## Quick Start Guide

### Using These Templates:

1. **Copy the HTML** you need
2. **Save as . html** file
3. **Open in browser** to test
4. **Customize** the code sections
5. **Add your logic** in the script tags

### For React Template: 
- Everything is self-contained
- No build step needed
- Great for prototyping
- For production, use `create-react-app`

### For Firebase Template:
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create project
3. Get config object
4. Replace the `firebaseConfig` in template

### For TypeScript: 
- Types are simulated with JSDoc
- For real TypeScript, use build tools
- This template is for quick experiments

### For Colab:
- Save Python notebook output
- Display in nice HTML format
- Great for sharing results

---
**Notes Section**:
- CDN links = quick start, no install
- For production = use proper build tools
- 
```