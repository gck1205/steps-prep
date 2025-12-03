import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run():
    options = PipelineOptions()
    p = beam.Pipeline(options=options)

    prices = [
        1367.36, 1360.66, 1394.20,
        1393.33, 1404.31, 1419.82,
        1429.73
    ]

    pcoll = p | "CreatePrices" >> beam.Create(prices)

    # SUM
    sum_result = (
        pcoll
        | "SumValues" >> beam.CombineGlobally(sum)
        | "PrintSum" >> beam.Map(lambda x: print(f"SUM: {x}") or x)
    )

    # MIN
    min_result = (
        pcoll
        | "MinValues" >> beam.CombineGlobally(min)
        | "PrintMin" >> beam.Map(lambda x: print(f"MIN: {x}") or x)
    )

    # MAX
    max_result = (
        pcoll
        | "MaxValues" >> beam.CombineGlobally(max)
        | "PrintMax" >> beam.Map(lambda x: print(f"MAX: {x}") or x)
    )

    # COUNT
    count_result = (
        pcoll
        | "CountValues" >> beam.combiners.Count.Globally()
        | "PrintCount" >> beam.Map(lambda x: print(f"COUNT: {x}") or x)
    )

    # MEAN
    mean_result = (
        pcoll
        | "MeanValues" >> beam.combiners.Mean.Globally()
        | "PrintMean" >> beam.Map(lambda x: print(f"MEAN: {x}") or x)
    )

    result = p.run()
    result.wait_until_finish()


if __name__ == "__main__":
    run()
