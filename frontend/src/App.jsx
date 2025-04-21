import React from 'react'
import { Routes, Route, Link } from 'react-router-dom'

function Dashboard() {
  return <h2>📊 Dashboard Page</h2>
}
function Projects() {
  return <h2>📁 Projects Page</h2>
}
function ToolConfigurator() {
  return <h2>🛠 Tool Configurator Page</h2>
}
function AgentManager() {
  return <h2>🤖 Agent Manager Page</h2>
}
function Logs() {
  return <h2>📜 Logs Page</h2>
}
function Feedback() {
  return <h2>🧾 Feedback Viewer Page</h2>
}

export default function App() {
  return (
    <div style={{ padding: 20 }}>
      <h1>🧠 TitanAI Studio</h1>
      <nav style={{ marginBottom: 20 }}>
        <Link to='/' style={{ marginRight: 10 }}>Dashboard</Link>
        <Link to='/projects' style={{ marginRight: 10 }}>Projects</Link>
        <Link to='/tools' style={{ marginRight: 10 }}>Tools</Link>
        <Link to='/agent-manager' style={{ marginRight: 10 }}>Agents</Link>
        <Link to='/logs' style={{ marginRight: 10 }}>Logs</Link>
        <Link to='/feedback'>Feedback</Link>
      </nav>
      <Routes>
        <Route path='/' element={<Dashboard />} />
        <Route path='/projects' element={<Projects />} />
        <Route path='/tools' element={<ToolConfigurator />} />
        <Route path='/agent-manager' element={<AgentManager />} />
        <Route path='/logs' element={<Logs />} />
        <Route path='/feedback' element={<Feedback />} />
      </Routes>
    </div>
  )
}
