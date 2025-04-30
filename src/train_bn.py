from features import load_data
from bayes_ids import build_model, run_inference, visualize_model

def main():
    # Load the data
    file_path = "src/cicids_bayesian_clean.csv"
      # Update if needed
    df = load_data(file_path)

    # Build and train model
    model = build_model()
    result = run_inference(model, df)

    # Print results
    print("Inference Result:")
    print(result)

    # Visualize
    visualize_model(model)

if __name__ == "__main__":
    main()
