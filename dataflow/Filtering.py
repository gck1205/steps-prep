import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


class FilterThresholdFn(beam.DoFn):
    def __init__(self, threshold):
        self.threshold = threshold

    def process(self, element):
        if element > self.threshold:
            yield element


def run():
    options = PipelineOptions()
    p = beam.Pipeline(options=options)

    goog_stock_prices = [
        1367.36, 1360.66, 1394.20,
        1393.33, 1404.31, 1419.82, 1429.73
    ]

    (
        p
        | "CreateList" >> beam.Create(goog_stock_prices)
        | "PrePrint" >> beam.Map(lambda x: print(f"-Pre-filtered: {x}") or x)
        | "FilterAbove1400" >> beam.ParDo(FilterThresholdFn(1400))
        | "PostPrint" >> beam.Map(lambda x: print(f"*Post-filtered: {x}") or x)
    )

    result = p.run()
    result.wait_until_finish()   # <<< VERY IMPORTANT FOR PRINTS


if __name__ == "__main__":
    run()
