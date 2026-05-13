# Climate Graphs

A production-ready climate summary automation platform for ecological and environmental reporting.

## Overview

This project replaces a semi-manual Excel climate workflow with a reproducible Python-native climate reporting platform.

The system automatically:

- retrieves BOM climate data
- validates and cleans datasets
- performs ecological-year month rotation
- calculates rolling climate anomalies
- generates publication-quality climate graphs
- generates deterministic narrative summaries
- exports report-ready outputs

## Frontend Stack

- Vite
- React
- TypeScript
- Tailwind CSS

## Backend Stack

- Python
- FastAPI
- pandas
- matplotlib
- pydantic
- geopandas

## Planned Features

- Automated BOM acquisition
- Intelligent fallback station selection
- Climate anomaly analysis
- High-resolution PNG exports
- SVG exports
- Optional Excel exports
- Deterministic climate narrative generation
- Structured logging and caching
- Visual regression testing

## Development

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn api.main:app --reload
```

## Repository Structure

```text
frontend/
backend/
config/
assets/
cache/
logs/
tests/
```
