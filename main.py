from fastapi import FastAPI
from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
import os

# Set up OpenTelemetry metrics
endpoint = os.getenv("OTLP_ENDPOINT", "http://localhost:4317")
exporter = OTLPMetricExporter(endpoint=endpoint)
reader = PeriodicExportingMetricReader(exporter)
resource = Resource(attributes={SERVICE_NAME: "otel-to-fabric"})
provider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter("item.counter.meter")

item_counter = meter.create_counter(
    "item.counter", unit="items", description="Counts the number of items created"
)

app = FastAPI()


@app.get("/")
def get():
    return {"message": "Hello World"}


@app.post("/items/{quantity}")
def create(quantity: int):
    item_counter.add(quantity, attributes={"item.type": "item_type_1"})
    return {"message": f"{quantity} items created"}
