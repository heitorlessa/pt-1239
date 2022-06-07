from aws_lambda_powertools import single_metric
from aws_lambda_powertools.metrics import MetricUnit


class Pool:
    def __init__(self) -> None:
        self.uuid = "f1316488-6aa6-464f-be78-13902b20ec33"
        self.name = "Prospects (Ireland) v2"
        self.min_size = "0"
        self.curr_size = "0"
        self.real_curr_size = "0"
        self.decommissioning_counter = "0"
        self.ready_counter = "0"
        self.creating_counter = "0"


metrics = Pool()


def lambda_handler(event, context):
    with single_metric(
        name="SlotAvailability", unit=MetricUnit.Percent, value=100
    ) as metric:
        metric.add_dimension(name="pool_id", value=metrics.uuid)
        metric.add_dimension(name="pool_name", value=metrics.name)
        metric.add_dimension(name="pool_min_size", value=metrics.min_size)
        metric.add_dimension(name="pool_curr_size", value=metrics.curr_size)
        metric.add_dimension(name="pool_real_size", value=metrics.real_curr_size)
        metric.add_dimension(
            name="pool_decommissioning_counter", value=metrics.decommissioning_counter
        )
        metric.add_dimension(name="pool_ready_counter", value=metrics.ready_counter)
        metric.add_dimension(
            name="pool_creating_counter", value=metrics.creating_counter
        )

    return {"body": "hello world", "statusCode": 200}
