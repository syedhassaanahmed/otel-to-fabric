# otel-to-fabric

```mermaid
flowchart TD
    User((User)) -->|"Create Items"| FastAPI[FastAPI App]
    FastAPI -->|"Response"| User
    FastAPI --> OTelSDK[OTEL SDK]
    OTelSDK --> Metrics["Counter Metric"]
    Metrics -->|"OTLP/gRPC"| Collector[OpenTelemetry Collector]
    Collector --> Fabric
    Collector --> AzMon[Azure Monitor]
```