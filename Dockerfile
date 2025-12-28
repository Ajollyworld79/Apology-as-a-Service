FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY src/ src/
COPY pyproject.toml .

# Expose the port (Railway sets PORT env var, default to 8000 if not set)
ENV PORT=8000

# Run the server using mcp's CLI or direct python execution
# FastMCP provides an easy way to run SSE server
CMD ["python", "-m", "src.server"]
