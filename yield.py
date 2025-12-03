import apache_beam as beam
 
LINES = [
"1/5/09 5:39,Shoes,1200,Amex,Netherlands",
"1/2/09 9:16,Jacket,1200,Mastercard,United States",
"1/5/09 10:08,Phone,3600,Visa,United States",
"1/2/09 14:18,Shoes,1200,Visa,United States",
"1/4/09 1:05,Phone,3600,Diners,Ireland",
"1/5/09 11:37,Books,1200,Visa,Canada"
]
 
class PrintToConsoleFn(beam.DoFn):
        def process(self, element):
            print(element)
            yield element
 
class ExtractPaymentTypeFn(beam.DoFn):
        def process(self, element):
            yield element.split(',')[3]
 
 
with beam.Pipeline() as p:
            (p
                | "ReadData" >> beam.Create(LINES)
                # | "PrintLines" >> beam.ParDo(PrintToConsoleFn())
                | "ExtractPaymentType" >> beam.ParDo(ExtractPaymentTypeFn())
                | "PrintPaymentType" >> beam.ParDo(PrintToConsoleFn())
            )