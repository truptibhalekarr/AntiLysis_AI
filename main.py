from src.pipeline import TrainingPipeline

if __name__ == "__main__":
    # Initialize the modular pipeline
    pipeline = TrainingPipeline()

    # Fire up the engine
    pipeline.run_pipeline()