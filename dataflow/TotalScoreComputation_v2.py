import apache_beam as beam

SOURCE_PATH = r"C:\Users\sneha.arumugam\apache_beam_demo\Source\student_scores.csv"
DEST_PATH = r"C:\Users\sneha.arumugam\apache_beam_demo\Sink\student_total_scores"

CSV_HEADER = "ID,Name,Physics,Chemistry,Math,English,Biology,History"

# Filter out CSV header
class FilterHeaderFn(beam.DoFn):
    def process(self, element):
        if element.strip() != CSV_HEADER:
            yield element

# Compute total score for each student
class ComputeTotalScoresFn(beam.DoFn):
    def process(self, element):
        parts = element.split(",")
        name = parts[1]
        total = sum(int(m) for m in parts[2:])  # sum all subject marks
        yield f"{name},{total}"

# Define pipeline
with beam.Pipeline() as pipeline:
    (
        pipeline
        | "Read CSV" >> beam.io.ReadFromText(SOURCE_PATH)
        | "Remove Header" >> beam.ParDo(FilterHeaderFn())
        | "Compute Total Marks" >> beam.ParDo(ComputeTotalScoresFn())
        | "Write Output" >> beam.io.WriteToText(
            DEST_PATH,
            file_name_suffix=".csv",
            num_shards=5  # split output into 5 files
        )
    )

print("✅ Pipeline execution completed successfully!")
