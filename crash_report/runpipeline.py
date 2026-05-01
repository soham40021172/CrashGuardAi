# crash_report/runpipeline.py

import argparse

from crash_report.pipeline.cleaning.load import run_cleaning_pipeline
from crash_report.modeling.train import run_train
from crash_report.modeling.predict import run_predection


def run_full_pipeline():
    print("🚀 Running Full ML System...\n")

    print("STEP 1 — Cleaning")
    run_cleaning_pipeline()

    print("\nSTEP 2 — Training")
    run_train()

    print("\n✅ Full Pipeline Completed Successfully")


def main():
    parser = argparse.ArgumentParser(description="Crash Report ML Pipeline")

    parser.add_argument(
        "--mode",
        choices=["all", "clean", "train", "predict"],
        required=True,
        help="Select which step to run",
    )

    args = parser.parse_args()

    if args.mode == "all":
        run_full_pipeline()

    elif args.mode == "clean":
        run_cleaning_pipeline()

    elif args.mode == "train":
        run_train()

    elif args.mode == "predict":
        run_predection()


if __name__ == "__main__":
    main()

#-----------------------------------
# ---------How To Run---------------
# python -m crash_report.runpipeline --mode all
# python -m crash_report.runpipeline --mode clean
# python -m crash_report.runpipeline --mode train
# python -m crash_report.runpipeline --mode predict    