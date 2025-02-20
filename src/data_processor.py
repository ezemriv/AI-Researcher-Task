import polars as pl

def load_raw_data_save(read_path, save_path):
    df = pl.read_csv(read_path, try_parse_dates=True)

    df = df.with_columns([
        pl.col(col).cast(pl.Float32, strict=False) for col in df.columns if col != "Date Time"
    ])

    df.sort("Date Time").write_parquet(save_path)

    # Convert to NaN to later impute
    df = df.with_columns([
        pl.col("wv (m/s)").replace(-9999, None),
        pl.col("max. wv (m/s)").replace(-9999, None)
    ])

    return df