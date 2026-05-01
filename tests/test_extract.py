from crash_report.pipeline.extract import DataExtractor

extractor = DataExtractor()
df = extractor.extract_raw_data()

print("Shape:", df.shape)
print(df.columns.tolist())