export async function generateClimateSummary(payload: {
  station: string
  survey_month: string
  survey_year: number
}) {
  const response = await fetch('http://127.0.0.1:8000/climate/summary', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  })

  if (!response.ok) {
    throw new Error('Failed to generate climate summary')
  }

  return response.json()
}
