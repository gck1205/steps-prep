import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class SplitWords(beam.DoFn):
    def process(self, element):
        words = element.lower().split(" ")
        for w in words:
            if w.strip():
                yield w

def run():
    options = PipelineOptions()
    p = beam.Pipeline(options=options)

    (
        p
        | "ReadFile" >> beam.io.ReadFromText(
            r"C:\Users\sneha.arumugam\apache_beam_demo\Source\SorrowsOfWerther.txt"
        )
        | "ExtractWords" >> beam.ParDo(SplitWords())
        | "CountWords" >> beam.combiners.Count.PerElement()
        | "FormatResults" >> beam.Map(lambda wc: f"{wc[0]}: {wc[1]}")
        | "WriteOutput" >> beam.io.WriteToText(
            r"C:\Users\sneha.arumugam\apache_beam_demo\Sink\word_count"
        )
    )

    p.run().wait_until_finish()
    print("✅ Pipeline executed successfully!")

if __name__ == "__main__":
    run()
