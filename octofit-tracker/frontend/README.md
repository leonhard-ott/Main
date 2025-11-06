# OctoFit Frontend (scaffold)

This is a minimal Vite + React scaffold for the OctoFit Tracker frontend.

How to run locally (from repository root):

```bash
# install dependencies
npm install --prefix octofit-tracker/frontend

# start dev server (exposed on 0.0.0.0:3000)
npm run dev --prefix octofit-tracker/frontend
```

Ports:
- Dev server: 3000 (public per project guidance)

Notes:
- The backend runs on 8000; you'll later point the frontend to the DRF API endpoints and enable CORS in the backend settings.
