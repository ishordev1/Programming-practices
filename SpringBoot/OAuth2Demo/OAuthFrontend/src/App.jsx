import { useState } from 'react'
import './App.css'
import Home from "./component/Home"
import Dashboard from "./component/Dashboard"
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

function App() {
  const [count, setCount] = useState(0)

  return (
   <>
   {/* <h1>this is app page</h1>
   <Home/> */}

<Router>
  <Routes>
    <Route path="/" element={<Home/>}/>
    <Route path="/dashboard" element={<Dashboard/>}/>
  </Routes>
</Router>
   </>
  )
}

export default App
