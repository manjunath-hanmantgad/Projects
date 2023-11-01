The architecture flow for the project is as follows:

```mermaid
graph TD;
    A[User Interface] -->|File Upload (ZIP)| B[ZIP Extraction];
    B -->|PDF to JPEG Conversion| C[GPT-4 Interaction];
    C -->|CSV Extraction & Grouping| D[Downloadable CSV Files];
```
