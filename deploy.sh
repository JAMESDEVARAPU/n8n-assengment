#!/bin/bash
# Quick deployment script

echo "Building n8n Workflow Tracker..."
docker build -t n8n-workflow-tracker .

echo "Starting container..."
docker run -d \
  --name n8n-tracker \
  -p 8002:8002 \
  --env-file .env \
  n8n-workflow-tracker

echo "Deployment complete!"
echo "Access at: http://localhost:8002/frontend/index.html"