from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

def build_model():
    model = BayesianModel([
        ('Is_Off_Hours', 'BreachWithin24h'),
        ('Short_Duration', 'BreachWithin24h'),
        ('Low_Byte_High_Packet', 'BreachWithin24h'),
        ('Suspicious_Port', 'BreachWithin24h')
    ])
    return model

def run_inference(model, df):
    # Fit the model using Bayesian Estimator
    from pgmpy.estimators import BayesianEstimator
    model.fit(df, estimator=BayesianEstimator, prior_type='BDeu')

    inference = VariableElimination(model)
    result = inference.query(
        variables=['BreachWithin24h'],
        evidence={
            'Is_Off_Hours': df['Is_Off_Hours'].cat.categories[0],
            'Short_Duration': df['Short_Duration'].cat.categories[1],
            'Low_Byte_High_Packet': df['Low_Byte_High_Packet'].cat.categories[0],
            'Suspicious_Port': df['Suspicious_Port'].cat.categories[1]
        }
    )
    return result

def visualize_model(model):
    import networkx as nx
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 6))

    # Convert model edges to networkx DiGraph
    G = nx.DiGraph()
    G.add_edges_from(model.edges())

    nx.draw(G, with_labels=True, node_size=2000, node_color='skyblue',
            font_size=10, font_weight='bold', arrows=True)

    plt.title("Bayesian Network Structure")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

