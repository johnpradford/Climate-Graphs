import { useState } from 'react'

type Props = {
  onRun: (payload: {
    station: string
    survey_month: string
    survey_year: number
  }) => void
}

export default function ClimateForm({ onRun }: Props) {
  const [station, setStation] = useState('')
  const [surveyMonth, setSurveyMonth] = useState('October')
  const [surveyYear, setSurveyYear] = useState(2025)

  return (
    <section className="panel">
      <h2>Climate Summary Inputs</h2>

      <div className="form-grid">
        <label>
          Station
          <input
            type="text"
            placeholder="Enter station name"
            value={station}
            onChange={(event) => setStation(event.target.value)}
          />
        </label>

        <label>
          Survey Month
          <select
            value={surveyMonth}
            onChange={(event) => setSurveyMonth(event.target.value)}
          >
            <option>January</option>
            <option>February</option>
            <option>March</option>
            <option>April</option>
            <option>May</option>
            <option>June</option>
            <option>July</option>
            <option>August</option>
            <option>September</option>
            <option>October</option>
            <option>November</option>
            <option>December</option>
          </select>
        </label>

        <label>
          Survey Year
          <input
            type="number"
            value={surveyYear}
            onChange={(event) => setSurveyYear(Number(event.target.value))}
          />
        </label>
      </div>

      <button
        onClick={() =>
          onRun({
            station,
            survey_month: surveyMonth,
            survey_year: surveyYear,
          })
        }
      >
        Generate Climate Summary
      </button>
    </section>
  )
}
