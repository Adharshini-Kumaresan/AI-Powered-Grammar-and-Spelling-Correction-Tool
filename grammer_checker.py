import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

def correct_grammar(text):
    """
    Uses DeepSeek AI to correct grammar and spelling errors in the given text.
    """
    prompt = f"Correct any spelling and grammar mistakes in the following text and provide explanations:\n\n{text}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No correction generated.")
    else:
        return f"Error: {response.text}"


# Minimal white + blue theme CSS
custom_css = """
.gradio-container {
    background-color: #F9F9F9 !important;
    font-family: 'Segoe UI', sans-serif;
    color: #333333;
}

textarea, input, .gr-button {
    border-radius: 8px !important;
}

textarea, input {
    background-color: white !important;
    border: 1px solid #CCCCCC !important;
    color: #333333 !important;
}

.gr-button {
    background-color: #007BFF !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
}

.gr-button:hover {
    background-color: #0056b3 !important;
}
"""

# Create Gradio interface
with gr.Blocks(css=custom_css) as interface:
    gr.Markdown(
        """
        <h1 style='text-align: center; color: #007BFF;'>AI Grammar & Spell Checker</h1>
        <p style='text-align: center; color: #555;'>Clean. Professional. Accurate.</p>
        """
    )
    
    input_text = gr.Textbox(lines=5, placeholder="Enter text with grammar or spelling mistakes", label="Your Text")
    output_text = gr.Textbox(label="Corrected Text")
    btn = gr.Button("Correct Grammar")
    
    btn.click(fn=correct_grammar, inputs=input_text, outputs=output_text)


# Launch the web app
if __name__ == "__main__":
    interface.launch()
