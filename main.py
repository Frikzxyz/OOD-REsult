import os
from src.pipeline import run_rolling_correlation_pipeline

if __name__ == "__main__":
    SPY_DATA_PATH = "data/spy_data.csv"
    INDICATOR_DATA_PATH = "data/CPI.csv"  # เปลี่ยนชื่อไฟล์ Indicator ได้ตามต้องการ
    OUTPUT_RESULT_PATH = "result/rolling_corr_result.csv"

    os.makedirs("result", exist_ok=True)

    print(f"กำลังเริ่มประมวลผล Cross-Correlation ระหว่าง SPY กับ {INDICATOR_DATA_PATH}...")

    results_df = run_rolling_correlation_pipeline(
        spy_path=SPY_DATA_PATH,
        indicator_path=INDICATOR_DATA_PATH,
        window_years=7,
        max_lag=14
    )

    results_df.to_csv(OUTPUT_RESULT_PATH, index=False)
    print(f"ประมวลผลสำเร็จ! บันทึกไฟล์ผลลัพธ์เรียบร้อยที่: {OUTPUT_RESULT_PATH}")