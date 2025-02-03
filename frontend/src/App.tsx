import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import './App.css'

function Home() {
  return <h2>Home Page</h2>
}

function Register() {
  return <h2>Register Page</h2>
}

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  )
}

export default App