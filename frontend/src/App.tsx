import { useState } from 'react'

import ClimateForm from './components/ClimateForm'
import { generateClimateSummary } from './services/api'

export default function App() {
  const [response, setResponse] = useState<any>(null)

  const handleRun = async (payload: {
    station: string
    survey_month: string
    survey_year: number
  }) => {
    const result = await generateClimateSummary(payload)

    setResponse(result)
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

      <section className="panel">
        <h2>API Response</h2>

        <pre>
          {JSON.stringify(response, null, 2)}
        </pre>
      </section>

      <section className="panel">
        <h2>Project Status</h2>

        <ul>
          <li>Frontend scaffold complete</li>
          <li>FastAPI backend scaffold complete</li>
          <li>Frontend-backend communication implemented</li>
          <li>Climate plotting engine scaffolded</li>
          <li>Validation framework implemented</li>
          <li>Month rotation logic implemented</li>
          <li>Fallback station logic scaffolded</li>
        </ul>
      </section>
    </main>
  )
}
