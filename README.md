# Finn-Extractor-API

A FastAPI-based web scraper that extracts vehicle details from a Finn.no ad page based on a provided Finn code. This project demonstrates how to build an API using FastAPI, Docker, and web scraping techniques.

## Features
- Accepts a **POST** request with a Finn code.
- Extracts key details from the specified Finn.no webpage: https://www.finn.no/mobility/item/382633172
  - **Modellår** (Model Year)
  - **Kilometer** (Mileage)
  - **Girkasse** (Transmission)
  - **Drivstoff** (Fuel Type)
  - Includes the provided Finn code in the output.
- Returns the extracted data as a JSON response.
