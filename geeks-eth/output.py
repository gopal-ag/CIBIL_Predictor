import gradio as gr
from blockchain import get_info  # This assumes get_info is a function that retrieves information based on an ID

def process_inputs():
    all_retrieved_info = ""  # Initialize a string to hold all retrieved information
    for i in range(21, 95):
        retrieved_info = get_info(i)  # Retrieve information for each ID
        all_retrieved_info += f"ID {i}: {retrieved_info}\n"  # Concatenate information with a newline
    return all_retrieved_info

iface = gr.Interface(
    fn=process_inputs,
    inputs=[],  # No inputs are needed
    outputs="text"
)

iface.launch()
