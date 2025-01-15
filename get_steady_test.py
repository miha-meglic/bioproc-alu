from grenmlin import simulator
from scaling_alu import create_alu_model  # Changed import to correct file
import numpy as np

def test_get_steady():
    # Create model
    model = create_alu_model()
    model.generate_model()
    
    # Test case 1: Simple input (A0=100, A1=0, B0=100, B1=0, CarryIn=0, I0=0, I1=0)
    test_input = [100, 0, 100, 0, 0, 0, 0]
    
    print("Testing get_steady with inputs:", test_input)
    
    try:
        # Try different parameter combinations
        print("\nTest 1: Basic call")
        result1 = simulator.get_steady(
            grn=model,
            INS_def=[test_input]
        )
        print("Result 1:", result1)
        
        print("\nTest 2: With model parameter")
        import model as model_module
        result2 = simulator.get_steady(
            grn=model,
            INS_def=[test_input],
            model=model_module.solve_model
        )
        print("Result 2:", result2)
        
    except Exception as e:
        print(f"Error occurred: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        
if __name__ == "__main__":
    test_get_steady()