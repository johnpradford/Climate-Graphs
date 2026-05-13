import { useState } from 'react'

import ClimateForm from './components/ClimateForm'
import ClimateResponse from './components/ClimateResponse'
import { generateClimateSummary } from './services/api'

export default function App() {
  const [response, setResponse] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  const handleRun = async (payload: {
    station: string
    survey_month: string
    survey_year: number
  }) => {
    setLoading(true)

    try {
      const result = await generateClimateSummary(payload)

      setResponse(result)
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="app-shell">
      <header>
        <h1>Climate Summary Engine</h1>

        <p>
          Automated climate reporting platform for ecological and environmental reporting.
        </p>
      </header>

      <ClimateForm onRun={handleRun} />

      {loading && (
        <section className="panel">
          <p>Generating climate summary...</p>
        </section>
      )}

      <ClimateResponse response={response} />

      <section className="panel">
        <h2>Project Status</h2>

        <ul>
          <li>Frontend scaffold complete</li>
          <li>FastAPI backend scaffold complete</li>
          <li>Frontend-backend communication implemented</li>
          <li>Climate plotting engine scaffolded</li>
          <li>Climate export workflow implemented</li>
          <li>Validation framework implemented</li>
          <li>Month rotation logic implemented</li>
          <li>Fallback station logic scaffolded</li>
          <li>Logging and caching scaffolded</li>
        </ul>
      </section>
    </main>
  )
}
