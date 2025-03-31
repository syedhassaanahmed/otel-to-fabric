# otel-to-fabric

## Data Flow

```mermaid
flowchart TD
    User((User)) -->|"Create Items"| FastAPI[FastAPI App]
    FastAPI -->|"Response"| User
    FastAPI -->|"OTel metrics over gRPC"| Collector[OTel Collector]
    Collector --> AzMon[Azure Monitor]
    Collector --> Fabric[Microsoft Fabric]
```

## Azure Monitor Setup

- Create an [Application Insights resource](https://learn.microsoft.com/en-us/azure/azure-monitor/app/create-workspace-resource?tabs=portal#create-an-application-insights-resource)
- Find the Application Insights [Connection String](https://learn.microsoft.com/en-us/azure/azure-monitor/app/connection-strings?tabs=net#find-your-connection-string)
- Create a `.env` file with the Application Insights Connection String. `sample.env` is provided as an example.
- This solution leverages the OpenTelemetry [Azure Monitor Exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/exporter/azuremonitorexporter/README.md) to send telemetry to Azure Monitor. Check out the docs for further config options.
- A [sample Azure Monitor Workbook](azmon/sample-azmon.workbook) is provided to demonstrate the querying capabilities.
<img src="azmon/sample-azmon-workbook.png">

## Run the E2E Solution
Open the solution in VS Code [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) or [GitHub Codespaces](https://github.com/codespaces).
```sh
docker compose up
```