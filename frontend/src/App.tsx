import ClimateForm from './components/ClimateForm'

export default function App() {
  const handleRun = () => {
    console.log('Generate climate summary')
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
        <h2>Project Status</h2>

        <ul>
          <li>Frontend scaffold complete</li>
          <li>FastAPI backend scaffold complete</li>
          <li>Climate plotting engine scaffolded</li>
          <li>Validation framework implemented</li>
          <li>Month rotation logic implemented</li>
          <li>Fallback station logic scaffolded</li>
        </ul>
      </section>
    </main>
  )
}
