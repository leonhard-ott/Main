const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export async function getHealth() {
  const res = await fetch(`${API_BASE}/api/health/`, {
    credentials: 'include',
  })
  if (!res.ok) throw new Error(`API error ${res.status}`)
  return res.json()
}
