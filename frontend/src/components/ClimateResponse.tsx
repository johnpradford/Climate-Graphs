type Props = {
  response: any
}

export default function ClimateResponse({ response }: Props) {
  if (!response) {
    return null
  }

  return (
    <section className="panel">
      <h2>Climate Summary Result</h2>

      <div>
        <strong>Station:</strong> {response.station}
      </div>

      <div>
        <strong>Survey Year:</strong> {response.survey_year}
      </div>

      <div>
        <strong>Status:</strong> {response.status}
      </div>

      <div>
        <strong>Generated Figure:</strong>
        <pre>
          {response.summary?.output_path}
        </pre>
      </div>

      <div>
        <strong>Rotated Months:</strong>
        <pre>
          {JSON.stringify(response.rotated_months, null, 2)}
        </pre>
      </div>
    </section>
  )
}
