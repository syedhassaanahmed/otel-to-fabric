#!/bin/sh

echo "Starting load generator targeting: $API_ENDPOINT"

while true; do
  sleep 5
  quantity=$((1 + RANDOM % 100))
  echo "Sending POST request with quantity: $quantity"
  curl -X POST "$API_ENDPOINT/$quantity" -H "Content-Type: application/json"
done