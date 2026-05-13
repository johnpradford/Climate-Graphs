type Props = {
  onRun: () => void
}

export default function ClimateForm({ onRun }: Props) {
  return (
    <section className="panel">
      <h2>Climate Summary Inputs</h2>

      <div className="form-grid">
        <label>
          Station
          <input type="text" placeholder="Enter station name" />
        </label>

        <label>
          Survey Month
          <select>
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
          <input type="number" defaultValue={2025} />
        </label>
      </div>

      <button onClick={onRun}>
        Generate Climate Summary
      </button>
    </section>
  )
}
