# Approach

1. Parse PDFs into hierarchical nodes with hashes
2. Store in SQLite with version tracking
3. Diff nodes by hash comparison
4. Select nodes and generate tests via Gemini
5. Track staleness by re-checking hashes
