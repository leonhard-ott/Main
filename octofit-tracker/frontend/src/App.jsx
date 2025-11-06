import { useEffect, useState } from 'react'
import { getHealth } from './api'

export default function App() {
  const [health, setHealth] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    getHealth()
      .then((data) => setHealth(data))
      .catch((err) => setError(err.message))
  }, [])

  return (
    <div className="app-root">
      <header>
        <h1>OctoFit Tracker</h1>
        <p>Frontend scaffold running (Vite + React).</p>
      </header>

      <section>
        <h2>Backend status</h2>
        {error && <p style={{ color: 'crimson' }}>Error: {error}</p>}
        {health ? (
          <pre>{JSON.stringify(health, null, 2)}</pre>
        ) : (
          <p>Loading backend status…</p>
        )}
      </section>
    </div>
  )
}
